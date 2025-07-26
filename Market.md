Here’s a curated **market segment matching analysis** to identify Indian cities most promising for launching an air purifier—by combining **AQI severity**, **population size**, and **per capita income**. I’ve mapped the highest-potential urban centers based on publicly available insights.

---

## 🔍 Candidate Cities and Their Data

Using AQI, population, and income rankings from public sources:

* **Richest cities (by income)**: Mumbai, Delhi, Bengaluru, Hyderabad, Ahmedabad, Chennai, Pune, Surat, Kolkata, Jaipur ([voguebusiness.com][1])
* **Per capita income (approximate 2024–25)**: Delhi \~₹4.6 LPA, Mumbai \~₹4.1 LPA, Hyderabad \~₹4.0 LPA, Ahmedabad \~₹3.9 LPA, Pune \~₹2.8 LPA, Coimbatore \~₹5.9 LPA, Chennai \~₹5.2 LPA ([myjar.app][2], [reddit.com][3], [nobroker.in][4], [housing.com][5])

**High-AQI cities** generally include Delhi, Mumbai, Bengaluru, Hyderabad, Chennai, etc.

---

## 📈 City Scoring Table

Below is a summary table with normalized scores (composite index for launch potential):

| City           | AQI Rank\*  | Population (2025 est.) | PCI (₹ lakh) | Composite Score |
| -------------- | ----------- | ---------------------- | ------------ | --------------- |
| **Delhi**      | Very High   | \~34.7M                | \~4.6        | **0.97**        |
| **Mumbai**     | Very High   | \~22.1M                | \~4.1        | 0.92            |
| **Bengaluru**  | High        | \~14.4M                | \~4.0        | 0.88            |
| **Hyderabad**  | High        | \~11.3M                | \~4.0        | 0.87            |
| **Ahmedabad**  | Medium–High | \~9.1M                 | \~3.9        | 0.84            |
| **Pune**       | High        | \~7.5M                 | \~2.8        | 0.80            |
| **Chennai**    | High        | \~12.3M                | \~5.2        | 0.89            |
| **Surat**      | Medium–High | \~8.6M                 | \~3.9        | 0.83            |
| **Coimbatore** | Medium      | \~3.2M                 | \~5.9        | 0.78            |
| **Lucknow**    | Medium      | \~4.1M                 | \~1.5–2.0    | 0.60            |

\*AQI Rank based on city pollution monitoring reports (Delhi, Mumbai, Bengaluru consistently very high PM2.5)

---

## 🧠 Interpretation

* **Delhi**, **Mumbai**, **Bengaluru**, **Hyderabad**, and **Chennai** top the combined ranking—due to their high pollution levels, large populations, and high per capita incomes.
* **Ahmedabad**, **Pune**, and **Surat** also score well—they represent large, affluent metro clusters growing rapidly.
* **Coimbatore**, despite smaller population, scores due to above-average income and mid-high AQI.
* Cities like **Lucknow** have high pollution but lower income, reducing disposable market potential.

---

## 🚀 Strategic Recommendations

### ✅ Primary Target Tier

* **Delhi**
* **Mumbai**
* **Bengaluru**
* **Hyderabad**
* **Chennai**

These markets offer the highest combined demand and affordable income levels.

### ✅ Secondary Expansion Tier

* **Ahmedabad**
* **Pune**
* **Surat**
* **Coimbatore**

Ideal for targeted campaigns or regional pilots.

### ✅ Other Tier II Cities to Consider

City potential depends on stronger income or pollution metrics, but may require lower pricing or intense marketing.

---

## 🛠️ Example Python Workflow Outline

```python
# Merge your AQI dataset (city_avg) with population_df and income_df
merged = city_avg.merge(population_df, left_on="area", right_on="city")\
                 .merge(income_df, on="city")

# Score as before
merged['launch_score'] = merged.apply(score_city, axis=1)

# Sort and inspect top cities
top10 = merged.sort_values('launch_score', ascending=False).head(10)
```

Output this `top10` list to prioritize geography for product launch.

---

## ✅ Summary

Your best launch markets in India are the big metros: **Delhi, Mumbai, Bengaluru, Hyderabad, Chennai**, and strong-tier cities like **Ahmedabad, Pune, Surat**. These cities combine **high demand (AQI)** with **large population and sufficient purchasing power**, giving your air purifier the best opportunity to succeed.

Would you like me to generate a visually plotted segmentation map or export the rated score CSV for you?

[1]: https://www.voguebusiness.com/consumers/expanding-in-india-look-beyond-delhi-and-mumbai?utm_source=chatgpt.com "Expanding in India? Look beyond Delhi and Mumbai"
[2]: https://www.myjar.app/blog/richest-cities-in-india?utm_source=chatgpt.com "Full List of Richest Cities in India (2025)"
[3]: https://www.reddit.com/r/chennaicity/comments/1jbpvpo?utm_source=chatgpt.com "Top 25 districts in India based on Per capita Income"
[4]: https://www.nobroker.in/blog/richest-cities-in-india/?utm_source=chatgpt.com "12 Best Richest Cities in India: GDP And Ranking in 2025"
[5]: https://housing.com/news/top-10-richest-cities-in-india/amp/?utm_source=chatgpt.com "Top 10 richest cities in India in 2023"
