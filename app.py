import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Coffee Shop Sales Dashboard",
    page_icon="☕",
    layout="wide"
)

DATA_FILE = Path(__file__).parent / "Coffee Shop Sales.xlsx"

@st.cache_data
def load_data():
    data = pd.read_excel(DATA_FILE, sheet_name="Transactions")
    data.columns = [str(c).strip() for c in data.columns]
    data["transaction_date"] = pd.to_datetime(data["transaction_date"], errors="coerce")
    data["transaction_qty"] = pd.to_numeric(data["transaction_qty"], errors="coerce").fillna(0)
    data["unit_price"] = pd.to_numeric(data["unit_price"], errors="coerce").fillna(0)
    data["sales"] = data["transaction_qty"] * data["unit_price"]
    data["month"] = data["transaction_date"].dt.to_period("M").astype(str)
    data["day_name"] = data["transaction_date"].dt.day_name()
    data["hour"] = pd.to_datetime(data["transaction_time"].astype(str), errors="coerce").dt.hour
    return data

st.title("☕ Coffee Shop Sales Dashboard")
st.caption("Interactive analysis of transaction volume, sales, products, stores, and purchasing patterns.")

if not DATA_FILE.exists():
    st.error("Data file not found. Put 'Coffee Shop Sales.xlsx' in the same folder as app.py.")
    st.stop()

df = load_data()
if df.empty:
    st.warning("The workbook has no transaction rows.")
    st.stop()

with st.sidebar:
    st.header("Dashboard Filters")
    min_date = df["transaction_date"].min().date()
    max_date = df["transaction_date"].max().date()
    date_range = st.date_input(
        "Transaction date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    locations = sorted(df["store_location"].dropna().unique().tolist())
    selected_locations = st.multiselect("Store location", locations, default=locations)
    categories = sorted(df["product_category"].dropna().unique().tolist())
    selected_categories = st.multiselect("Product category", categories, default=categories)

filtered = df.copy()
if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        filtered["transaction_date"].dt.date.between(start_date, end_date)
    ]
if selected_locations:
    filtered = filtered[filtered["store_location"].isin(selected_locations)]
else:
    filtered = filtered.iloc[0:0]
if selected_categories:
    filtered = filtered[filtered["product_category"].isin(selected_categories)]
else:
    filtered = filtered.iloc[0:0]

if filtered.empty:
    st.warning("No transactions match the selected filters. Change the filters in the sidebar.")
    st.stop()

total_sales = filtered["sales"].sum()
total_transactions = filtered["transaction_id"].nunique()
total_items = filtered["transaction_qty"].sum()
average_transaction = total_sales / total_transactions if total_transactions else 0
average_price = filtered["unit_price"].mean()

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Sales", f"${total_sales:,.2f}")
c2.metric("Transactions", f"{total_transactions:,}")
c3.metric("Items Sold", f"{total_items:,.0f}")
c4.metric("Avg. Sales / Transaction", f"${average_transaction:,.2f}")
c5.metric("Average Unit Price", f"${average_price:,.2f}")

st.divider()

tab1, tab2, tab3, tab4 = st.tabs([
    "Overview", "Products", "Store Performance", "Time Patterns"
])

with tab1:
    left, right = st.columns(2)
    sales_by_date = filtered.groupby("transaction_date", as_index=False)["sales"].sum()
    fig = px.line(sales_by_date, x="transaction_date", y="sales",
                  title="Daily Sales Trend", markers=False,
                  labels={"transaction_date": "Date", "sales": "Sales ($)"})
    left.plotly_chart(fig, use_container_width=True)

    category_sales = filtered.groupby("product_category", as_index=False).agg(
        sales=("sales", "sum"), items=("transaction_qty", "sum")
    ).sort_values("sales", ascending=False)
    fig = px.bar(category_sales, x="product_category", y="sales",
                 title="Sales by Product Category", color="sales",
                 labels={"product_category": "Category", "sales": "Sales ($)"})
    right.plotly_chart(fig, use_container_width=True)

    st.subheader("Top 10 Products by Sales")
    top_products = filtered.groupby("product_detail", as_index=False).agg(
        sales=("sales", "sum"),
        items=("transaction_qty", "sum"),
        transactions=("transaction_id", "nunique")
    ).sort_values("sales", ascending=False).head(10)
    st.dataframe(top_products, use_container_width=True, hide_index=True)

