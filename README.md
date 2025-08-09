## 📘 Project Summary -  Air Quality Insights & Smart Purifier Market Prioritization Dashboard

### 🔍 **Problem Statement**
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
* 
### ✅ **4. Predictive Analysis**
* Used `Prophet` to forecast AQI trends for the next 12 months for Tier-1/2 cities
* Estimated **potential purifier demand** 
* Created slider-based simulation tools in Streamlit to model "what-if" demand based on AQI changes


## 📈 Deliverables
### 📊 **Interactive Streamlit Dashboard**
Key components:
* Collapsible **static overview** of insights
* City-wise AQI and demand forecast tabs
* User simulation sliders to tweak AQI and see demand changes

### 📁 **Codebase**
* Modular Python files:
  * `app.py`: main Streamlit app
  * `tabs/static_content.py`: collapsible dashboard overview
 
### 🌐 **Deployment**
* Hosted on Streamlit Community Cloud
* Publicly accessible link with live interactivity

## 🔚 Conclusion & Impact
This project empowered decision-makers with:
* Clear **visual insight** into pollution-driven demand patterns
* **Competitive analysis** to guide product development
* **Predictive tools** for seasonal planning
* A solid base for launching a **D2C e-commerce platform** in high-risk cities


     

  


