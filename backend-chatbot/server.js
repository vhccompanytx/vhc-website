import express from "express";
import cors from "cors";
import OpenAI from "openai";
import dotenv from "dotenv";
import { Resend } from "resend";
import fs from "fs";

dotenv.config();

const app = express();
app.use(cors({ origin: "*" }));
app.use(express.json());

app.get("/", (req, res) => {
  res.send(`
    <div style="font-family: sans-serif; text-align: center; padding: 50px;">
      <h1 style="color: #0b1332;">VHC Chatbot System</h1>
      <p style="color: #666;">Status: <span style="color: #2D7A4F; font-weight: bold;">ACTIVE</span></p>
      <hr style="max-width: 300px; border: 0; border-top: 1px solid #eee; margin: 20px auto;">
      <p style="font-size: 0.8em; color: #999;">© ${new Date().getFullYear()} VHC Company Services</p>
    </div>
  `);
});

const BRAND = "VHC Company Services";
const DEFAULT_LANG = "en";
const DEFAULT_MODEL = process.env.OPENAI_MODEL || "gpt-5.4-mini";
const DEFAULT_LEAD_EMAIL = process.env.LEAD_EMAIL || "sales@vhccompanytx.com";
const DEFAULT_FROM_EMAIL = process.env.FROM_EMAIL || "sales@vhccompanytx.com";
const DEFAULT_REPLY_TO_EMAIL = process.env.REPLY_TO_EMAIL || "sales@vhccompanytx.com";

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const resend = process.env.RESEND_API_KEY ? new Resend(process.env.RESEND_API_KEY) : null;

const sessions = new Map();
const SESSION_TTL = 5 * 60 * 1000;

function normalizeLang(value) {
  return String(value || "").toLowerCase() === "es" ? "es" : "en";
}

function inferLangFromMessage(text = "") {
  return /\b(hola|gracias|quiero|necesito|cotizacion|cotización|instalacion|instalación|bateria|batería|casa|negocio|servicio)\b/i.test(text)
    ? "es"
    : "en";
}

function getSession(id) {
  if (!sessions.has(id)) {
    sessions.set(id, {
      data: {
        nombre: null,
        telefono: null,
        ubicacion: null,
        proyecto: null,
        tipo: null,
        capacidad: null,
        tension: null,
        fecha: null,
        correo: null,
        lang: DEFAULT_LANG,
      },
      history: [],
      leadSent: false,
      techQuestions: 0,
      conflict: null,
      emailUpdated: false,
      emailRejected: false,
      lastActivity: Date.now(),
      lang: DEFAULT_LANG,
    });
  }
  const session = sessions.get(id);
  session.lastActivity = Date.now();
  return session;
}

setInterval(() => {
  const now = Date.now();
  for (const [id, session] of sessions) {
    if (now - session.lastActivity > SESSION_TTL) sessions.delete(id);
  }
}, 60_000);

