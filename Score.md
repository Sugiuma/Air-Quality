Certainly! Let’s build the dataset with publicly available sources for **population** and **income (per capita)** to score cities for an air purifier launch:

---

## 1. 🏙️ City Population Data

Based on United Nations projections (StatisticsTimes, March 2025):

| City                                 | Estimated Population (2025) |
| ------------------------------------ | --------------------------- |
| Delhi                                | 34,665,569                  |
| Mumbai                               | 22,088,953                  |
| Bengaluru                            | 14,395,443                  |
| Chennai                              | 12,336,047                  |
| Hyderabad                            | 11,337,852                  |
| Ahmedabad                            | 9,061,819                   |
| Surat                                | 8,581,733                   |
| Pune                                 | 7,525,717                   |
| Jaipur                               | 4,411,107                   |
| Patna                                | 2,689,544                   |
| Lucknow                              | 4,132,671                   |
| Coimbatore                           | 3,158,723                   |
| Visakhapatnam                        | 2,440,423                   |
| Vadodara                             | 2,424,919                   |
| Nashik                               | 2,351,139                   |
| Meerut                               | 1,874,886                   |
| Ghaziabad                            | 1,199,191                   |
| Madurai                              | 1,911,646                   |
| Thiruvananthapuram                   | 3,072,532                   |
| Tiruchirappalli (Tirunelveli region) | 1,269,897                   |

These can be loaded into a `population_df`.

([Statistics Times][1])

---

## 2. 💰 Income Data (State & District-Level)

### National/State Per Capita Income (2023‑24):

* National average per capita income: **₹1,72,000** ([Press Information Bureau][2])
* Goa: ₹3,57,611
* Delhi: ₹2,71,000
* Chandigarh: ₹2,56,912
* Sikkim: ₹2,92,339
* Tamil Nadu (2025 estimate): ₹1,96,000 ([Reddit][3], [Maharashtra Times][4], [The Times of India][5], [The Times of India][6])

### High-Income Districts (Top Tier):

* Rangareddy (Telangana): ₹11.46 LPA (\~₹1,146,000)
* Bengaluru Urban (Karnataka): ₹8.93 LPA
* Gurgaon (Haryana): ₹9.05 LPA
* Gautam Buddh Nagar (Noida): ₹8.48 LPA ([Reddit][3])

You can map city names to these district values (e.g., Bengaluru city ≈ Bengaluru Urban district; Noida → Gautam Buddh Nagar).

---

## 3. 📋 Build the Dataset

### Step 1: Create `population_df` and `income_df`

```python
population_df = pd.DataFrame({
  'city': ['Delhi', 'Mumbai', 'Bengaluru', ...],
  'population': [34665569, 22088953, 14395443, ...]
})

income_df = pd.DataFrame({
  'city': ['Delhi', 'Bengaluru', 'Gurugram', 'Noida', ...],
  'per_capita_income': [271000, 893000, 905000, 848000, ...]
})
```

### Step 2: Merge with AQI data

```python
df = city_avg.merge(population_df, left_on='area', right_on='city', how='left')\
              .merge(income_df, on='city', how='left')
```

### Step 3: Compute launch potential score

```python
def score_city(row):
    pollution = min(row['aqi_value'] / 500, 1.0)
    pop = min(row['population'] / 1_000_000, 1.0)
    inc = min(row['per_capita_income'] / 200000, 1.0)
    return 0.4 * pollution + 0.3 * pop + 0.3 * inc

df['launch_score'] = df.apply(score_city, axis=1)
top = df.sort_values('launch_score', ascending=False).head(10)
```

---

## 4. 🏆 Recommended Priority Cities

Based on combining high AQI, population, and income, cities likely to be top candidates include:

* **Delhi**, **Mumbai**, **Bengaluru**, **Hyderabad**, **Gurugram**, **Noida**, **Pune**, **Chennai**, **Ahmedabad**, **Surat**

---

## ✅ Next Steps:

* I can help generate these CSV files with the data above.
* I can expand to other cities using district-level income proxies.
* I can help write code to score and visualize results.

Would you like me to output example CSVs and code ready to merge with your AQI dataset?

[1]: https://statisticstimes.com/demographics/country/india-cities-population.php?utm_source=chatgpt.com "Population of cities in India 2025 - StatisticsTimes.com"
[2]: https://pib.gov.in/PressReleaseIframePage.aspx?PRID=1913325&utm_source=chatgpt.com "Per Capita Income in Rural and Urban Areas"
[3]: https://www.redditmedia.com/r/chennaicity/comments/1jbpvpo/top_25_districts_in_india_based_on_per_capita/?utm_source=chatgpt.com "Top 25 districts in India based on Per capita Income"
[4]: https://marathi.indiatimes.com/business/business-news/richest-and-poorest-states-in-india-as-per-capta-income/articleshow/122873001.cms?utm_source=chatgpt.com "Per Capita Income : भारतातील सर्वात गरीब अन् श्रीमंत राज्य कोणतं, महाराष्ट्र कोणत्या स्थानी? कोण टॉपला? पाहा लिस्ट"
[5]: https://timesofindia.indiatimes.com/city/chandigarh/per-capita-income-sikkim-dethrones-ut-from-top-3/articleshow/122866639.cms?utm_source=chatgpt.com "Per capita income: Sikkim dethrones UT from Top 3"
[6]: https://timesofindia.indiatimes.com/city/chennai/cm-tn-will-top-per-capita-income-under-dmk-2-0/articleshow/122866898.cms?utm_source=chatgpt.com "CM: TN will top per capita income under DMK 2.0"
