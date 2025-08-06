## 📘 Project Summary

### **Title**: Air Quality Insights & Smart Purifier Demand Forecasting Dashboard

---

### 🧩 **Objective**

To analyze city-level air quality data in India, correlate pollution levels with consumer demand triggers, and build a dynamic dashboard with predictive features to support product launch decisions for a smart air purifier. The end goal was to identify high-opportunity cities, seasons, and pricing models — and to validate product features via competitive benchmarking.

---

### 🔍 **Problem Statement**

Air purifier sales in India are seasonal and highly correlated with poor AQI events (e.g., post-Diwali, stubble burning). However, current market solutions lack personalization, affordability, and smart features. This project aims to:

* Identify **which cities** have the greatest need and market opportunity
* Forecast **seasonal demand** using AQI trends
* Compare **feature gaps** in competitor products
* Build a **Streamlit dashboard** to track and simulate demand

---

## 🔧 Tech Stack

| Layer           | Tools Used                              |
| --------------- | --------------------------------------- |
| Data Processing | `Pandas`, `NumPy`                       |
| Visualization   | `Plotly`, `Seaborn`, `Matplotlib`       |
| Prediction      | `Prophet` (for time series forecasting) |
| Dashboard       | `Streamlit`, `Pydeck`, `Plotly`         |
| Deployment      | `Streamlit Community Cloud`, GitHub     |

---

## 📊 Methodology

### ✅ **1. Data Collection & Cleaning**

* Loaded and cleaned historical AQI datasets across major Indian cities (CSV files)
* Merged AQI trends with population projections, income estimates, and healthcare data
* Derived **Risk Scores** based on AQI severity, pediatric asthma rates, and healthcare access

### ✅ **2. Exploratory Data Analysis**

* Identified spikes in AQI post-Diwali and during crop-burning months (Oct–Dec)
* Visualized city-wise AQI trends across years
* Correlated AQI with asthma hospitalization data to show health burden
* Compared average per capita income vs. product affordability

### ✅ **3. Predictive Analysis**

* Used `Prophet` to forecast AQI trends for the next 12–36 months for Tier-1/2 cities

* Estimated **potential purifier demand** using a custom formula:

  $$
  \text{Predicted Demand} = \text{Population} \times \text{AQI severity factor} \times \text{Health sensitivity weight}
  $$

* Created slider-based simulation tools in Streamlit to model "what-if" demand based on AQI changes

### ✅ **4. Feature Gap Analysis**

* Created a detailed comparison matrix of competitor air purifiers (Xiaomi, Coway, Philips, Sharp)
* Highlighted critical gaps: CADR, H13+ HEPA, smart app, coverage area, and pricing
* Positioned “Our Product” as a high-value, AI-driven purifier with low cost of ownership

---

## 📈 Deliverables

### 📊 **Interactive Streamlit Dashboard**

Key components:

* Collapsible **static overview** of insights
* City-wise AQI and demand forecast tabs
* Pydeck map to highlight target launch cities
* Feature Comparison Matrix using markdown/HTML
* User simulation sliders to tweak AQI and see demand changes

### 📁 **Codebase**

* Modular Python files:

  * `app.py`: main Streamlit app
  * `tabs/static_content.py`: collapsible product overview
  * `utils/data_loader.py`: data reading and preprocessing
  * `predict/forecast.py`: Prophet-based AQI predictions

### 🌐 **Deployment**

* Hosted on Streamlit Community Cloud
* Publicly accessible link with live interactivity

---

## 🔚 Conclusion & Impact

This project empowered decision-makers with:

* Clear **visual insight** into pollution-driven demand patterns
* **Competitive analysis** to guide product development
* **Predictive tools** for seasonal planning
* A solid base for launching a **D2C e-commerce platform** in high-risk cities

presentation.

