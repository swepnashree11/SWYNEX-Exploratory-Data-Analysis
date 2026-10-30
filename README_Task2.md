## Task 2: Exploratory Data Analysis (EDA)

### Objective
To perform exploratory data analysis on the cleaned Cafe Sales dataset and identify important statistics, trends, patterns, and anomalies.

### Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib

### Analysis Performed
- Dataset overview and descriptive statistics
- Total revenue and average transaction value
- Item-wise revenue analysis
- Payment method analysis
- Sales by store location
- Monthly revenue trend analysis
- Outlier detection using the IQR method

### Key Findings
1. Total transactions: 10,000
2. Total revenue: 88,952
3. Average transaction value: 8.93
4. Salad generated the highest identified item revenue (17,320).
5. June recorded the highest monthly revenue (7,350).
6. 268 potential outlier transactions were detected using the IQR method.
7. In-store and Takeaway sales showed similar performance.

### Visualizations
All generated charts are available in the `task2_visualizations/` folder:

- `revenue_by_item.png`
- `payment_method.png`
- `monthly_revenue_trend.png`
- `sales_outliers.png`

### Output Files
- `task2_eda.py` – Python script for exploratory data analysis.
- `task2_insights.txt` – Summary of findings and insights.
- `task2_visualizations/` – Generated charts.

### Conclusion
The analysis identified the top revenue-generating items, payment patterns, location-based sales, monthly trends, and potential sales outliers. These insights help understand cafe sales performance and support data-driven decisions.