## 📘 Project Summary -  Air Quality Insights & Smart Purifier Market Prioritization Dashboard

### 🔍 **Business Problem**
"AirPure Innovations" is a startup born out of the air quality crisis in India, with 14 cities ranking among the world’s top 20 most polluted urban centers. The company is in the early stages of product development and is unsure whether there is a strong, sustained demand for its air purifier product. Before committing to production and R&D, they need to answer critical questions:
1. What pollutants or particles should their air purifier target?
2. What are the most essential features that should be incorporated into the air purifier?
3. Which cities have the highest demand for air purifiers, and what is the market size in these regions?
4. How can R&D be aligned with localized pollution patterns?

## 🔧 Tech Stack

| Layer           | Tools Used                              |
| --------------- | --------------------------------------- |
| Data Processing | `Pandas`                      |
| Visualization   | `Plotly`      |
| Prediction      | `Prophet` (for time series forecasting) |
| Dashboard       | `Streamlit`       |
| Deployment      | `Streamlit Community Cloud`, GitHub     |


## 📊 Methodology
### ✅ **1. Data Collection & Cleaning**
* Loaded and cleaned historical AQI datasets across major Indian cities (CSV file)
* Merged AQI trends with population projections, disease dataset, income estimates, and vehicle data.
* Derived **Risk Scores** based on AQI severity, population and income levels.

### ✅ **2. Exploratory Data Analysis**
* Identified spikes in AQI post-Diwali and during crop-burning months (Oct–Dec)
* Visualized city-wise AQI trends across years

### ✅ **3. Feature Gap Analysis**
* Created a detailed comparison matrix of competitor air purifiers (Xiaomi, Coway, Philips, Sharp)
* Highlighted critical gaps: CADR, H13+ HEPA, smart app, coverage area, and pricing
* Positioned “Our Product” as a high-value, AI-driven purifier with low cost of ownership
  
### ✅ **4. Predictive Analysis**
* Used `Prophet` to forecast AQI trends for the next 12 months for Tier-1/2 cities
* Estimated **potential purifier demand** 
* Created slider-based simulation tools in Streamlit to model "what-if" demand based on AQI changes

## 📊Engineered Solution
1. Designed and developed an end-to-end AQI analytics and market simulation framework using Python, Plotly, Prophet, and Streamlit to guide consumer-centric, sustainable air purifier design.
2. Built a fully interactive, one-page Streamlit dashboard that allows stakeholders to dynamically adjust parameters and instantly evaluate city-level demand and adoption scenarios.
3. Developed modules for market size estimation, consumer behavior analysis, health impact assessment, and competitive product evaluation, integrating analytics, simulation, and strategy in a single tool.
4. Implemented advanced forecasting with Prophet for real-time demand prediction and scenario analysis, providing actionable insights beyond static BI dashboards.

   
## 📈 Deliverables
### 📊 **Interactive Streamlit Dashboard & Product Requirement Document**
[Dashboard](https://aqianalysis-dfjvztzrg6rpcbrdz5ymya.streamlit.app/)

[Product Requirement Document](https://github.com/Sugiuma/Air-Quality/blob/main/Product_Req_Doc.md)

[Video presentation](https://www.youtube.com/watch?v=fart_dPZcOg)

Key components:
* Collapsible **static overview** of insights
* City-wise AQI and demand forecast tabs
* User simulation sliders to tweak AQI and see demand changes

### 📁 **Codebase**
* Modular Python files:
  * `app.py`: main Streamlit app
  * `tabs/static_content.py`: collapsible dashboard overview


## 🚀 Steps to Run Locally
1. **Clone the repository**

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Mac/Linux
   venv\Scripts\activate       # On Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   Open the link shown in the terminal (usually `http://localhost:8501`) in your browser.
 
### 🌐 **Deployment**
* Hosted on Streamlit Community Cloud
* Publicly accessible link with live interactivity

## 🔚 Conclusion & Impact

1. **Innovation:** Developed a fully interactive, one-page Streamlit platform combining static insights with dynamic city-level simulations, integrating population, disease, environmental datasets, and composite city scores.
2. **Predictive Analytics:** Implemented Prophet-based forecasting to predict real-time demand and adoption trends for air purifiers across cities, enabling scenario planning and strategic prioritization.
3. **Operational Efficiency:** Delivered a decision-ready tool that eliminates the need for navigating traditional BI dashboards, providing actionable insights on a single interface.
4. **Overall Business Value:** Empowered data-driven R&D and product strategy by translating complex environmental and market data into actionable insights for product design, market sizing, and city-level demand evaluation.


This project empowered decision-makers with:
* Clear **visual insight** into pollution-driven demand patterns
* **Competitive analysis** to guide product development
* **Predictive tools** for seasonal planning
* A solid base for launching a **D2C e-commerce platform** in high-risk cities


     

  