with tab2:
    left, right = st.columns(2)
    product_type = filtered.groupby("product_type", as_index=False).agg(
        sales=("sales", "sum"), items=("transaction_qty", "sum")
    ).sort_values("sales", ascending=False).head(15)
    fig = px.bar(product_type.sort_values("sales"), x="sales", y="product_type",
                 orientation="h", title="Top 15 Product Types by Sales",
                 labels={"sales": "Sales ($)", "product_type": "Product Type"})
    left.plotly_chart(fig, use_container_width=True)

    product_category = filtered.groupby("product_category", as_index=False).agg(
        items=("transaction_qty", "sum"), sales=("sales", "sum")
    ).sort_values("items", ascending=False)
    fig = px.pie(product_category, names="product_category", values="items",
                 title="Items Sold by Category", hole=0.45)
    right.plotly_chart(fig, use_container_width=True)

    st.subheader("Product Detail Performance")
    product_table = filtered.groupby(
        ["product_category", "product_type", "product_detail"], as_index=False
    ).agg(
        sales=("sales", "sum"),
        items=("transaction_qty", "sum"),
        transactions=("transaction_id", "nunique"),
        average_unit_price=("unit_price", "mean")
    ).sort_values("sales", ascending=False)
    st.dataframe(product_table, use_container_width=True, hide_index=True)

with tab3:
    store_perf = filtered.groupby("store_location", as_index=False).agg(
        sales=("sales", "sum"),
        transactions=("transaction_id", "nunique"),
        items=("transaction_qty", "sum")
    ).sort_values("sales", ascending=False)
    left, right = st.columns(2)
    fig = px.bar(store_perf, x="store_location", y="sales", color="store_location",
                 title="Sales by Store Location",
                 labels={"store_location": "Store", "sales": "Sales ($)"})
    left.plotly_chart(fig, use_container_width=True)
    fig = px.scatter(store_perf, x="transactions", y="sales", size="items",
                     color="store_location", hover_name="store_location",
                     title="Store Sales vs. Transactions",
                     labels={"transactions": "Transactions", "sales": "Sales ($)", "items": "Items Sold"})
    right.plotly_chart(fig, use_container_width=True)
    st.dataframe(store_perf, use_container_width=True, hide_index=True)

with tab4:
    hourly = filtered.dropna(subset=["hour"]).groupby("hour", as_index=False).agg(
        sales=("sales", "sum"),
        transactions=("transaction_id", "nunique")
    )
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    daily = filtered.groupby("day_name", as_index=False).agg(
        sales=("sales", "sum"),
        transactions=("transaction_id", "nunique")
    )
    daily["day_name"] = pd.Categorical(daily["day_name"], categories=day_order, ordered=True)
    daily = daily.sort_values("day_name")
    left, right = st.columns(2)
    fig = px.bar(hourly, x="hour", y="transactions", title="Transactions by Hour",
                 labels={"hour": "Hour of Day", "transactions": "Transactions"})
    left.plotly_chart(fig, use_container_width=True)
    fig = px.bar(daily, x="day_name", y="sales", title="Sales by Day of Week",
                 labels={"day_name": "Day", "sales": "Sales ($)"})
    right.plotly_chart(fig, use_container_width=True)

    monthly = filtered.groupby("month", as_index=False).agg(
        sales=("sales", "sum"),
        transactions=("transaction_id", "nunique")
    ).sort_values("month")
    fig = px.line(monthly, x="month", y="sales", title="Monthly Sales Trend",
                  markers=True, labels={"month": "Month", "sales": "Sales ($)"})
    st.plotly_chart(fig, use_container_width=True)

with st.expander("Data notes and methodology"):
    st.markdown(
        "- **Sales** is calculated as `transaction_qty × unit_price` for each transaction row.\n"
        "- **Transactions** counts distinct `transaction_id` values after applying the filters.\n"
        "- The workbook contains transaction-level data. The dashboard's totals change when filters are changed.\n"
        "- Sales are calculated from the supplied workbook; they should not be interpreted as audited accounting revenue."
    )

st.caption("Coffee Shop Sales Analysis | Built with Python, Pandas, Plotly, and Streamlit")
