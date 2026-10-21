# ☕ Coffee Shop Sales Dashboard

## 📌 Project Overview

This project analyzes coffee shop transaction data to understand sales performance, product demand, store performance, and customer purchasing patterns. It uses Excel and Power BI for data analysis and reporting, alongside an interactive dashboard built with Python, Pandas, Plotly, and Streamlit.

The goal is to transform raw sales transactions into useful business insights that can support better decision-making.

## 🎯 Business Problem

Coffee shops generate large amounts of transaction data every day. However, raw data alone does not clearly show which products perform best, when sales are highest, or how different store locations compare.

This project explores these questions through data analysis and interactive visualizations, helping users understand sales trends and identify areas for further investigation.

## 🎯 Project Objectives

- Analyze overall sales performance.
- Identify high-performing product categories and product types.
- Compare sales performance across store locations.
- Understand sales patterns by date, day, and hour.
- Present key performance indicators (KPIs) in an interactive dashboard.
- Support data-driven business decisions through visual analysis.

## 📂 Dataset Information

The project uses coffee shop transaction data stored in an Excel workbook.

**Dataset details:**

- Dataset file: `Coffee Shop Sales.xlsx`
- Worksheet: `Transactions`
- Records: Approximately 149,116 transaction rows
- Columns: 11

**Main fields include:**

- `transaction_id` — Transaction identifier
- `transaction_date` — Date of the transaction
- `transaction_time` — Time of the transaction
- `transaction_qty` — Quantity purchased
- `store_id` — Store identifier
- `store_location` — Store location
- `product_id` — Product identifier
- `unit_price` — Price per unit
- `product_category` — Product category
- `product_type` — Product type
- `product_detail` — Product description

## 🛠️ Tools and Technologies

- **Microsoft Excel:** Dataset storage and initial data exploration
- **Microsoft Power BI:** Business intelligence reporting and dashboard visualization
- **Python:** Dashboard application logic
- **Pandas:** Data loading, transformation, and analysis
- **Plotly:** Interactive charts and visualizations
- **Streamlit:** Interactive web dashboard
- **GitHub:** Project version control and source-code hosting

## 📊 Key Performance Indicators (KPIs)

The interactive dashboard calculates and displays:

- **Total Sales:** Total revenue calculated from quantity multiplied by unit price
- **Total Transactions:** Number of transaction records included in the filtered data
- **Items Sold:** Total quantity of items sold
- **Average Sales per Transaction:** Total sales divided by the number of transactions
- **Average Unit Price:** Average unit price in the filtered dataset

KPIs and visualizations respond to the selected filters.

## 📈 Dashboard Features

### 1. Executive Overview

Provides a summary of sales performance through KPI cards and charts.

### 2. Product Analysis

Explores product categories, product types, and product performance to identify important contributors to sales.

### 3. Store Performance

Compares sales performance across store locations.

### 4. Time-Based Analysis

Examines sales patterns over time, including monthly trends, days of the week, and hourly purchasing patterns.

### 5. Interactive Filters

Users can filter the dashboard by:

- Date range
- Store location
- Product category

The charts and KPI cards update according to the selected filters.

## 🔍 Analysis Approach

The project follows a practical business analytics workflow:

1. Load the transaction dataset from Excel.
2. Inspect the available fields and data structure.
3. Prepare the data for analysis.
4. Calculate sales using transaction quantity and unit price.
5. Analyze sales by product, store, and time period.
6. Develop visualizations to communicate findings.
7. Present the analysis through Power BI and an interactive Streamlit dashboard.

## 💡 Business Value

The dashboard can help a coffee shop business:

- Understand overall sales performance.
- Identify products and categories contributing to revenue.
- Compare performance across store locations.
- Recognize periods of higher and lower sales activity.
- Explore filtered data to support operational and sales decisions.

The findings can help guide further investigation into product planning, staffing, promotions, and store-level performance.

## 🚀 Run the Streamlit Dashboard Locally

### Prerequisites

Install Python and ensure that `pip` is available.

### Step 1: Clone the repository

Replace `YOUR_GITHUB_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/coffee-shop-sales-dashboard.git
```

### Step 2: Open the project folder

```bash
cd coffee-shop-sales-dashboard
```

### Step 3: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 4: Start the dashboard

```bash
streamlit run app.py
```

The dashboard should open in your browser. Keep `Coffee Shop Sales.xlsx` in the same project folder as `app.py`, because the application reads the dataset from that file.

## 📁 Project Structure

```text
coffee-shop-sales-dashboard/
│
├── app.py
├── Coffee Shop Sales.xlsx
├── Coffee SHop Dashboard.pbix
├── README.md
├── requirements.txt
└── .gitignore
```

## 🔗 Project Links

- **Live Streamlit Dashboard:** ADD_YOUR_STREAMLIT_URL_HERE
- **GitHub Repository:** ADD_YOUR_GITHUB_REPOSITORY_URL_HERE

*Replace both placeholders with the actual URLs once the project has been uploaded and deployed.*

## 📚 Learning Outcomes

Through this project, I practiced:

- Working with transaction-level business data
- Calculating and interpreting sales KPIs
- Analyzing product, store, and time-based performance
- Building interactive data visualizations
- Presenting business information through dashboards
- Organizing and documenting an analytics project on GitHub

## 👤 Author

**Alok Ranjan Pandey**

BBA — International Business Management
Interested in Business Analytics, Data Analysis, and Business Intelligence.

---

*This project is intended for learning and portfolio demonstration.*
