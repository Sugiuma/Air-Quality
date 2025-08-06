import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
from tabs.static_content import show_static_content

# --- Page config ---
st.set_page_config(layout="wide")
st.header("AirPure Innovations")
st.markdown("### Air Purifier Market Prioritization Dashboard")

# Show static part
show_static_content()

# Load datasets
df = pd.read_csv("data/merged_city_data.csv")
df["City"] = df["City"].str.title()

df1 = pd.read_csv("data/citywise_trend.csv")
df1["month"] = pd.to_datetime(df1["month"])
df1["year"] = df1["month"].dt.year
df1["month_name"] = df1["month"].dt.strftime('%b')
df1["month_num"] = df1["month"].dt.month


# Inject custom CSS for chart containers
st.markdown("""
<style>
div[data-testid="stPlotlyChart"] {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 20px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 All cities Overview", "📈 Target Cities to Launch", "🧪 Predictive Analysis - City specific Simulation"])


# -------------------- TAB 1: Overview --------------------
with tab1:
    

    # -------------------------------
    # Load Datasets
    # -------------------------------
    df2 = pd.read_csv("data/city_pollutants_aqi_summary.csv")
    df2["City"] = df2["City"].str.title()

    df3 = pd.read_csv("data/all_citywise_trend.csv")
    df3["month"] = pd.to_datetime(df3["month"])
    df3["year"] = df3["month"].dt.year
    df3["month_name"] = df3["month"].dt.strftime('%b')
    df3["month_num"] = df3["month"].dt.month
    df3["area"] = df3["area"].str.title()
    df3["state"] = df3["state"].str.title()

    df_state_avg = pd.read_csv("data/state_avg.csv")
    df_state_avg["state"] = df_state_avg["state"].str.title()

    df_disease = pd.read_csv("data/top2_diseases_per_state_with_aqi.csv")
    df_disease["State"] = df_disease["State"].str.title()

    df_ev = pd.read_csv("data/ev.csv")
    df_ev["State"] = df_ev["State"].str.title()

    

    # -------------------------------
    # Merge state info from df3 → df2
    # -------------------------------
    city_state_map = df3[["area", "state"]].drop_duplicates().rename(columns={"area": "City"})
    df2 = df2.merge(city_state_map, on="City", how="left")

    # -------------------------------
    # Top-Level State & City Selector
    # -------------------------------
    st.markdown("### Air Quality Dashboard")
    st.markdown("Select a state and city")

    state_list = sorted(df2["state"].dropna().unique())
    selected_state = st.selectbox("Select State", state_list)

    city_list = sorted(df2[df2["state"] == selected_state]["City"].unique())
    selected_city = st.selectbox("Select City", city_list, key="city_selector_top")

    # -------------------------------
    # Filter City & State Data
    # -------------------------------
    city_data = df2[df2["City"] == selected_city].iloc[0]
    city_df = df2[df2["City"] == selected_city]

    monthly_df = df3[df3["area"] == selected_city].copy().sort_values(by=["year", "month_num"])

    ev_row = df_ev[df_ev["State"] == selected_state]

    if not ev_row.empty:
        total_vehicles = ev_row["Total_Vehicles"].values[0]
        ev_vehicles = ev_row["EV_Vehicles"].values[0]
        ev_adoption_pct = (ev_vehicles / total_vehicles) * 100
        ev_info = (
            f"🚗Total Vehicles: {total_vehicles:,}"
            f"   🔋Total EVs: {ev_vehicles:,}<br>"
            f"⚡ EV Adoption Rate: {ev_adoption_pct:.1f}%"
        )
    # -------------------------------
    # KPI Card Utility
    # -------------------------------
    def custom_kpi_card(title, value, icon="", value_color="#444"):
        st.markdown(
            f"""
            <div style="
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 12px;
                margin-bottom: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                background-color: #fff;
            ">
                <div style="font-weight: 700; font-size: 17px;">{icon} {title}</div>
                <div style="font-size: 20px; color: {value_color}; margin-top: 5px;">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # -------------------------------
    # KPIs
    # -------------------------------
    st.markdown(f"Overview of: {selected_city}, {selected_state}")

    kpi1, kpi2,kpi3 = st.columns(3)
    with kpi1:
        custom_kpi_card("City Avg AQI (2022–2025)", f"{city_data['avg_aqi_2022_2025']:.1f}", icon="📊")

    with kpi2:
        custom_kpi_card("State", selected_state, icon="🏷️")
    
    with kpi3:
    # State Avg AQI
        state_avg_row = df_state_avg[df_state_avg["state"] == selected_state]
        if not state_avg_row.empty:
            state_avg_aqi = state_avg_row["aqi_value"].values[0]
            custom_kpi_card("State Avg AQI", f"{state_avg_aqi:.1f}", icon="🌐")

    #with kpi4:
        # Top 2 diseases in state
    top2_diseases = df_disease[(df_disease["State"] == selected_state) & (df_disease["Rank"] <= 2)]

    # Combine disease names and cases using HTML line breaks
    disease_info = "<br>".join(
        [f"☣️{row['Disease']}📋 {row['Cases']} cases" for _, row in top2_diseases.iterrows()]
    )

    # Show in a single KPI card
    kpi4, kpi5 = st.columns([2,3])

    with kpi4:
        custom_kpi_card("Top 2 Diseases of the State", disease_info, icon="🦠")

    with kpi5:
        custom_kpi_card("EV Adoption Stats", ev_info, icon="🚘")


    # -------------------------------
    # Pollutant Composition Pie Chart
    # -------------------------------
    names, values = [], []
    for entry in city_df["pollutants"]:
        if "(" in entry and ")" in entry:
            try:
                name = entry.split("(")[0].strip()
                count = int(entry.split("(")[1].replace(")", "").strip())
                names.append(name)
                values.append(count)
            except:
                continue

    status_cols = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe']
    status_data = {status: city_data.get(status, 0) for status in status_cols}

    # -------------------------------
    # Chart Styling
    # -------------------------------
    st.markdown("""
    <style>
    div[data-testid="stPlotlyChart"] {
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 20px;
        box-sizing: border-box;
        background-color: #fff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # -------------------------------
    # Charts
    # -------------------------------
    charts_col1, charts_col2 = st.columns(2)

    # Pie Chart: Pollutants
    with charts_col1:
        st.markdown("##### ☁️ Pollutant Composition")
        if names and values:
            fig_pie = px.pie(names=names, values=values, hole=0.4)
            fig_pie.update_traces(textinfo='label+percent', textposition='inside')
            st.plotly_chart(fig_pie, use_container_width=False)
        else:
            st.write("No pollutant breakdown available.")

    # Bar Chart: AQI Status Distribution
    with charts_col2:
        st.markdown("##### 🧭 AQI Status Distribution")
        fig_bar = px.bar(
            x=list(status_data.keys()),
            y=list(status_data.values()),
            labels={"x": "Status", "y": "Count"},
            color=list(status_data.values()),
            color_continuous_scale="Reds"
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    # Line Chart: Monthly AQI Trend
    st.markdown("##### 📈 AQI Monthly Trend")
    fig_line = px.line(
        monthly_df,
        x="month_name",
        y="aqi_value",
        color="year",
        markers=True,
        labels={"month_name": "Month", "aqi_value": "AQI"},
        title="Monthly AQI Trends by Year"
    )
    fig_line.update_traces(line=dict(width=2))
    fig_line.update_layout(
        xaxis=dict(categoryorder="array", categoryarray=[
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ])
    )
    st.plotly_chart(fig_line, use_container_width=True)



# -------------------- TAB 2: Overview --------------------
with tab2:
    composite_df = pd.read_csv("data/composite_score.csv")

    # Rename problematic column
    composite_df.rename(columns={"AQI_Rank*": "AQI_Rank"}, inplace=True)

    # Merge composite data
    df = df.merge(
        composite_df[["City", "AQI_Rank", "Composite_Score"]],
        on="City",
        how="left"
    )

    # UI
    st.markdown("### Select a city for detailed overview")
    city_list = sorted(df["City"].unique())
    selected_city = st.selectbox("Select City", city_list, key="tab1_city")

    # Filter selected city data
    city_data = df[df["City"] == selected_city].iloc[0]

    st.markdown(f"#### Overview: {selected_city}")

    # Custom KPI card
    def custom_kpi_card(title, value, icon="", value_color="#444"):
        st.markdown(
            f"""
            <div style="
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 12px;
                margin-bottom: 20px;
                background-color: #fff;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            ">
                <div style="font-weight: 700; font-size: 17px;">{icon} {title}</div>
                <div style="font-size: 20px; color: {value_color}; margin-top: 5px;">{value}</div>
            </div>
            """, unsafe_allow_html=True
        )

    # First row (3 KPIs)
    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        custom_kpi_card("City Avg AQI (2022–2025)", f"{city_data['avg_aqi_2022_2025']:.1f}", "📊")
    with kpi2:
        custom_kpi_card("City Population (2025)", f"{int(city_data['population']):,}", "👥")
    with kpi3:
        custom_kpi_card("City Per Capita Income (INR)", f"{int(city_data['per_capita_income']):,}", "💰")

    # Second row (3 KPIs)
    kpi4, kpi5, kpi6 = st.columns(3)
    with kpi4:
        custom_kpi_card("City Category", city_data["category"], "🏷️")
    with kpi5:
        custom_kpi_card("City AQI Rank", city_data["AQI_Rank"], "🥇")
    with kpi6:
        custom_kpi_card("City Risk Score", f"{city_data['Composite_Score']:.2f}", "📈")

    # Pollutant pie chart
    names, values = [], []
    for entry in city_df["pollutants"]:
        if "(" in entry and ")" in entry:
            try:
                name = entry.split("(")[0].strip()
                count = int(entry.split("(")[1].replace(")", "").strip())
                names.append(name)
                values.append(count)
            except:
                continue

    status_cols = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe']
    status_data = {status: city_data.get(status, 0) for status in status_cols}

    monthly_df = df1[df1["area"] == selected_city].sort_values(by=["year", "month_num"])

    chart1, chart2 = st.columns(2)

    with chart1:
        st.markdown("##### ☁️ Pollutant Composition")
        if names and values:
            fig1 = px.pie(names=names, values=values, hole=0.4)
            fig1.update_traces(textinfo='label+percent')
            st.plotly_chart(fig1,key='tab2-pie', use_container_width=True)
        else:
            st.write("No pollutant breakdown available.")

    with chart2:
        st.markdown("##### 🧭 AQI Status Distribution")
        fig2 = px.bar(x=list(status_data.keys()), y=list(status_data.values()),
                     labels={"x": "Status", "y": "Count"},
                     color=list(status_data.values()),
                     color_continuous_scale="Reds")
        st.plotly_chart(fig2,key='tab2-bar', use_container_width=True)

    
    st.markdown("##### 📈 Monthly AQI Trend")
    fig3 = px.line(monthly_df, x="month_name", y="aqi_value", color="year", markers=True)
    fig3.update_layout(
        xaxis=dict(categoryorder="array", categoryarray=[
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ])
    )
    st.plotly_chart(fig3, key='tab2-line',use_container_width=True)

# -------------------- TAB 3: Simulation --------------------
with tab3:
 
    # 🔹 Load and prepare data
    @st.cache_data
    def load_data():
        df = pd.read_csv("data/citywise_trend.csv")  # Must contain: area, month, aqi_value
        df.rename(columns={"area": "City", "month": "Month", "aqi_value": "AQI"}, inplace=True)
        return df

    df_raw = load_data()
    
    st.subheader("📊 Market Rule Configuration")
    city_options = df_raw["City"].unique().tolist()
    selected_city = st.selectbox("Select City", city_options)
    

    st.markdown(f"### Adjust Rules for **{selected_city}**")

    # Use columns to organize sliders
    col1, col2, col3 = st.columns(3)

    with col1:
        base = st.slider("Base Demand", 100, 2000, 1000)

    with col2:
        threshold = st.slider("AQI Threshold", 100, 400, 300)

    with col3:
        multiplier = st.slider("AQI Spike Multiplier", 1.0, 3.0, 2.0)

    # Row below for seasonal boost
    col4, _ = st.columns([1, 2])
    with col4:
        boost = st.slider("Seasonal Boost (%)", 0.0, 0.5, 0.2)

    
    season = [10, 11]  # Oct & Nov

    # Filter for selected city
    city_df = df_raw[df_raw["City"] == selected_city].copy()

    # ✅ Prophet-compatible df
    city_df["ds"] = pd.to_datetime(city_df["Month"], format="%Y-%m")
    city_df["y"] = city_df["AQI"]

    # 🔮 Prophet model
    m = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    m.fit(city_df[["ds", "y"]])

    # Forecast 12 months ahead
    future = m.make_future_dataframe(periods=12, freq="MS")
    forecast = m.predict(future)

    # 📈 Prepare AQI forecast DataFrame
    aqi_forecast = forecast[["ds", "yhat"]].copy()
    aqi_forecast["Month"] = aqi_forecast["ds"].dt.month
    aqi_forecast["Year"] = aqi_forecast["ds"].dt.year
    aqi_forecast["City"] = selected_city
    aqi_forecast.rename(columns={"yhat": "AQI"}, inplace=True)
    aqi_forecast = aqi_forecast[["City", "Year", "Month", "AQI", "ds"]]

    # 🔢 Dynamic demand calculation based on slider values
    def predict_demand(row):
        demand = base
        if row["AQI"] > threshold:
            demand *= multiplier
        if row["Month"] in season:
            demand *= (1 + boost)
        return int(demand)

    #st.write(aqi_forecast[["ds", "AQI"]].tail(12))

    # Recalculate demand after every slider interaction
    aqi_forecast["Predicted Demand"] = aqi_forecast.apply(predict_demand, axis=1)

    #st.write(f"Base: {base}, Threshold: {threshold}, Multiplier: {multiplier}, Boost: {boost}")

    # 🧮 Split actual vs forecasted
    cutoff = city_df["ds"].max()
    actual = aqi_forecast[aqi_forecast["ds"] <= cutoff]
    forecasted = aqi_forecast[aqi_forecast["ds"] > cutoff]

    # 📊 Plot
    with st.container():
        st.markdown("<div class='box'><h4>📈 AQI Forecast vs Predicted Demand</h4>", unsafe_allow_html=True)

        fig = px.line(
            aqi_forecast,
            x="ds",
            y=["AQI", "Predicted Demand"],
            markers=True,
            labels={"ds": "Date", "value": "Value", "variable": "Metric"},
            title=f"AQI & Demand Forecast for {selected_city}"
        )
        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="AQI / Demand",
            xaxis=dict(tickformat="%b\n%Y"),
            height=450
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # 📉 Prophet Cross Validation
    # with st.container():
    #     st.markdown("### 🔁 Model Performance (Cross-Validation Metrics)")

    #     try:
    #         df_cv = cross_validation(
    #             m,
    #             horizon="180 days",
    #             period="90 days",
    #             initial="730 days"
    #         )
    #         df_p = performance_metrics(df_cv)

    #         st.dataframe(df_p[["horizon", "mae", "mse", "rmse"]])
    #     except Exception as e:
    #         st.warning(f"Cross-validation failed: {e}")

    # 🧼 Filter Recommendations Based on AQI Forecast
    with st.container():
        #st.markdown("<div class='box'><h4>🧼 Filter Recommendations</h4>", unsafe_allow_html=True)

        # 1. Get forecasted AQI values (after the last known date)
        forecasted_aqi = aqi_forecast[aqi_forecast["ds"] > city_df["ds"].max()]
        
        # 2. Calculate average or max AQI in the projected period
        avg_aqi = forecasted_aqi["AQI"].mean()
        max_aqi = forecasted_aqi["AQI"].max()

        # 3. Determine filters based on AQI severity
        if max_aqi <= 100:
            filters = ["HEPA"]
            level = "Good"
        elif max_aqi <= 200:
            filters = ["HEPA", "Activated Carbon"]
            level = "Moderate"
        elif max_aqi <= 300:
            filters = ["HEPA", "Activated Carbon", "UV"]
            level = "Poor"
        elif max_aqi <= 400:
            filters = ["HEPA", "Activated Carbon", "UV", "Pre-filter"]
            level = "Very Poor"
        else:
            filters = ["HEPA", "Activated Carbon", "UV", "Pre-filter", "Ozone Filter"]
            level = "Severe"

        # 4. Display
        # 1. Prepare dynamic HTML using f-string
        html_content = f"""
            <div style="
                border: 2px solid #ddd;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 20px;
            ">
                <h4 style="color:#007acc;">🛡️ Filter Recommendations</h4>
                <p><b>Projected AQI Level:</b> {level} ({max_aqi:.0f})</p>
                <p><b>Recommended Filters:</b></p>
                <ul>
                    {''.join(f'<li>✅ {f}</li>' for f in filters)}
                </ul>
            </div>
        """

        # 2. Render the HTML
        st.markdown(html_content, unsafe_allow_html=True)


    # Footer
    st.markdown("<hr><center><sub>Forecast generated using Facebook Prophet. Adjust rules and explore seasonality impacts on purifier demand.</sub></center>", unsafe_allow_html=True)


# Footer
st.markdown("---")
st.caption("📁 Data Source: Consolidated AQI, Population, Income | Powered by Streamlit & Plotly")
