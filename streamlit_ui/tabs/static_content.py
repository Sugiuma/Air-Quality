import streamlit as st



def show_static_content():
    with st.expander("📌 Executive Overview (Click to Expand/Collapse)", expanded=False):

        key_pollutants = """
            <style>
            .pollutant-table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 1rem;
                font-size: 16px;
            }
            .pollutant-table th, .pollutant-table td {
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }
            .pollutant-table th {
                background-color: #d9eefa;
                color: #333;
            }
            .pollutant-table tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            .pollutant-table tr:hover {
                background-color: #eef9ff;
            }
            </style>

            <table class="pollutant-table">
                <tr>
                    <th>Pollutant</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td><b>PM2.5</b></td>
                    <td>Fine particulate matter ≤2.5 microns; penetrates deep into lungs and bloodstream</td>
                </tr>
                <tr>
                    <td><b>PM10</b></td>
                    <td>Coarse particulate matter ≤10 microns</td>
                </tr>
                <tr>
                    <td><b>NO₂ (Nitrogen Dioxide)</b></td>
                    <td>Produced by vehicles, industry, and fires; affects lungs and contributes to ozone</td>
                </tr>
                <tr>
                    <td><b>CO (Carbon Monoxide)</b></td>
                    <td>Inhibits oxygen delivery in the body; produced by incomplete combustion</td>
                </tr>
                <tr>
                    <td><b>O₃ (Ground-level Ozone)</b></td>
                    <td>Secondary pollutant formed from NOx and VOCs in sunlight</td>
                </tr>
                <tr>
                    <td><b>SO₂ (Sulfur Dioxide)</b></td>
                    <td>From burning fossil fuels and industrial processes</td>
                </tr>
            </table>
            """

        city_table_html = """
            <style>
            .city-table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 1rem;
                font-size: 15px;
            }
            .city-table th, .city-table td {
                border: 1px solid #ccc;
                padding: 10px;
                text-align: left;
            }
            .city-table th {
                background-color: #d9f0ff;
                color: #333;
            }
            .city-table tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            .city-table tr:hover {
                background-color: #e6f7ff;
            }
            </style>

            <table class="city-table">
                <tr>
                    <th>City</th>
                    <th>Category</th>
                    <th>AQI Rank</th>
                    <th>Risk Score</th>
                    <th>Major Issues triggering demand</th>
                </tr>
                <tr><td><b>Delhi</b></td><td>Tier 1</td><td>Very High</td><td>0.91</td><td>Highest AQI in the world at times</td></tr>
                <tr><td><b>Mumbai</b></td><td>Tier 1</td><td>High</td><td>0.45</td><td>Coastal, but construction & traffic</td></tr>
                <tr><td><b>Bengaluru</b></td><td>Tier 1</td><td>Moderate</td><td>0.39</td><td>Tech hub, rising construction dust</td></tr>
                <tr><td><b>Kolkata</b></td><td>Tier 1</td><td>High</td><td>0.30</td><td>Old industries, coal, traffic</td></tr>
                <tr><td><b>Hyderabad</b></td><td>Tier 1</td><td>Moderate</td><td>0.29</td><td>Expanding metro with rising AQI</td></tr>
                <tr><td><b>Chennai</b></td><td>Tier 1</td><td>Moderate</td><td>0.19</td><td>Industrial + vehicular pollution</td></tr>
                <tr><td><b>Ahmedabad</b></td><td>Tier 1</td><td>High</td><td>0.35</td><td>Textile & chemical zones</td></tr>
                <tr><td><b>Pune</b></td><td>Tier 1</td><td>High</td><td>0.30</td><td>Tier-1 for consumer tech & health</td></tr>
                <tr><td><b>Ghaziabad</b></td><td>Tier 2</td><td>High</td><td>0.43</td><td>Road dust, waste burning, traffic</td></tr>
                <tr><td><b>Patna</b></td><td>Tier 2</td><td>High</td><td>0.43</td><td>Brick kilns + traffic</td></tr>
                <tr><td><b>Chandigarh</b><td>Tier 2</td></td><td>High</td><td>0.38</td><td>Seasonal pollution</td></tr>
                <tr><td><b>Meerut</b></td><td>Tier 2</td><td>High</td><td>0.36</td><td>Waste burning</td></tr>
            </table>
            """
        must_have_features_html = """
        <table style="width: 100%; font-size: 15px; color: #333; border-collapse: collapse; border: 1px solid #ccc;">
        <style>
            table.custom-hover tr:hover {
                background-color: #eef9ff;
            }
        </style>
        <thead>
            <tr style="background-color: #d9eefa;">
            <th style="text-align: left; padding: 8px; border: 1px solid #ccc;">Category</th>
            <th style="text-align: left; padding: 8px; border: 1px solid #ccc;">Must-Have Features in <em>our product</em></th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td style="padding: 8px; border: 1px solid #ccc;">Filtration</td>
            <td style="padding: 8px; border: 1px solid #ccc;">
                - Pre-filter + True HEPA H13+<br>
                - Activated Carbon + VOC filter<br>
                - Optional UV/ion (ozone-free)
            </td>
            </tr>
            <tr>
            <td style="padding: 8px; border: 1px solid #ccc;">Performance</td>
            <td style="padding: 8px; border: 1px solid #ccc;">
                - CADR ≥ 400 m³/hr<br>
                - Covers 500+ sq.ft<br>
                - 360° airflow
            </td>
            </tr>
            <tr>
            <td style="padding: 8px; border: 1px solid #ccc;">Smart Features</td>
            <td style="padding: 8px; border: 1px solid #ccc;">
                - Real-time indoor AQI display<br>
                - Outdoor AQI sync via mobile<br>
                - Voice assistant + App control
            </td>
            </tr>
            <tr>
            <td style="padding: 8px; border: 1px solid #ccc;">User Experience</td>
            <td style="padding: 8px; border: 1px solid #ccc;">
                - Whisper quiet sleep mode (&lt;25 dB)<br>
                - Stable Auto mode<br>
                - No lockout even if filter is expired
            </td>
            </tr>
            <tr>
            <td style="padding: 8px; border: 1px solid #ccc;">Reliability</td>
            <td style="padding: 8px; border: 1px solid #ccc;">
                - Power resume after outage<br>
                - Affordable filters (₹1,500–2,000)<br>
                - Filter availability online
            </td>
            </tr>
            <tr>
            <td style="padding: 8px; border: 1px solid #ccc;">Design</td>
            <td style="padding: 8px; border: 1px solid #ccc;">
                - Sleek, portable, child lock, minimal UI
            </td>
            </tr>
        </tbody>
        </table>
        """
        #st.markdown(must_have_features_html, unsafe_allow_html=True)

        filter_types = """
            <style>
                .filter-table {
                    border-collapse: collapse;
                    width: 100%;
                    font-size: 15px;
                }
                .filter-table th, .filter-table td {
                    border: 1px solid #ccc;
                    padding: 10px;
                    text-align: left;
                }
                .filter-table th {
                    background-color: #d9f0ff;  /* Light blue */
                }
                .filter-table td {
                    background-color: #fff;
                }
                .filter-table tr:hover {
                    background-color: #eef9ff;
                }
            </style>

            <table class="filter-table">
                <thead>
                    <tr>
                        <th>Basic Filter Types</th>
                        <th>Targets</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>HEPA (H13/H14)</b></td>
                        <td>PM2.5, PM10, pollen, bacteria, allergens</td>
                    </tr>
                    <tr>
                        <td><b>Activated Carbon</b></td>
                        <td>VOCs, odors, formaldehyde, gases</td>
                    </tr>
                    <tr>
                        <td><b>Pre-filter (mesh)</b></td>
                        <td>Hair, pet fur, coarse dust</td>
                    </tr>
                    <tr>
                        <td style="background-color: #e6f9e6;"><b>🔬 R&D Filters</b></td>
                        <td style="background-color: #e6f9e6;"><b>Targets</b></td>
                    </tr>
                    <tr>
                        <td><b>UV-C Light</b></td>
                        <td>Bacteria, viruses, mold spores</td>
                    </tr>
                    <tr>
                        <td><b>Cold Catalyst / Photocatalyst</b></td>
                        <td>Formaldehyde, VOCs</td>
                    </tr>
                    <tr>
                        <td><b>Ionizer / Plasma Filter</b></td>
                        <td>Fine dust, static pollutants</td>
                    </tr>
                    <tr>
                        <td><b>Humidifying Filters</b></td>
                        <td>Dry air, airborne bacteria</td>
                    </tr>
                </tbody>
            </table>
            """

        air_purifier_segment = """
            <style>
                .segment-table {
                    border-collapse: collapse;
                    width: 100%;
                    font-size: 15px;
                }
                .segment-table th, .segment-table td {
                    border: 1px solid #ccc;
                    padding: 10px;
                    text-align: left;
                }
                .segment-table th {
                    background-color: #d9f0ff;  /* Light blue */
                }
                .segment-table td {
                    background-color: #fff;
                }
            </style>

            <table class="segment-table">
                <thead>
                    <tr>
                        <th>Segment</th>
                        <th>Suggested Features</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><b>Tier 1 Metro Home</b></td>
                        <td>HEPA + Carbon + Auto AQI detection</td>
                    </tr>
                    <tr>
                        <td><b>Tier 2 City Home</b></td>
                        <td>HEPA + Basic Carbon + Pre-filter</td>
                    </tr>
                    <tr>
                        <td><b>Industrial Office/Home</b></td>
                        <td>HEPA H14 + High-grade Carbon + Ionizer or UV-C</td>
                    </tr>
                    <tr>
                        <td><b>Pet Households</b></td>
                        <td>HEPA + Pre-filter (washable) + Carbon + Odor sensors</td>
                    </tr>
                    <tr>
                        <td><b>Children/Elderly Room</b></td>
                        <td>HEPA + UV-C (for hygiene) + Low-noise modes</td>
                    </tr>
                </tbody>
            </table>
            """
        tier_pricing = """
        <table style="width: 100%; border-collapse: collapse; font-size: 16px;">
        <tr style="background-color: #d9f0ff;">
            <th style="padding: 10px; border: 1px solid #ccc;">💰 Tier</th>
            <th style="padding: 10px; border: 1px solid #ccc;">Price Range</th>
            <th style="padding: 10px; border: 1px solid #ccc;">Ideal For</th>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #ccc;">Basic</td>
            <td style="padding: 10px; border: 1px solid #ccc;">₹6,000 - ₹8,000</td>
            <td style="padding: 10px; border: 1px solid #ccc;">Small rooms, budget-conscious users</td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #ccc;">Mid</td>
            <td style="padding: 10px; border: 1px solid #ccc;">₹8,000 - ₹12,000</td>
            <td style="padding: 10px; border: 1px solid #ccc;">Families, tier-2 city homes</td>
        </tr>
        <tr>
            <td style="padding: 10px; border: 1px solid #ccc;">Premium</td>
            <td style="padding: 10px; border: 1px solid #ccc;">₹16,000 and above</td>
            <td style="padding: 10px; border: 1px solid #ccc;">Metro cities, high-pollution zones, elderly/infants</td>
        </tr>
        </table>
        """
        innovation = """
            <style>
            .innovation-table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 1rem;
                font-size: 15px;
            }
            .innovation-table th, .innovation-table td {
                border: 1px solid #ccc;
                padding: 10px;
                text-align: left;
            }
            .innovation-table th {
                background-color: #d0ecff;
                color: #333;
            }
            .innovation-table tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            .innovation-table tr:hover {
                background-color: #eef9ff;
            }
            </style>

            <table class="innovation-table">
                <tr>
                    <th>Area</th>
                    <th>Add-On Ideas</th>
                </tr>
                <tr>
                    <td><b>Health Insights</b></td>
                    <td>Suggest ventilation routines, exposure history, alert during spikes</td>
                </tr>
                <tr>
                    <td><b>Energy Savings</b></td>
                    <td>Smart Eco Mode based on AQI + usage patterns</td>
                </tr>
                <tr>
                    <td><b>Subscription</b></td>
                    <td>Filter subscription service with reminders + doorstep delivery</td>
                </tr>
                <tr>
                    <td><b>Modularity</b></td>
                    <td>Swappable filter packs: e.g., "Smoke", "Pet", "Dust" modes</td>
                </tr>
            </table>
            """
        launch = """
        <style>
        .air-table {
            border-collapse: collapse;
            width: 100%;
            font-family: Arial, sans-serif;
            font-size: 15px;
        }
        .air-table th, .air-table td {
            border: 1px solid #ccc;
            padding: 10px;
            vertical-align: top;
            text-align: left;
        }
        .air-table th {
            background-color: #d0ecff;
            font-weight: bold;
        }
        .air-table tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        </style>

        <table class="air-table">
            <thead>
                <tr>
                    <th>Seasonal Triggers & AQI Trends</th>
                    <th>Brand Sales Trends</th>
                    <th>Opportunity for Launch</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>Late Sep:</b> Pre-Diwali awareness ads, AQI starts rising</td>
                    <td>Slight uptick (prep phase)</td>
                    <td>🔶 Build-up campaigns start</td>
                </tr>
                <tr>
                    <td><b>Oct (Full):</b> Stubble burning begins, AQI 200–300+</td>
                    <td>30–40% spike (esp. in metros)</td>
                    <td>✅ Product launch window begins</td>
                </tr>
                <tr>
                    <td><b>Oct End–Nov Mid:</b> Diwali + peak pollution, AQI > 300 (Hazardous)</td>
                    <td>Up to 10x metro sales, 50%+ national surge</td>
                    <td>✅✅ High-impact launch phase</td>
                </tr>
                <tr>
                    <td><b>Nov End–Dec:</b> Winter smog, prolonged AQI > 300</td>
                    <td>200% QoQ rise for select models (Dyson, Philips)</td>
                    <td>✅ Continue ads + bundle offers</td>
                </tr>
                <tr>
                    <td><b>Jan:</b> Cold weather, AQI 150–250</td>
                    <td>Moderate sales (filters, accessories)</td>
                    <td>🔶 Post-launch remarketing</td>
                </tr>
                <tr>
                    <td><b>Feb–Mar:</b> AQI drops below 150, warmer climate</td>
                    <td>Decline in demand</td>
                    <td>🔴 Avoid major campaigns</td>
                </tr>
                <tr>
                    <td><b>Apr–Jun:</b> Summer season, AQI improves</td>
                    <td>Flat sales, very niche use cases</td>
                    <td>🔴 Not suitable for launch</td>
                </tr>
                <tr>
                    <td><b>Jul–Aug:</b> Monsoon, AQI low</td>
                    <td>Low purifier sales, minor niche (dehumidifiers)</td>
                    <td>🔴 Low relevance</td>
                </tr>
            </tbody>
        </table>
        """

        def custom_summary_card(title, value, icon="📌", text_color="#444"):
            st.markdown(
                f"""
                <div style="
                    border: 1px solid #ccc;
                    border-radius: 10px;
                    padding: 15px;
                    margin-bottom: 15px;
                    background-color: #fff;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
                    min-height: 80px;
                ">
                    <div style="font-weight: 600; font-size: 17px; margin-bottom: 5px;">{icon} {title}</div>
                    <div style="font-size: 16px; color: {text_color};">{value}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
        col1, col2, col3 = st.columns([2,2,2])
        with col1:
            custom_summary_card("1. Target Pollutants & Particles", key_pollutants, icon="🧪")

        with col2:
            custom_summary_card("2. Must-Have Features", must_have_features_html, icon="🛠️")
            
        with col3:
            custom_summary_card("2a. Tiered Pricing Models", tier_pricing, icon="💰")
            
        col4, col5 = st.columns([2,2])
        with col4:
            custom_summary_card("3. Market Demand - Target Cities to launch", city_table_html, icon="🌆")

        with col5:
            custom_summary_card("3a. Market Demand - Time to launch", launch, icon="🚀")
        col6, col7,col8 = st.columns([2,2,2])
        with col6:
            custom_summary_card("4. Aligning R&D with filter types", filter_types, icon="🧪")

        with col7:
            custom_summary_card("4a. Aligning R&D with localized patterns", air_purifier_segment, icon="👥")

        with col8:
            custom_summary_card("4b. Aligning R&D with innovation", innovation, icon="👥")