const PHONE_RE = /(?:\+?1[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}/;
const EMAIL_RE = /[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}/;
const CAP_RE = /(\d+[\.,]?\d*)\s*(kw|kwh|kva|amps?|amp(?:s|erios?)?|panels?|paneles?|batter(?:y|ies)|bater[ií]as?)/i;
const TENSION_RE = /(\d{2,4})\s*v(?:olts?|oltios?)?\b/i;
const DATE_RE = /\b(today|tomorrow|this week|next week|this month|next month|urgent|asap|as soon as possible|\d+\s*days?|\d+\s*weeks?|\d+\s*months?|hoy|ma[nñ]ana|esta semana|pr[oó]xima semana|este mes|pr[oó]ximo mes|urgente|lo antes posible|\d+\s*d[ií]as?|\d+\s*semanas?|\d+\s*meses?)\b/i;
const LOCATION_RE = /\b(texas|tx|houston|katy|cypress|spring|the woodlands|pearland|pasadena|sugar land|missouri city|richmond|rosenberg|league city|galveston|conroe|tomball|humble|dallas|fort worth|arlington|plano|frisco|austin|san antonio|el paso|corpus christi|mcallen)\b/i;
const TYPE_HOME_RE = /\b(home|house|residential|residence|townhome|condo|apartment|casa|hogar|residencial|vivienda|apartamento)\b/i;
const TYPE_BIZ_RE = /\b(business|commercial|office|retail|warehouse|restaurant|shop|store|clinic|school|church|industrial|negocio|comercial|empresa|oficina|bodega|restaurante|local|industrial)\b/i;
const PROJECT_RE = /\b(solar|panels?|paneles?|battery|backup|generator|ev charger|charger|electrical|breaker|main panel|subpanel|rewire|troubleshoot|inspection|permit|roof|roofing|inverter|powerwall|instalaci[oó]n|paneles? solares|bater[ií]a|respaldo|cargador ev|cargador|el[eé]ctrico|tablero|interruptor|medidor|inversor|generador|revisi[oó]n|mantenimiento|reparar|instalar|agregar|a[ñn]adir|ampliar|expand|upgrade|monitoring|generation|energy storage|sistema solar|solar system)\b/i;
// Catches layman intent phrases that clearly describe solar/electrical work even without explicit tech keywords
const SOLAR_INTENT_RE = /\b(panel|solar|energy|battery|electric|install|add|expand|upgrade|system|inverter|backup|ev|charger|energ[ií]a|bater[ií]a|instalar|agregar|ampliar|sistema)\b/i;
const NAME_TRIGGER_RE = /(?:(?:my name is|i am|i'm|call me|me llamo|soy|mi nombre es|nombre es)\s+)([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'\-]{1,}(?:\s+[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'\-]{1,}){0,2})/i;
const NAME_BLOCK_RE = /^(no|yes|si|ok|okay|hola|hello|gracias|thanks|quiero|necesito|i|we|our|para|for|de|la|el|san|santa|texas|houston|katy|cypress|spring)$/i;
const NOT_A_NAME_RE = /\b(city|state|street|avenue|road|project|installation|quote|estimate|service|servicio|proyecto|instalaci[oó]n|cotizaci[oó]n|texas|houston|business|negocio|empresa)\b/i;
const BLOCK_PROJECT_RE = /\b(plumbing|hvac|air conditioning|ac|heater|leak|water|pipe|plomeria|plomero|aire acondicionado|calefaccion|fuga|agua|tuberia)\b/i;
const TECH_RE = /\b(voltage|amps?|ampacity|kw|kva|breaker|panel|inverter|battery|solar|roof|permit|electrical|wire|cable|ground|generator|voltaje|amperios|tension|tensión|tablero|inversor|bater[ií]a|solar|el[eé]ctrico|cable|generador)\b/i;
const UPDATE_RE = /\b(update|change|correct|correction|that'?s not right|actualizar|cambiar|me equivoqu[eé]|corregir|correcci[oó]n|no es)\b/i;

function cleanPhone(raw) {
  const digits = String(raw || "").replace(/\D/g, "");
  if (digits.length === 11 && digits.startsWith("1")) return digits.slice(1);
  return digits;
}

function isValidUSPhone(phone) {
  return /^\d{10}$/.test(cleanPhone(phone));
}

function capitalizeWords(text) {
  return String(text || "")
    .trim()
    .split(/\s+/)
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1).toLowerCase())
    .join(" ");
}

function fixCommonEmailTypos(text) {
  let fixed = String(text || "");
  fixed = fixed.replace(/@(gmil|gmai|gamil|gmail|gimail)\.(com?|co|con|c0m|clm)\b/i, "@gmail.com");
  fixed = fixed.replace(/@(hotmail|hotmai|hormail)\.(com?|co|con|c0m)\b/i, "@hotmail.com");
  fixed = fixed.replace(/@(yahoo)\.(com?|co|con|c0m)\b/i, "@yahoo.com");
  fixed = fixed.replace(/@(outlook)\.(com?|co|con|c0m)\b/i, "@outlook.com");
  if (!fixed.includes("@")) {
    fixed = fixed.replace(/\s*(gmail\.com|hotmail\.com|yahoo\.com|outlook\.com)$/i, "@$1");
  }
  return fixed.replace(/@@+/g, "@");
}

function getLabels(lang) {
  if (lang === "es") {
    return {
      internalLead: "Nuevo lead",
      internalCustomer: "Cliente",
      internalConversation: "Conversacion",
      internalGenerated: "Generado por VHC Website Chatbot",
      type: "Tipo",
      name: "Nombre",
      phone: "Telefono",
      email: "Correo",
      location: "Ubicacion",
      project: "Proyecto",
      capacity: "Capacidad",
      voltage: "Voltaje",
      date: "Fecha deseada",
      customerSubject: (name) => `Recibimos tu solicitud, ${name} | ${BRAND}`,
      customerGreeting: (name) => `Hola, ${name}`,
      customerIntro: "Recibimos tu solicitud y nuestro equipo se pondra en contacto contigo pronto.",
      customerRequest: "Tu solicitud",
      customerNote: (phone) => `Te contactaremos al ${phone} o a este mismo correo.`,
      contactLabel: "Consultas",
      companyLine: "Instalacion solar y servicios electricos en Texas",
      language: "Idioma",
      languageVal: "🇲🇽 Español",
    };
  }

  return {
    internalLead: "New lead",
    internalCustomer: "Customer",
    internalConversation: "Conversation",
    internalGenerated: "Generated by VHC Website Chatbot",
    type: "Type",
    name: "Name",
    phone: "Phone",
    email: "Email",
    location: "Location",
    project: "Project",
    capacity: "System details",
    voltage: "Voltage",
    date: "Desired timeline",
    customerSubject: (name) => `We received your request, ${name} | ${BRAND}`,
    customerGreeting: (name) => `Hello, ${name}`,
    customerIntro: "We received your request and our team will reach out soon.",
    customerRequest: "Your request",
    customerNote: (phone) => `We will contact you at ${phone} or by replying to this email.`,
    contactLabel: "Questions",
    companyLine: "Texas solar installation and electrical services",
    language: "Language",
    languageVal: "🇺🇸 English",
  };
}
function lastAsked(history) {
  const last = [...history].reverse().find((item) => item.role === "assistant");
  if (!last) return null;
  const text = String(last.content || "").toLowerCase();
  if (/full name|last name|nombre completo|apellido/.test(text)) return "nombre";
  if (/phone|telefono|teléfono|contact number/.test(text)) return "telefono";
  if (/email|correo/.test(text)) return "correo";
  if (/city in texas|service address|property located|ubicacion|ubicación|ciudad en texas|direccion del proyecto|dirección del proyecto/.test(text)) return "ubicacion";
  if (/system size|capacity|kw|kva|capacidad/.test(text)) return "capacidad";
  if (/voltage|voltaje|tension|tensión/.test(text)) return "tension";
  // Broad match: any phrasing asking for service/project type
  if (/\b(project|service|need help|what service|what kind|type of service|type of project|trabajo|proyecto|servicio|necesitas|en qu[eé] (te |le )?podemos|qu[eé] (servicio|tipo|proyecto))\b/.test(text)) return "proyecto";
  if (/timeline|when do you need|cuando lo necesitas|cuándo lo necesitas|cuando necesitas|cuándo necesitas|fecha deseada/.test(text)) return "fecha";
  return null;
}

function extractData(message, session) {
  const raw = String(message || "").trim();
  const lowered = raw.toLowerCase();
  session.emailRejected = false; // reset each turn — re-set below if a bad email is detected
  const asked = lastAsked(session.history);
  const data = session.data;

  if (!data.tipo) {
    if (TYPE_HOME_RE.test(raw)) data.tipo = "residential";
    else if (TYPE_BIZ_RE.test(raw)) data.tipo = "commercial";
  }

  if (!data.telefono) {
    const match = raw.match(PHONE_RE);
    if (match) data.telefono = cleanPhone(match[0]);
  }

  if (!data.correo) {
    const fixed = fixCommonEmailTypos(raw);
    const match = fixed.match(EMAIL_RE);
    if (match) data.correo = match[0].toLowerCase();
  }

  if (!data.capacidad) {
    const match = raw.match(CAP_RE);
    if (match) data.capacidad = match[0];
  }

  if (!data.tension) {
    const match = raw.match(TENSION_RE);
    if (match) data.tension = match[0];
  }

  if (!data.fecha) {
    const match = raw.match(DATE_RE);
    if (match) data.fecha = match[0];
  }

  if (!data.ubicacion && LOCATION_RE.test(raw)) {
    data.ubicacion = raw.slice(0, 120);
  }

  // Accept any solar/electrical intent — including layman phrasing like "add panels", "my system"
  if (!data.proyecto && (PROJECT_RE.test(raw) || SOLAR_INTENT_RE.test(raw)) && !BLOCK_PROJECT_RE.test(raw)) {
    data.proyecto = raw.split(".")[0].slice(0, 220);
  }

  if (!data.nombre) {
    const match = raw.match(NAME_TRIGGER_RE);
    if (match) {
      const candidate = match[1].trim();
      if (!NAME_BLOCK_RE.test(candidate) && !NOT_A_NAME_RE.test(candidate)) {
        data.nombre = capitalizeWords(candidate);
      }
    }
  }

  if (asked === "nombre" && !data.nombre) {
    let cleanName = raw.replace(/^(yeah|yes|yep|sure|ok|okay|si|sí|claro|exacto|por supuesto|hola|hello|hi|good morning|buenos dias|buenas tardes|me llamo|mi nombre es|soy|nombre es|i am|i'm|my name is|call me is|it is|it's|is)[,\-\s.:]+/i, "").trim();
    const words = cleanName.split(/\s+/).filter(Boolean);
    if (
      words.length >= 1 &&
      words.length <= 4 &&
      /^[A-Za-zÀ-ÿ'\-\s]+$/.test(cleanName) &&
      !NAME_BLOCK_RE.test(words[0]) &&
      !NOT_A_NAME_RE.test(cleanName.toLowerCase()) &&
      !LOCATION_RE.test(cleanName.toLowerCase())
    ) {
      data.nombre = capitalizeWords(cleanName);
    }
  }

  if (asked === "telefono" && !data.telefono) {
    const cleaned = cleanPhone(raw);
    if (isValidUSPhone(cleaned)) data.telefono = cleaned;
  }

  if (asked === "correo" && !data.correo) {
    const fixed = fixCommonEmailTypos(raw);
    const match = fixed.match(EMAIL_RE);
    if (match) {
      data.correo = match[0].toLowerCase();
    } else {
      // Detect if the user clearly tried to give an email but the format is invalid
      const looksLikeEmailAttempt =
        raw.includes('@') ||
        /\b(gmail|yahoo|hotmail|outlook|icloud|mail)\b/i.test(raw) ||
        /\b\w+\.\w{2,4}$/.test(raw);
      if (looksLikeEmailAttempt) session.emailRejected = true;
    }
  }

  if (asked === "ubicacion" && !data.ubicacion && raw.length >= 3) {
    data.ubicacion = raw.slice(0, 120);
  }

  if (asked === "capacidad" && !data.capacidad) {
    const match = raw.match(CAP_RE);
    if (match) data.capacidad = match[0];
  }

  if (asked === "tension" && !data.tension) {
    const match = raw.match(TENSION_RE);
    if (match) data.tension = match[0];
    else if (/^\d{2,4}$/.test(raw)) data.tension = `${raw}V`;
  }

  // KEY FIX: When the bot explicitly asked for the project, accept any non-blocked response.
  // Don't double-gate with PROJECT_RE — the AI conversation handles understanding; we just need to store it.
  if (asked === "proyecto" && !data.proyecto && raw.length >= 5 && !BLOCK_PROJECT_RE.test(raw)) {
    data.proyecto = raw.slice(0, 220);
  }

  if (asked === "fecha" && !data.fecha && raw.length >= 2) {
    data.fecha = raw.slice(0, 80);
  }

  if (!data.proyecto && data.tipo && !asked) {
    const looksLikeContact =
      PHONE_RE.test(raw) ||
      EMAIL_RE.test(raw) ||
      CAP_RE.test(raw) ||
      TENSION_RE.test(raw) ||
      (LOCATION_RE.test(raw) && raw.split(/\s+/).length <= 4);
    if (!looksLikeContact && raw.split(/\s+/).length >= 3) {
      // Also catch layman solar intent (e.g. "add panels", "expand my system")
      if ((PROJECT_RE.test(raw) || SOLAR_INTENT_RE.test(raw)) && !BLOCK_PROJECT_RE.test(raw)) {
        data.proyecto = raw.slice(0, 220);
      }
    }
  }
}

function isLeadComplete(data) {
  const hasFullName = Boolean(data.nombre && data.nombre.trim().includes(" "));
  const hasPhone = isValidUSPhone(data.telefono);
  const base = hasFullName && hasPhone && data.correo && data.proyecto && data.ubicacion;
  if (data.tipo === "residential") return Boolean(base);
  if (data.tipo === "commercial") return Boolean(base && (data.capacidad || data.tension));
  return Boolean(hasFullName && hasPhone && data.correo);
}

function getMissingField(data, lang) {
  if (lang === "es") {
    const residential = [
      !data.proyecto && "que servicio necesitas",
      !data.ubicacion && "la ciudad o area del proyecto en Texas",
      (!data.nombre || !data.nombre.trim().includes(" ")) && "tu nombre completo",
      !data.telefono && "tu numero de telefono",
      !data.correo && "tu correo electronico",
    ].filter(Boolean);

    const commercial = [
      !data.proyecto && "el servicio o alcance del proyecto",
      !data.ubicacion && "la ubicacion del negocio o propiedad en Texas",
      (!data.nombre || !data.nombre.trim().includes(" ")) && "tu nombre completo",
      !data.telefono && "tu numero de telefono",
      !data.correo && "tu correo electronico",
      !data.capacidad && !data.tension && "el tamano del sistema, capacidad o voltaje",
      !data.fecha && "cuando te gustaria iniciar",
    ].filter(Boolean);

    return data.tipo === "commercial" ? commercial[0] : residential[0];
  }

  const residential = [
    !data.proyecto && "what service you need",
    !data.ubicacion && "the Texas city or service area",
    (!data.nombre || !data.nombre.trim().includes(" ")) && "your full name",
    !data.telefono && "your phone number",
    !data.correo && "your email address",
  ].filter(Boolean);

  const commercial = [
    !data.proyecto && "the service scope or project type",
    !data.ubicacion && "the property or business location in Texas",
    (!data.nombre || !data.nombre.trim().includes(" ")) && "your full name",
    !data.telefono && "your phone number",
    !data.correo && "your email address",
    !data.capacidad && !data.tension && "system size, capacity, or voltage",
    !data.fecha && "your expected timeline",
  ].filter(Boolean);

  return data.tipo === "commercial" ? commercial[0] : residential[0];
}

function buildPrompt(data, session) {
  const lang = normalizeLang(session.lang || data.lang || DEFAULT_LANG);
  const techRule =
    lang === "es"
      ? session.techQuestions >= 2
        ? 'TOPE TECNICO ACTIVO: ya respondiste 2 consultas tecnicas. Si llega otra consulta tecnica, responde exactamente: "Para ese detalle, uno de nuestros especialistas te asesora mejor. ¿Te contactamos?"'
        : `Puedes responder hasta ${2 - session.techQuestions} consulta(s) tecnica(s) mas. Cada respuesta tecnica debe ser muy breve y nunca incluir precios.`
      : session.techQuestions >= 2
        ? 'TECHNICAL LIMIT ACTIVE: you already answered 2 technical questions. If another technical question comes in, reply exactly: "For that detail, one of our specialists can advise you better. Would you like us to contact you?"'
        : `You may answer up to ${2 - session.techQuestions} more technical question(s). Every technical answer must stay very brief and never include pricing.`;

  const priceRule =
    lang === "es"
      ? "REGLA DE PRECIOS: nunca des precios, rangos ni estimados. Si el usuario pide precio, explica que VHC prepara cotizaciones personalizadas despues de revisar el proyecto y pide sus datos."
      : "PRICING RULE: never give prices, ranges, or estimates. If the user asks for pricing, explain that VHC prepares custom quotes after reviewing the project and ask for their contact details.";

  const outOfScopeRule =
    lang === "es"
      ? "FUERA DE ALCANCE: solo atiendes servicios de VHC Company Services relacionados con instalacion solar residencial, sistemas de respaldo con bateria, cargadores EV, evaluaciones solares y servicios electricos residenciales en Texas. Si el usuario pide algo fuera de eso (ej: plomería, HVAC), dile amablemente que no ofrecemos ese servicio y pregúntale directamente si le interesa recibir información sobre nuestros paneles solares o servicios eléctricos."
      : "OUT OF SCOPE: you only handle VHC Company Services requests related to residential solar installation, battery backup systems, EV chargers, solar evaluations, and residential electrical services in Texas. If the user asks for something else (e.g. plumbing, HVAC), politely decline and explicitly ask if they would be interested in learning about our solar panel or electrical services instead.";

  const rejectionRule =
    lang === "es"
      ? "CIERRE PREMATURO: Si el usuario intenta despedirse pero faltan datos, dile amablemente que aun necesitas esa informacion (como telefono o correo) para enviar su solicitud, y vuelvesela a pedir. Si se niega rotundamente, despídete y no sigas preguntando."
      : "PREMATURE CLOSING: If the user tries to end the conversation but details are missing, politely explain that you still need that information to submit their request, and ask again. Stop asking only if they explicitly refuse to provide it.";
  if (session.emailRejected) {
    return lang === "es"
      ? `Eres el asistente de ${BRAND}. El usuario acaba de intentar proporcionar su correo electrónico pero el formato no es válido—parece que falta "@" o el dominio (ej: nombre@gmail.com). Díselo amablemente y pídele que lo vuelva a escribir correctamente. Máximo 2 líneas.`
      : `You are the assistant for ${BRAND}. The customer just tried to provide their email address but it wasn't valid—it appears to be missing "@" or the domain (e.g. name@gmail.com). Please politely let them know and ask them to re-enter it in the correct format. Maximum 2 lines.`;
  }

  if (session.conflict) {
    return lang === "es"
      ? `Detectaste un conflicto en ${session.conflict.field}. Antes estaba guardado "${session.conflict.old}" y ahora recibiste "${session.conflict.new}". Haz una sola pregunta para confirmar cual dato es correcto y nada mas.`
      : `You detected a conflict for ${session.conflict.field}. The previous value was "${session.conflict.old}" and the new value is "${session.conflict.new}". Ask one single clarifying question and nothing else.`;
  }

  if (!data.tipo) {
    return lang === "es"
      ? `Eres el asistente virtual de ${BRAND}. Atiendes clientes de Texas para instalacion solar residencial, sistemas de respaldo con bateria, cargadores EV, evaluaciones solares y servicios electricos residenciales.

COMPORTAMIENTO:
- Si el usuario solo saluda, presentate brevemente y pregunta en que puedes ayudar.
- Si el usuario tiene intencion comercial clara, no repitas la presentacion y pregunta directamente si el proyecto es para casa o negocio.
- Si el usuario ya dio contexto suficiente, clasifica y avanza sin repetir preguntas.
- Responde en espanol neutro.
- Maximo 2 lineas por respuesta.
- Nunca repitas la misma pregunta.

${rejectionRule}
${outOfScopeRule}
${priceRule}
${techRule}`
      : `You are the virtual assistant for ${BRAND}. You help Texas customers with residential solar installation, battery backup systems, EV chargers, solar site evaluations, and residential electrical services.

BEHAVIOR:
- If the user only says hello, briefly introduce yourself and ask how you can help.
- If the user clearly wants a quote or service, do not repeat the intro and ask whether the project is for a home or a business.
- If the user already gave enough context, classify and move forward without repeating questions.
- Reply in natural English.
- Maximum 2 lines per reply.
- Never repeat the same question.

${rejectionRule}
${outOfScopeRule}
${priceRule}
${techRule}`;
  }

  const confirmed = Object.entries(data)
    .filter(([key, value]) => value !== null && key !== "lang")
    .map(([key, value]) => `${key}="${value}"`)
    .join(", ");

  const missing = getMissingField(data, lang);

  if (!missing) {
    return lang === "es"
      ? `Eres el asistente de ${BRAND}. El lead esta completo.
Datos confirmados: ${confirmed}.
Agradece, confirma que un asesor de VHC dara seguimiento y mantente en maximo 2 lineas.
${rejectionRule}
${outOfScopeRule}
${priceRule}
${techRule}`
      : `You are the assistant for ${BRAND}. The lead is complete.
Confirmed details: ${confirmed}.
Thank the user, confirm that a VHC specialist will follow up, and stay within 2 lines.
${rejectionRule}
${outOfScopeRule}
${priceRule}
${techRule}`;
  }

  const strictRule =
    lang === "es"
      ? "ESTRICTO: Si el usuario dio un dato y este YA aparece en la lista 'YA TIENES' (aunque tenga otro formato, porque el sistema lo limpia), acéptalo y pasa a pedir lo que diga 'SOLO FALTA'. PERO si no aparece en 'YA TIENES' y el sistema sigue pidiendo lo mismo en 'SOLO FALTA', significa que el formato fue inválido (ej: teléfono sin 10 dígitos). Dile que el dato es incorrecto y vuelve a pedirlo."
      : "STRICT: If the user provided a detail and it NOW appears in the 'YOU ALREADY HAVE' list (even in a cleaned format), accept it and ask for what is in 'ONLY ASK FOR'. BUT if it does not appear in 'YOU ALREADY HAVE', it means the backend rejected it (e.g. phone not 10 digits). In that case, tell them it was invalid and ask for it again.";

  return lang === "es"
    ? `Eres el asistente de ${BRAND}. Cliente tipo ${data.tipo}.
YA TIENES: ${confirmed || "ningun dato"}.
SOLO FALTA: "${missing}".

REGLAS:
1. Haz una sola pregunta por turno.
2. Confirma brevemente el dato recibido y pregunta el siguiente.
3. Tu respuesta debe terminar con una pregunta.
4. Tono amigable, profesional y breve.
5. Maximo 2 lineas.
${rejectionRule}
${outOfScopeRule}
${priceRule}
${techRule}
${strictRule}`
    : `You are the assistant for ${BRAND}. Customer type: ${data.tipo}.
YOU ALREADY HAVE: ${confirmed || "no details yet"}.
ONLY ASK FOR: "${missing}".

RULES:
1. Ask only one question per turn.
2. Briefly confirm the received detail and ask the next one.
3. Your response must end with a question.
4. Keep the tone friendly, professional, and brief.
5. Maximum 2 lines.
${rejectionRule}
${outOfScopeRule}
${priceRule}
${techRule}
${strictRule}`;
}

function buildRows(data, lang) {
  const labels = getLabels(lang);
  return [
    [labels.type, data.tipo || "-"],
    [labels.name, data.nombre || "-"],
    [labels.phone, data.telefono || "-"],
    [labels.email, data.correo || "-"],
    [labels.location, data.ubicacion || "-"],
    [labels.project, data.proyecto || "-"],
    data.capacidad && [labels.capacity, data.capacidad],
    data.tension && [labels.voltage, data.tension],
    data.fecha && [labels.date, data.fecha],
    [labels.language, labels.languageVal],
  ].filter(Boolean);
}

async function sendLeadEmail(data, history) {
  if (!resend) return;

  const lang = normalizeLang(data.lang);
  const labels = getLabels(lang);
  const rows = buildRows(data, lang)
    .map(
      ([label, value]) =>
        `<tr><td style="padding:8px 12px;font-weight:600;background:#f5f7fb;border:1px solid #d9e0ef">${label}</td><td style="padding:8px 12px;border:1px solid #d9e0ef">${value}</td></tr>`
    )
    .join("");

  const transcript = history
    .filter((item) => item.role !== "system")
    .map((item) => {
      const speaker = item.role === "user" ? labels.internalCustomer : "Bot";
      const bg = item.role === "user" ? "#eef4ff" : "#fafbfd";
      return `<tr style="background:${bg}"><td style="padding:6px 12px;font-weight:600;border:1px solid #e5eaf4;white-space:nowrap">${speaker}</td><td style="padding:6px 12px;border:1px solid #e5eaf4">${item.content}</td></tr>`;
    })
    .join("");

  await resend.emails.send({
    from: `${BRAND} <${DEFAULT_FROM_EMAIL}>`,
    to: DEFAULT_LEAD_EMAIL,
    replyTo: DEFAULT_REPLY_TO_EMAIL,
    subject: `${labels.internalLead}: ${data.nombre || "Unknown"} | ${BRAND}`,
    html: `<!DOCTYPE html><html><body style="font-family:system-ui,-apple-system,sans-serif;max-width:700px;margin:auto;background-color:#f9fafb;padding:20px">
      <div style="background-color:#ffffff;border:1px solid #e5e7eb;border-radius:12px;overflow:hidden;box-shadow:0 1px 3px 0 rgba(0,0,0,0.1)">
        <h2 style="background:#0b1332;color:#fff;padding:20px 24px;margin:0;font-size:20px;font-weight:600">${labels.internalLead}</h2>
        <div style="padding:24px">
          <p style="margin-top:0;color:#6b7280;font-size:14px;margin-bottom:20px">${labels.companyLine}</p>
          <table style="border-collapse:collapse;width:100%;font-size:14px;border:1px solid #e5e7eb">
            ${rows}
          </table>
          
          <h3 style="margin:32px 0 16px;color:#111827;font-size:16px;font-weight:600;border-bottom:2px solid #f3f4f6;padding-bottom:8px">${labels.internalConversation}</h3>
          <div style="background:#fdfdfd;border:1px solid #f3f4f6;border-radius:8px;overflow:hidden">
            <table style="border-collapse:collapse;width:100%;font-size:13px">
              ${transcript}
            </table>
          </div>
          
          <p style="font-size:11px;color:#9ca3af;margin-top:24px;text-align:center">${labels.internalGenerated}</p>
        </div>
      </div>
    </body></html>`,
  });
}

async function sendConfirmationEmail(data) {
  if (!resend || !data.correo || !data.correo.includes("@")) return;

  const lang = normalizeLang(data.lang);
  const labels = getLabels(lang);
  const rows = buildRows(data, lang)
    .map(
      ([label, value]) =>
        `<tr><td style="padding:8px 16px;font-weight:600;background:#f5f7fb;border:1px solid #d9e0ef;width:160px">${label}</td><td style="padding:8px 16px;border:1px solid #d9e0ef">${value}</td></tr>`
    )
    .join("");

  await resend.emails.send({
    from: `${BRAND} <${DEFAULT_FROM_EMAIL}>`,
    to: data.correo,
    replyTo: DEFAULT_REPLY_TO_EMAIL,
    subject: labels.customerSubject(data.nombre || "Customer"),
    html: `<!DOCTYPE html><html><body style="margin:0;padding:0;background:#eef2f8;font-family:system-ui,sans-serif">
      <table width="100%" cellpadding="0" cellspacing="0" style="background:#eef2f8;padding:40px 0">
        <tr><td align="center">
          <table width="580" cellpadding="0" cellspacing="0" style="background:#ffffff;border-radius:14px;overflow:hidden">
            <tr><td style="background:#0b1332;padding:28px 32px">
              <p style="margin:0;color:#ffffff;font-size:22px;font-weight:700">${BRAND}</p>
              <p style="margin:6px 0 0;color:rgba(255,255,255,0.72);font-size:13px">${labels.companyLine}</p>
            </td></tr>
            <tr><td style="padding:32px">
              <p style="margin:0 0 10px;font-size:20px;font-weight:700;color:#0b1332">${labels.customerGreeting(data.nombre || "Customer")}</p>
              <p style="margin:0 0 24px;color:#455066;font-size:14px;line-height:1.7">${labels.customerIntro}</p>
              <p style="margin:0 0 10px;font-weight:700;color:#0b1332;font-size:13px;text-transform:uppercase;letter-spacing:.04em">${labels.customerRequest}</p>
              <table width="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;font-size:14px;margin-bottom:24px">${rows}</table>
              <div style="background:#f7f9fc;border:1px solid #d9e0ef;border-radius:10px;padding:16px 18px;margin-bottom:20px">
                <p style="margin:0;color:#1f2937;font-size:14px">${labels.customerNote(data.telefono || "-")}</p>
              </div>
              <p style="margin:0;color:#5b6478;font-size:13px">${labels.contactLabel}: <a href="mailto:${DEFAULT_REPLY_TO_EMAIL}" style="color:#1b2d6e;font-weight:600">${DEFAULT_REPLY_TO_EMAIL}</a></p>
            </td></tr>
          </table>
        </td></tr>
      </table>
    </body></html>`,
  });
}
function saveLeadToFile(data) {
  try {
    const path = "./leads.json";
    const leads = fs.existsSync(path) ? JSON.parse(fs.readFileSync(path, "utf-8") || "[]") : [];
    leads.push({ ...data, telefono: cleanPhone(data.telefono), guardado: new Date().toISOString() });
    fs.writeFileSync(path, JSON.stringify(leads, null, 2));
  } catch (error) {
    console.error("[VHC] saveLeadToFile:", error.message);
  }
}

const rateStore = new Map();
function isRateLimited(ip) {
  const now = Date.now();
  const hits = (rateStore.get(ip) || []).filter((timestamp) => now - timestamp < 60_000);
  hits.push(now);
  rateStore.set(ip, hits);
  return hits.length > 25;
}

app.post("/chat", async (req, res) => {
  const ip = req.headers["x-forwarded-for"]?.split(",")[0] || req.socket.remoteAddress;
  if (isRateLimited(ip)) {
    return res.status(429).json({ error: "Too many requests. Please wait a moment." });
  }

  const { message, sessionId, reset, lang } = req.body;
  if (!sessionId || typeof sessionId !== "string") {
    return res.status(400).json({ error: "sessionId required" });
  }

  if (reset) {
    sessions.delete(sessionId);
    return res.json({ reply: "session reset", meta: { reset: true } });
  }

  if (!message || typeof message !== "string" || !message.trim()) {
    return res.status(400).json({ error: "Empty message" });
  }

  const trimmed = message.trim().slice(0, 600);
  const session = getSession(sessionId);
  session.lang = normalizeLang(lang || session.lang || inferLangFromMessage(trimmed));
  session.data.lang = session.lang;

  const fixedMessage = fixCommonEmailTypos(trimmed);
  const isUpdate = UPDATE_RE.test(trimmed);

  const extract = {};
  const phoneMatch = trimmed.match(PHONE_RE);
  if (phoneMatch) extract.telefono = cleanPhone(phoneMatch[0]);
  const emailMatch = fixedMessage.match(EMAIL_RE);
  if (emailMatch) extract.correo = emailMatch[0].toLowerCase();
  const nameMatch = trimmed.match(NAME_TRIGGER_RE);
  if (nameMatch) extract.nombre = capitalizeWords(nameMatch[1]);
  if (LOCATION_RE.test(trimmed)) extract.ubicacion = trimmed.match(LOCATION_RE)[0];

  const lastAssistant = [...session.history].reverse().find((item) => item.role === "assistant");
  if (
    lastAssistant &&
    /apellido|full name|last name/.test(String(lastAssistant.content || "").toLowerCase()) &&
    session.data.nombre &&
    !session.data.nombre.includes(" ")
  ) {
    const cleanNameTail = trimmed.trim();
    if (/^[A-Za-zÀ-ÿ'\-\s]{2,30}$/.test(cleanNameTail)) {
      session.data.nombre = capitalizeWords(`${session.data.nombre} ${cleanNameTail}`);
    }
  }

  if (session.conflict) {
    const field = session.conflict.field;
    if (
      /\b(yes|si|correct|correcto|this one|este|new|nuevo|old|anterior|previous|ese)\b/i.test(trimmed) ||
      (extract[field] && String(extract[field]).toLowerCase() === String(session.data[field]).toLowerCase())
    ) {
      if (extract[field]) {
        session.data[field] = extract[field];
        if (field === "correo") session.emailUpdated = true;
      }
      session.conflict = null;
    }
  }

  let caughtConflict = null;
  for (const key of ["telefono", "correo", "ubicacion", "nombre"]) {
    if (
      extract[key] &&
      session.data[key] &&
      String(session.data[key]).toLowerCase() !== String(extract[key]).toLowerCase()
    ) {
      if (isUpdate) {
        session.data[key] = extract[key];
        if (key === "correo") session.emailUpdated = true;
        session.conflict = null;
      } else if (!session.conflict) {
        caughtConflict = { field: key, old: session.data[key], new: extract[key] };
      }
    }
  }
  if (caughtConflict && !session.conflict) session.conflict = caughtConflict;

  extractData(fixedMessage, session);

  if (TECH_RE.test(trimmed) && trimmed.includes("?") && session.techQuestions < 2) {
    session.techQuestions += 1;
  }

  const messages = [
    { role: "system", content: buildPrompt(session.data, session) },
    ...session.history.slice(-10),
    { role: "user", content: trimmed },
  ];

  try {
    const response = await openai.responses.create({
      model: DEFAULT_MODEL,
      max_output_tokens: 180,
      temperature: 0.35,
      input: messages,
    });

    const reply = (
      response.output_text ||
      response.output?.find((item) => item.type === "message")?.content?.find((item) => item.type === "output_text")?.text ||
      ""
    ).trim();

    if (!reply) throw new Error("Empty response from OpenAI");

    session.history.push({ role: "user", content: trimmed });
    session.history.push({ role: "assistant", content: reply });

    let leadJustSent = false;
    if (!session.leadSent && isLeadComplete(session.data)) {
      session.leadSent = true;
      leadJustSent = true;
      saveLeadToFile(session.data);
      Promise.all([
        sendLeadEmail(session.data, session.history).catch((error) => console.error("[VHC] lead email:", error.message)),
        sendConfirmationEmail(session.data).catch((error) => console.error("[VHC] confirmation email:", error.message)),
      ]);
    } else if (session.leadSent && session.emailUpdated) {
      session.emailUpdated = false;
      saveLeadToFile(session.data);
      Promise.all([
        sendLeadEmail(session.data, session.history).catch((error) => console.error("[VHC] lead email update:", error.message)),
        sendConfirmationEmail(session.data).catch((error) => console.error("[VHC] confirmation email update:", error.message)),
      ]);
    }

    return res.json({
      reply,
      meta: {
        lang: session.lang,
        tipo: session.data.tipo,
        leadSent: session.leadSent,
        leadJustSent,
        collected: Object.fromEntries(Object.entries(session.data).filter(([, value]) => value !== null)),
      },
    });
  } catch (error) {
    console.error("[VHC] chat error:", error.message);
    return res.status(500).json({ error: "Error processing message. Please try again." });
  }
});

app.get("/health", (_, res) => {
  res.json({
    status: "ok",
    brand: BRAND,
    sessions: sessions.size,
    uptime: `${Math.floor(process.uptime())}s`,
  });
});

app.get("/test-email", async (_, res) => {
  if (!resend) return res.status(500).json({ error: "RESEND_API_KEY is missing" });
  try {
    await resend.emails.send({
      from: `${BRAND} <${DEFAULT_FROM_EMAIL}>`,
      to: DEFAULT_LEAD_EMAIL,
      replyTo: DEFAULT_REPLY_TO_EMAIL,
      subject: `Test email | ${BRAND}`,
      html: `<p>Email delivery is working for ${BRAND}.</p>`,
    });
    res.json({ status: "ok", message: "Email sent" });
  } catch (error) {
    console.error("[VHC] test-email:", error.message);
    res.status(500).json({ error: error.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`VHC chatbot server listening on http://localhost:${PORT}`));

