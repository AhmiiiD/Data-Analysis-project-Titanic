# 🚢 Titanic - Bivariate Analysis & Survival Insights

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-444876?style=for-the-badge&logo=seaborn&logoColor=white)

## 📌 Project Overview
This project focuses on performing **Bivariate Analysis** on the classic Titanic dataset to uncover the hidden patterns that influenced a passenger's chance of survival. Instead of just looking at individual variables, this analysis explores the relationships between features (like Gender, Class, and Age) and the target variable: **Survival**.

The goal is to validate historical hypotheses (such as "women and children first") using data-driven evidence.

## 📊 Key Insights & Observations
Based on the analysis of the `train.csv` file, the following key insights were discovered:

*   **Gender Bias in Survival:** There is a stark contrast in survival rates. Approximately **74% of females** survived, compared to only **19% of males**. This confirms that gender was one of the most critical predictors[cite: 1].
*   **The "Women and Children First" Policy:** The visualization clearly shows that survival protocols heavily favored female passengers, making them 3.8x more likely to survive than men[cite: 1].
*   **Socio-Economic Impact:** The analysis explores how `Pclass` (Passenger Class) and `Fare` correlated with survival, highlighting the advantage held by first-class passengers.
*   **Family Dynamics:** By creating the `alone Traveller` feature, the analysis examines whether traveling with family (`SibSp`, `Parch`) increased or decreased survival chances.

## 📁 Dataset Description
The analysis uses the **`train.csv`** file, which contains details of 891 passengers, including:
*   `Survived`: Survival (0 = No, 1 = Yes)
*   `Pclass`: Ticket class (1st, 2nd, 3rd)
*   `Sex`: Passenger gender
*   `Age`: Age in years
*   `SibSp`: Number of siblings/spouses aboard
*   `Parch`: Number of parents/children aboard
*   `Fare`: Passenger fare
*   `Embarked`: Port of Embarkation

## 🛠️ Tech Stack & Libraries
*   **Language:** Python
*   **Data Manipulation:** Pandas, NumPy
*   **Visualization:** Matplotlib, Seaborn
*   **Notebook Environment:** Jupyter Notebook

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/titanic-bivariate-analysis.git](https://github.com/your-username/titanic-bivariate-analysis.git)
