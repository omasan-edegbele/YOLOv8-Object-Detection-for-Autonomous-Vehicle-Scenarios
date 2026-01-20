# Tesla Fatality Data Analysis

## 📌 Overview
This project analyzes **reported Tesla-related fatalities** using a structured CSV dataset. The goal is to explore patterns in fatal incidents involving Tesla vehicles, focusing on incident severity, driver involvement, and occupant outcomes.

The analysis applies **exploratory data analysis (EDA)** techniques to better understand real-world safety outcomes associated with advanced driver-assistance and autonomous vehicle technologies.

---

## 🎯 Objective
To examine Tesla-related fatality data and identify trends related to:
- Number of deaths per incident
- Frequency of Tesla driver fatalities
- Occupant involvement in fatal crashes
- Distribution of fatal outcomes across reported events

---

## 📂 Dataset
- **File:** `Tesla_Deaths.csv`
- **Format:** CSV
- **Description:** Incident-level records of reported Tesla-related fatalities

### Key Data Fields
- Total number of deaths per incident
- Tesla driver fatalities
- Tesla occupant fatalities
- Incident characteristics and counts

---

## 🧠 Methodology
- Loaded and cleaned the dataset using **Pandas**
- Performed exploratory data analysis (EDA)
- Aggregated fatality counts by incident
- Analyzed distributions of deaths and driver involvement
- Visualized trends using plots and summary statistics
- Interpreted findings to contextualize autonomous vehicle safety risks

---

## 📊 Key Findings (High-Level)
- Most fatal incidents involved **one or two deaths**
- Multi-fatality incidents were relatively rare
- Tesla driver fatalities occurred in a subset of incidents
- Analysis highlights the importance of evaluating **incident severity**, not just incident frequency

---

## 🛠️ Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📓 Notebook
- `OE_Capstone1_Part2.ipynb`

---

## ⚠️ Notes & Limitations
- The dataset includes only reported incidents and may not represent all Tesla-related crashes
- The analysis is **descriptive**, not predictive
- No causal conclusions are drawn regarding autonomous driving systems

---

## 🔮 Future Work
- Expand the dataset to include additional manufacturers
- Perform time-series analysis of fatal incidents
- Incorporate geographic breakdowns
- Normalize fatalities by exposure metrics (e.g., miles driven)
