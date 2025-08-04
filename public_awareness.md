Internet penetration in **Indian metro cities** is significantly higher than state/national averages, often reaching **80–90%** or more due to better infrastructure, urbanization, and smartphone access.

## 🌆 Internet Penetration in Major Indian Metro Cities (2023–2024 Estimates)

| City          | Estimated Internet Penetration (%) | Notes / Source                                                                                                                                                                                  |
| ------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Delhi NCR** | 85–90%                             | One of the most digitally connected regions in India ([IAMAI 2023](https://www.iamai.in))                                                                                                       |
| **Mumbai**    | 83–87%                             | High smartphone usage, strong broadband presence ([DataReportal](https://datareportal.com))                                                                                                     |
| **Bangalore** | 85%                                | Top tech city; nearly saturated urban market ([TRAI Reports](https://trai.gov.in))                                                                                                              |
| **Chennai**   | 80–85%                             | Strong mobile and broadband usage                                                                                                                                                               |
| **Hyderabad** | 82–85%                             | Telangana ranks #2 in India for net penetration ([TOI, 2023](https://timesofindia.indiatimes.com/city/hyderabad/telangana-second-only-to-kerala-in-net-subscriptions/articleshow/98787925.cms)) |
| **Kolkata**   | 75–80%                             | Urban net access improving rapidly, but rural outskirts pull avg. down                                                                                                                          |
| **Pune**      | 82–85%                             | Urban tech hub, close to Mumbai stats                                                                                                                                                           |
| **Ahmedabad** | 75–80%                             | High internet adoption in urban Gujarat                                                                                                                                                         |
| **Surat**     | 70–75%                             | Growing penetration, but lower than Mumbai                                                                                                                                                      |
| **Jaipur**    | 70–75%                             | High urban-rural divide, improving                                                                                                                                                              |

### 🧠 Key Points:

* **Urban digital divide is shrinking**, but still exists in peripheral zones.
* Penetration is highest in **Delhi, Mumbai, Bangalore**, and **Hyderabad**.
* **Mobile internet** is the dominant access mode (\~97%+ in metros).

---

### ✅ Use in Code (Example)

```python
internet_penetration_city = {
    "Delhi": 0.88,
    "Mumbai": 0.85,
    "Bangalore": 0.85,
    "Chennai": 0.83,
    "Hyderabad": 0.84,
    "Kolkata": 0.78
}
```

Then use:

```python
estimated_awareness = (search_score / 100) * internet_penetration_city[city]
```

Would you like to overlay this with your Google Trends data in a bar or heatmap chart to visualize **city-wise AQI awareness potential**?


Here are the **approximate internet penetration rates** for the major **Southern Indian states**—based on the most recent public data (TRAI, IAMAI/Kantar, DataReportal, NFHS)—along with a useful reference table you can plug into your awareness model.

---

## 🌐 Internet Penetration Estimates for Southern States (2023–2024)

| State              | Penetration Rate (% of population) | Notes / Source                                                                                                     |
| ------------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Kerala**         | \~ 69–71%                          | Highest in India after Delhi ([GrabOn][1])                                                                         |
| **Telangana**      | \~ 83%                             | Second only to Kerala nationally ([The Times of India][2], [Wikipedia][3])                                         |
| **Karnataka**      | \~ 68%                             | Among top penetration rates in 2023–24 ([The Times of India][2], [RSA Regions][4])                                 |
| **Tamil Nadu**     | \~ 67%                             | High urban & rural coverage; state digital initiative ([Wikipedia][5], [RSA Regions][4])                           |
| **Andhra Pradesh** | \~ 59%                             | \~67.1 million internet subscribers in 2023; \~60%+ penetration estimate ([Wikipedia][6], [The Times of India][2]) |

---

### ✅ How to Use these in your Python Code

```python
internet_reach_south = {
    "Kerala": 0.70,
    "Telangana": 0.83,
    "Karnataka": 0.68,
    "Tamil Nadu": 0.67,
    "Andhra Pradesh": 0.59
}
```

You can then compute:

```python
estimated_awareness_percent = (float(search_interest) / 100) * internet_reach_south[state] * 100
```

— where `search_interest` is your Google Trends score.

---

### 🧠 Why These Estimates Matter

* These rates combine **NFHS gendered figures** and **state-level internet subscriber data** from TRAI and IAMAI to produce consensus figures.
* Kerala and Telangana top the list due to both urban saturation and strong digital infrastructure.
* Andhra Pradesh lags slightly behind but still ranks among **India’s high-penetration southern states**.

---

Would you like help building a combined dashboard that matches **search trends, internet reach, and actual AQI levels** for these southern states (or others)?

[1]: https://www.grabon.in/indulge/tech/internet-users-statistics/?utm_source=chatgpt.com "Internet Statistics in India: Usage and Penetration Rate (2025)"
[2]: https://timesofindia.indiatimes.com/city/hyderabad/telangana-second-only-to-kerala-in-net-subscriptions/articleshow/98787925.cms?utm_source=chatgpt.com "Telangana second only to Kerala in Net subscriptions - Times of India"
[3]: https://en.wikipedia.org/wiki/Kerala?utm_source=chatgpt.com "Kerala"
[4]: https://regions.regionalstudies.org/ezine/article/digitisation-in-india/?doi=10.1080%2F13673882.2021.00001100&utm_source=chatgpt.com "Contours of Internet Access in Rural-Urban Landscapes in India"
[5]: https://en.wikipedia.org/wiki/Tamil_Nadu?utm_source=chatgpt.com "Tamil Nadu"
[6]: https://en.wikipedia.org/wiki/Andhra_Pradesh?utm_source=chatgpt.com "Andhra Pradesh"


Here are the latest **estimated internet penetration rates** for your top‑10 states, which you can use to refine awareness analysis:

---

### 🌐 Internet Penetration by State (Percent of Population)

Based on aggregated data from TRAI, IAMAI, DataReportal, and other public sources as of early–mid 2024:

| State          | Internet Penetration (%) |
| -------------- | ------------------------ |
| Delhi          | \~74 – 85%               |
| Haryana        | \~60 – 72%               |
| Punjab         | \~55 – 78%               |
| West Bengal    | \~46 – 67%               |
| Rajasthan      | \~37 – 66%               |
| Uttar Pradesh  | \~30 – 59%               |
| Madhya Pradesh | \~27 – 56%               |
| Odisha         | \~25 – 51%               |
| Assam          | \~28 – 43%               |
| Bihar          | \~20 – 44%               |

**Notes:**

* Delhi tops the list at **63.8 % female and 85.2 % male users**, with combined penetration around **74 – 85 %** ([FindEasy][1])
* Bihar registers the lowest estimates at around **20.6 % female and 43.6 % male**, implying **\~30–37 % penetration** ([FindEasy][1], [GrabOn][2])
* States like **Punjab, Haryana, Kerala, Maharashtra** report higher figures (in the **upper 60–70 %** range) ([FindEasy][1], [GrabOn][2])
* National-level average is around **52.4 %** in early 2024 ([DataReportal – Global Digital Insights][3])

---

### ✅ How to Apply in Code

Use these approximate penetration rates in your Python model like so:

```python
internet_reach = {
    "Delhi": 0.80,
    "Haryana": 0.66,
    "Punjab": 0.70,
    "West Bengal": 0.55,
    "Rajasthan": 0.52,
    "Uttar Pradesh": 0.45,
    "Madhya Pradesh": 0.42,
    "Odisha": 0.38,
    "Assam": 0.36,
    "Bihar": 0.30
}
```

Then calculate:

```python
awareness_percent = (search_interest / 100) * internet_reach[state] * 100
```

---

### 📌 Why These Are Estimates Only

* State-level granular penetration isn't publicly released annually. Data sources like IAMAI ICUBE and TRAI provide samples or segmented demographics.
* Rural–urban digital gaps remain significant; rates vary internally within a state.
* There's a gender dimension: urban males often outpace rural females.

---

Would you like assistance creating a **table or dashboard** that combines Google Trends data with these internet rates to estimate **state-by-state awareness percentages**? If you have more recent per‑state data, I can help incorporate that, too.

[1]: https://www.findeasy.in/indian-states-by-internet-users/?utm_source=chatgpt.com "Indian States by Internet Users 2024 | Find Easy"
[2]: https://www.grabon.in/indulge/tech/internet-users-statistics/?utm_source=chatgpt.com "Internet Statistics in India: Usage and Penetration Rate (2025)"
[3]: https://datareportal.com/reports/digital-2024-india?utm_source=chatgpt.com "Digital 2024: India — DataReportal – Global Digital Insights"
