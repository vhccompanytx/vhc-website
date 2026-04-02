
new_block = r"""            <!-- Project Cards Grid -->
            <div id="pfGrid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:1.5rem;">

                <!-- 0: The Grande -->
                <div class="pf-card" data-cat="solar" onclick="pfOpen(0)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 10.41.51 PM.jpeg" alt="The Grande" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Sugar Land, TX &middot; Full Roof Solar</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">The Grande</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">Aerial dual-array installation. 48 premium panels across a large residential property.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">18.2 kW</div><div style="font-size:.7rem;color:var(--vhc-gray);">System Size</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">2</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photos</div></div>
                        </div>
                    </div>
                </div>

                <!-- 1: Texas Residential Solar -->
                <div class="pf-card" data-cat="solar" onclick="pfOpen(1)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 11.06.44 PM.jpeg" alt="Texas residential solar at sunset" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Houston Area, TX &middot; Full Roof Solar</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">Texas Residential Solar</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">Full-roof installs across the Houston area — aerial drone shots and sunset photography.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">8&#8211;22 kW</div><div style="font-size:.7rem;color:var(--vhc-gray);">Range</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">6</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photos</div></div>
                        </div>
                    </div>
                </div>

                <!-- 2: Katy Enphase IQ Exterior -->
                <div class="pf-card" data-cat="enphase" onclick="pfOpen(2)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 10.44.13 PM.jpeg" alt="Enphase IQ exterior" style="width:100%;height:100%;object-fit:cover;object-position:center top;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Katy, TX &middot; Enphase Storage</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">Katy Enphase IQ &#8212; Exterior</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">Exterior-mounted Enphase IQ Battery 5P units with dual inverter integration on a brick home.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">Enphase IQ5P</div><div style="font-size:.7rem;color:var(--vhc-gray);">Battery</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">3</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photos</div></div>
                        </div>
                    </div>
                </div>

                <!-- 3: Enphase IQ Garage -->
                <div class="pf-card" data-cat="enphase" onclick="pfOpen(3)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 11.13.27 PM.jpeg" alt="Enphase IQ batteries in garage" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">The Woodlands, TX &middot; Enphase Storage</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">Enphase IQ 10T &#8212; Garage Install</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">Indoor garage installation of 3 Enphase IQ Battery 10T units on a clean white ledge.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">Enphase IQ10T</div><div style="font-size:.7rem;color:var(--vhc-gray);">Model</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">4</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photos</div></div>
                        </div>
                    </div>
                </div>

                <!-- 4: NeoVolta White Siding -->
                <div class="pf-card" data-cat="neovolta" onclick="pfOpen(4)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 11.01.45 PM.jpeg" alt="NeoVolta white siding house" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Houston, TX &middot; NeoVolta Storage</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">NeoVolta &#8212; White Siding Home</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">3-unit NeoVolta battery system with inverter on white vinyl siding. Solar + storage combo.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">3&#215;NeoVolta</div><div style="font-size:.7rem;color:var(--vhc-gray);">Batteries</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">2</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photos</div></div>
                        </div>
                    </div>
                </div>

                <!-- 5: NeoVolta Brick Home -->
                <div class="pf-card" data-cat="neovolta" onclick="pfOpen(5)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 11.04.53 PM.jpeg" alt="NeoVolta brick home" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Katy, TX &middot; NeoVolta Storage</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">NeoVolta &#8212; Brick Home</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">Dual NeoVolta inverter setup with 4 storage units on a light brick exterior. Clean panel install on roof.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">2&#215;Inverter</div><div style="font-size:.7rem;color:var(--vhc-gray);">NeoVolta</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">2</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photos</div></div>
                        </div>
                    </div>
                </div>

                <!-- 6: NeoVolta Blue Siding -->
                <div class="pf-card" data-cat="neovolta" onclick="pfOpen(6)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 11.08.06 PM.jpeg" alt="NeoVolta blue siding" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Sugar Land, TX &middot; NeoVolta Storage</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">NeoVolta &#8212; Blue Siding Home</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">Single NeoVolta inverter with 3-unit battery bank on blue siding home. Full roof solar + storage.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">3&#215;NeoVolta</div><div style="font-size:.7rem;color:var(--vhc-gray);">Batteries</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">3</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photos</div></div>
                        </div>
                    </div>
                </div>

                <!-- 7: NeoVolta Powerhouse Gray Barn -->
                <div class="pf-card" data-cat="neovolta" onclick="pfOpen(7)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 11.05.55 PM.jpeg" alt="NeoVolta Powerhouse" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Houston, TX &middot; NeoVolta Storage</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">NeoVolta Powerhouse</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">4-unit NeoVolta battery bank with dual inverters on gray panel exterior &#8212; the largest system in our portfolio.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">40 kWh</div><div style="font-size:.7rem;color:var(--vhc-gray);">Capacity</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">2</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photos</div></div>
                        </div>
                    </div>
                </div>

                <!-- 8: Tesla Red Metal + EV -->
                <div class="pf-card" data-cat="tesla" onclick="pfOpen(8)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 11.12.55 PM.jpeg" alt="Tesla Powerwall red metal home" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Austin, TX &middot; Tesla Powerwall</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">Tesla Powerwall &#8212; Metal Home + EV</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">Dual Tesla Powerwall with Level 2 EV charger on red corrugated metal home. Premium clean conduit work.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">27 kWh</div><div style="font-size:.7rem;color:var(--vhc-gray);">Storage</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">2</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photos</div></div>
                        </div>
                    </div>
                </div>

                <!-- 9: Tesla Brick Home -->
                <div class="pf-card" data-cat="tesla" onclick="pfOpen(9)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 11.12.11 PM.jpeg" alt="Tesla Powerwall brick home" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-gold);color:var(--vhc-navy-deep);font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">Completed</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Houston, TX &middot; Tesla Powerwall</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">Tesla Powerwall &#8212; Brick Home</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">Single Tesla Powerwall on red brick exterior, paired with a Carrier HVAC system upgrade.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">13.5 kWh</div><div style="font-size:.7rem;color:var(--vhc-gray);">Storage</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">1</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photo</div></div>
                        </div>
                    </div>
                </div>

                <!-- 10: Tesla Pool House -->
                <div class="pf-card" data-cat="tesla" onclick="pfOpen(10)" style="cursor:pointer;background:#fff;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,0.08);transition:transform .3s,box-shadow .3s;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 12px 36px rgba(0,0,0,0.14)'" onmouseout="this.style.transform='';this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'">
                    <div style="height:220px;overflow:hidden;position:relative;">
                        <img src="brand/WhatsApp Image 2026-03-31 at 11.11.21 PM.jpeg" alt="Tesla pool house" style="width:100%;height:100%;object-fit:cover;transition:transform .4s;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform=''">
                        <span style="position:absolute;top:.75rem;right:.75rem;background:var(--vhc-navy);color:#fff;font-size:.7rem;font-weight:700;padding:.25rem .75rem;border-radius:2rem;text-transform:uppercase;letter-spacing:.05em;">More Photos Soon</span>
                    </div>
                    <div style="padding:1.25rem 1.5rem;">
                        <div style="font-size:.75rem;color:var(--vhc-gold);text-transform:uppercase;letter-spacing:.1em;font-weight:600;margin-bottom:.25rem;">Houston, TX &middot; Tesla Powerwall</div>
                        <h3 style="font-family:var(--font-display);font-size:1.15rem;color:var(--vhc-navy-deep);margin:0 0 .5rem;">Tesla Powerwall &#8212; Pool House</h3>
                        <p style="font-size:.875rem;color:var(--vhc-gray);margin:0 0 1rem;line-height:1.5;">Tesla Powerwall install on green siding home with poolside access. More photos coming soon.</p>
                        <div style="display:flex;gap:1rem;">
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">13.5 kWh</div><div style="font-size:.7rem;color:var(--vhc-gray);">Storage</div></div>
                            <div style="text-align:center;"><div style="font-weight:700;color:var(--vhc-navy-deep);font-size:1rem;">1</div><div style="font-size:.7rem;color:var(--vhc-gray);">Photo</div></div>
                        </div>
                    </div>
                </div>

            </div><!-- /pfGrid -->
        </div>
    </section>

    <!-- LIGHTBOX -->
    <div id="pfLightbox" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.92);z-index:9999;flex-direction:column;align-items:center;justify-content:center;" onclick="pfLBClose(event)">
        <button onclick="document.getElementById('pfLightbox').style.display='none'" style="position:absolute;top:1.25rem;right:1.25rem;background:rgba(255,255,255,0.1);border:none;color:#fff;width:44px;height:44px;border-radius:50%;font-size:1.5rem;cursor:pointer;z-index:10;" aria-label="Close">&times;</button>
        <button onclick="pfLBNav(-1);event.stopPropagation();" style="position:absolute;left:1.25rem;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.12);border:none;color:#fff;width:48px;height:48px;border-radius:50%;font-size:1.5rem;cursor:pointer;z-index:10;" aria-label="Prev">&#8592;</button>
        <button onclick="pfLBNav(1);event.stopPropagation();" style="position:absolute;right:1.25rem;top:50%;transform:translateY(-50%);background:rgba(255,255,255,0.12);border:none;color:#fff;width:48px;height:48px;border-radius:50%;font-size:1.5rem;cursor:pointer;z-index:10;" aria-label="Next">&#8594;</button>
        <img id="pfLBImg" src="" alt="" style="max-width:90vw;max-height:80vh;object-fit:contain;border-radius:12px;box-shadow:0 8px 48px rgba(0,0,0,0.5);">
        <div id="pfLBCaption" style="color:#fff;margin-top:1rem;font-family:var(--font-display);font-size:1rem;text-align:center;max-width:600px;padding:0 1rem;"></div>
        <div id="pfLBCounter" style="color:rgba(255,255,255,0.5);font-size:.8rem;margin-top:.4rem;"></div>
    </div>

    <script>
    var pfProjects = [
        {name:'The Grande',loc:'Sugar Land, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 10.41.51 PM.jpeg',cap:'Aerial view of dual-array 48-panel solar installation'},
            {src:'brand/WhatsApp Image 2026-03-31 at 10.42.06 PM.jpeg',cap:'Second aerial angle — The Grande full roof'}
        ]},
        {name:'Texas Residential Solar',loc:'Houston Area, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 11.06.44 PM.jpeg',cap:'Full panel array at golden sunset — gray shingle roof'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.05.28 PM.jpeg',cap:'Close-up panel row on brown shingle roof'},
            {src:'brand/WhatsApp Image 2026-03-31 at 10.46.20 PM.jpeg',cap:'Aerial drone view — full residential roof layout'},
            {src:'brand/WhatsApp Image 2026-03-31 at 10.48.33 PM.jpeg',cap:'Ground-level view of panel array'},
            {src:'brand/WhatsApp Image 2026-03-31 at 10.48.53 PM.jpeg',cap:'Close-up of panel mounting hardware'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.09.52 PM.jpeg',cap:'Solar panel installation — sunset backyard view'}
        ]},
        {name:'Katy Enphase IQ — Exterior',loc:'Katy, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 10.44.13 PM.jpeg',cap:'Enphase IQ Battery 5P — exterior wall mount'},
            {src:'brand/WhatsApp Image 2026-03-31 at 10.44.21 PM.jpeg',cap:'Side angle — Enphase install with pool visible'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.02.16 PM.jpeg',cap:'Dual Enphase inverters on brick wall — full electrical panel view'}
        ]},
        {name:'Enphase IQ 10T — Garage',loc:'The Woodlands, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 11.13.27 PM.jpeg',cap:'Three Enphase IQ 10T units on white garage ledge'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.13.35 PM.jpeg',cap:'Enphase IQ 10T front view — garage install'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.13.47 PM.jpeg',cap:'Enphase IQ battery trio — angled profile'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.14.00 PM.jpeg',cap:'Full Enphase IQ garage installation — IQ8 inverter visible'}
        ]},
        {name:'NeoVolta — White Siding Home',loc:'Houston, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 11.01.45 PM.jpeg',cap:'3x NeoVolta batteries + inverter + Enphase solar combiner — white vinyl siding'},
            {src:'brand/WhatsApp Image 2026-03-31 at 10.50.36 PM.jpeg',cap:'Roof panel view — white siding home'}
        ]},
        {name:'NeoVolta — Brick Home',loc:'Katy, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 11.04.53 PM.jpeg',cap:'Dual NeoVolta inverters + 4 storage units on light brick wall'},
            {src:'brand/WhatsApp Image 2026-03-31 at 10.42.35 PM.jpeg',cap:'Solar panel rooftop view — brick home'}
        ]},
        {name:'NeoVolta — Blue Siding Home',loc:'Sugar Land, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 11.08.06 PM.jpeg',cap:'Single NeoVolta inverter + 3-unit battery bank on blue siding'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.05.37 PM.jpeg',cap:'NeoVolta battery row — front view, blue siding home'},
            {src:'brand/WhatsApp Image 2026-03-31 at 10.56.29 PM.jpeg',cap:'Aerial solar view — blue siding home rooftop'}
        ]},
        {name:'NeoVolta Powerhouse',loc:'Houston, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 11.05.55 PM.jpeg',cap:'4x NeoVolta batteries + dual NeoVolta inverters — gray panel exterior'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.09.21 PM.jpeg',cap:'Full powerhouse system rear angle — gray barn siding'}
        ]},
        {name:'Tesla Powerwall — Metal Home + EV',loc:'Austin, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 11.12.55 PM.jpeg',cap:'Dual Tesla Powerwall (T logo) + Level 2 EV charger — red corrugated metal'},
            {src:'brand/WhatsApp Image 2026-03-31 at 11.11.42 PM.jpeg',cap:'Tesla Powerwall prep — cream siding, construction phase'}
        ]},
        {name:'Tesla Powerwall — Brick Home',loc:'Houston, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 11.12.11 PM.jpeg',cap:'Tesla Powerwall on red brick exterior + Carrier HVAC'}
        ]},
        {name:'Tesla Powerwall — Pool House',loc:'Houston, TX',photos:[
            {src:'brand/WhatsApp Image 2026-03-31 at 11.11.21 PM.jpeg',cap:'Tesla Powerwall install — green siding home with pool access'}
        ]}
    ];
    var pfLBCur=0,pfLBProject=0;
    function pfOpen(idx){pfLBProject=idx;pfLBCur=0;pfLBShow();document.getElementById('pfLightbox').style.display='flex';}
    function pfLBShow(){var p=pfProjects[pfLBProject];var ph=p.photos[pfLBCur];document.getElementById('pfLBImg').src=ph.src;document.getElementById('pfLBImg').alt=ph.cap;document.getElementById('pfLBCaption').textContent=p.name+' \u00b7 '+p.loc;document.getElementById('pfLBCounter').textContent=(pfLBCur+1)+' / '+p.photos.length;}
    function pfLBNav(d){var p=pfProjects[pfLBProject];pfLBCur=(pfLBCur+d+p.photos.length)%p.photos.length;pfLBShow();}
    function pfLBClose(e){if(e.target===document.getElementById('pfLightbox'))document.getElementById('pfLightbox').style.display='none';}
    document.addEventListener('keydown',function(e){var lb=document.getElementById('pfLightbox');if(lb.style.display==='flex'){if(e.key==='ArrowRight')pfLBNav(1);if(e.key==='ArrowLeft')pfLBNav(-1);if(e.key==='Escape')lb.style.display='none';}});
    function pfFilter(btn,cat){
        document.querySelectorAll('.pf-tab').forEach(function(b){b.style.background='transparent';b.style.color='var(--vhc-navy)';});
        btn.style.background='var(--vhc-navy)';btn.style.color='#fff';
        document.querySelectorAll('.pf-card').forEach(function(c){c.style.display=(cat==='all'||c.dataset.cat===cat)?'block':'none';});
    }
    </script>"""

with open('frontend/portfolio.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '            <!-- Project Cards Grid -->'
end_marker = '    </script>\n\n    <!-- Footer'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print('ERROR: markers not found')
else:
    new_content = content[:start_idx] + new_block + '\n\n    <!-- Footer' + content[end_idx + len('    </script>\n\n    <!-- Footer'):]
    with open('frontend/portfolio.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('SUCCESS: portfolio.html updated')
    print('New size:', len(new_content))
