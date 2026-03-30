import streamlit as st
import pandas as pd
import plotly.express as px
 

st.set_page_config(page_title="Retail Order Analysis", layout='wide')
st.title("🛒 Retail Order Data Analysis")

# ── Load & Prepare Data ────────────────────────────────
@st.cache_data
def load_data():
  
   

    
    df = pd.read_csv("Retail_order_data_analysis/orders.csv")
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df['discount_amount'] = df['list_price'] * df['discount_percent'] * 0.01
    df['sale_price']      = df['list_price'] - df['discount_amount']
    df['profit']          = df['sale_price'] - df['cost_price']
    df['revenue']         = df['sale_price'] * df['quantity']
    df['profit']          = df['profit']     * df['quantity']
    df['discount_amount'] = df['discount_amount'] * df['quantity']
    df['order_date']      = pd.to_datetime(df['order_date'])
    df['order_year']      = df['order_date'].dt.year
    df['order_month']     = df['order_date'].dt.month
    return df

df = load_data()

# ── Sidebar ────────────────────────────────────────────
st.sidebar.title("📊 Select Report")
option = st.sidebar.selectbox("Choose a Query", [
    "data",
    "Q1  - Top 10 Revenue Products",
    "Q2  - Top 5 Cities by Profit Margin",
    "Q3  - Total Discount per Category",
    "Q4  - Avg Sale Price per Product Category",
    "Q5  - Region with Highest Avg Sale Price",
    "Q6  - Total Profit per Category",
    "Q7  - Top 3 Segments by Orders",
    "Q8  - Avg Discount % per Region",
    "Q9  - Category with Highest Total Profit",
    "Q10 - Total Revenue per Year",
    "Q11 - YoY Sales Growth per Category",
    "Q12 - Month with Highest Sales",
    "Q13 - Top 5 Sub-Categories by Profit Margin",
    "Q14 - Products with Discount > 20%",
    "Q15 - Rank Products by Revenue in Category",
    "Q16 - Segment-wise Profit Contribution %",
    "Q17 - Monthly MoM Revenue Change",
    "Q18 - Region with Most Orders per Category",
    "Q19 - Categories where Avg Profit > 100",
    "Q20 - Bottom 5 Loss-Making Products",
])
#data
if option=="data":
    st.subheader("Retail order dataset")
    st.dataframe(df)
# Q1
if option == "Q1  - Top 10 Revenue Products":
    st.subheader("🏆 Q1: Top 10 Highest Revenue Generating Products")
    data = df.groupby('product_id')['revenue'].sum().round(2).reset_index()
    data.columns = ['product_id', 'total_revenue']
    data = data.sort_values('total_revenue', ascending=False).head(10)
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="product_id", y="total_revenue", color="total_revenue", text="total_revenue")
    fig.update_traces(texttemplate='$%{text:,.2f}')
    fig.update_layout(xaxis_title="Product ID", yaxis_title="Total Revenue",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""TEC-CO-10004722 is the revenue king at $2,45,056 — nearly 1.5x more than the second-best product.
            7 out of the top 10 products belong to Technology and Office Supplies (Binders),
            confirming these segments drive the most sales value in the business.""")

# Q2
elif option == "Q2  - Top 5 Cities by Profit Margin":
    st.subheader("🏙️ Q2: Top 5 Cities with Highest Profit Margins")
    data = df.groupby('city').agg(profit=('profit','sum'), revenue=('revenue','sum')).reset_index()
    data['profit_margin'] = (data['profit'] / data['revenue'] * 100).round(2)
    data = data.sort_values('profit_margin', ascending=False).head(5)[['city','profit_margin']]
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="city", y="profit_margin", color="profit_margin", text="profit_margin")
    fig.update_traces(texttemplate='%{text:.2f}%')
    fig.update_layout(xaxis_title="City", yaxis_title="Profit Margin %")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Danbury and Goldsboro share the highest profit margin at 29.82%, followed by Bozeman (25.02%),
            Rogers (23.47%), and Owensboro (22.87%).
            These cities are the most efficient markets — small in volume but extremely profitable per sale.""")

# Q3
elif option == "Q3  - Total Discount per Category":
    st.subheader("🏷️ Q3: Total Discount Given per Category")
    data = df.groupby('category')['discount_amount'].sum().round(2).reset_index()
    data.columns = ['category', 'total_discount']
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="category", y="total_discount", color="total_discount", text="total_discount")
    fig.update_traces(texttemplate='$%{text:,.2f}')
    fig.update_layout(xaxis_title="Category", yaxis_title="Total Discount",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Technology received the highest total discount, followed by Furniture and Office Supplies.
            Despite having the most discount given, Technology still leads in profit —
            showing its strong base pricing absorbs discounts well.""")

# Q4
elif option == "Q4  - Avg Sale Price per Product Category":
    st.subheader("💲 Q4: Average Sale Price per Product Category")
    data = df.groupby('category')['sale_price'].mean().round(2).reset_index()
    data.columns = ['category', 'average_sale_price']
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="category", y="average_sale_price", color="average_sale_price", text="average_sale_price")
    fig.update_traces(texttemplate='$%{text:,.2f}')
    fig.update_layout(xaxis_title="Category", yaxis_title="Average Sale Price",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Technology dominates with an average sale price of $436.86 — nearly 4x that of Office Supplies ($115.11).
            Furniture sits at $337.27. This confirms Technology products are premium-priced,
            making every sale significantly more valuable.""")

# Q5
elif option == "Q5  - Region with Highest Avg Sale Price":
    st.subheader("🌍 Q5: Region with Highest Average Sale Price")
    data = df.groupby('region')['sale_price'].mean().round(2).reset_index()
    data.columns = ['region', 'avg_sale_price']
    data = data.sort_values('avg_sale_price', ascending=False)
    st.dataframe(data, use_container_width=True)
    st.metric(label=f"🥇 Top Region: {data.iloc[0]['region']}",
              value=f"${data.iloc[0]['avg_sale_price']:,.2f}")
    fig = px.bar(data, x="region", y="avg_sale_price", color="avg_sale_price", text="avg_sale_price")
    fig.update_traces(texttemplate='$%{text:,.2f}')
    fig.update_layout(xaxis_title="Region", yaxis_title="Avg Sale Price",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""The South region leads with the highest average sale price, ahead of East, West, and Central.
            The South is consistently selling higher-value products,
            making it the most premium market in the country.""")

# Q6
elif option == "Q6  - Total Profit per Category":
    st.subheader("💰 Q6: Total Profit per Category")
    data = df.groupby('category')['profit'].sum().round(2).reset_index()
    data.columns = ['category', 'total_profit']
    data = data.sort_values('total_profit', ascending=False)
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="category", y="total_profit", color="total_profit", text="total_profit")
    fig.update_traces(texttemplate='$%{text:,.2f}')
    fig.update_layout(xaxis_title="Category", yaxis_title="Total Profit",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Technology generates 37% of all profit, followed by Furniture and Office Supplies.
            Profits are fairly well distributed, but Technology has a clear edge —
            worth investing more in this category.""")

# Q7
elif option == "Q7  - Top 3 Segments by Orders":
    st.subheader("📦 Q7: Top 3 Segments by Order Quantity")
    data = df.groupby('segment')['order_id'].count().reset_index()
    data.columns = ['segment', 'total_orders']
    data = data.sort_values('total_orders', ascending=False).head(3)
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="segment", y="total_orders", color="total_orders", text="total_orders")
    fig.update_layout(xaxis_title="Segment", yaxis_title="Total Orders")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Consumers place 5,191 orders (52% of all orders), followed by Corporate (3,020) and Home Office (1,783).
            The Consumer segment is by far the most active —
            marketing and loyalty programs should primarily target this group.""")

# Q8
elif option == "Q8  - Avg Discount % per Region":
    st.subheader("🏷️ Q8: Average Discount % per Region")
    data = df.groupby('region')['discount_percent'].mean().round(2).reset_index()
    data.columns = ['region', 'avg_discount_pct']
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="region", y="avg_discount_pct", color="avg_discount_pct", text="avg_discount_pct")
    fig.update_traces(texttemplate='%{text:.2f}%')
    fig.update_layout(xaxis_title="Region", yaxis_title="Avg Discount %")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""All four regions have almost identical average discounts — between 3.47% and 3.49%.
            This means discounting is applied uniformly with no region-specific strategy.
            There's a clear opportunity to use targeted discounting to boost underperforming regions like Central.""")

# Q9
elif option == "Q9  - Category with Highest Total Profit":
    st.subheader("🥇 Q9: Category with Highest Total Profit")
    data = df.groupby('category')['profit'].sum().round(2).reset_index()
    data.columns = ['category', 'total_profit']
    data = data.sort_values('total_profit', ascending=False).head(1)
    st.dataframe(data, use_container_width=True)
    st.metric(label=f"🏆 {data.iloc[0]['category']}",
              value=f"${data.iloc[0]['total_profit']:,.2f}")
    st.info("""Technology is the most profitable category, contributing 37% of total profit.
            It leads despite receiving the most total discounts,
            proving that even after discounting, Technology products maintain strong margins.""")

# Q10
elif option == "Q10 - Total Revenue per Year":
    st.subheader("📅 Q10: Total Revenue per Year")
    data = df.groupby('order_year')['revenue'].sum().round(2).reset_index()
    data.columns = ['year', 'total_revenue']
    data['year'] = data['year'].astype(str)
    st.dataframe(data, use_container_width=True)
    fig = px.line(data, x="year", y="total_revenue", markers=True, title="Yearly Revenue Trend")
    fig.update_layout(xaxis_title="Year", yaxis_title="Total Revenue",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Revenue grew positively from 2022 to 2023.
            The business is stable but needs stronger strategies to accelerate revenue expansion.""")

# Q11
elif option == "Q11 - YoY Sales Growth per Category":
    st.subheader("📈 Q11: YoY Sales Growth per Category")
    yoy = df.groupby(['category','order_year'])['revenue'].sum().reset_index()
    yoy.columns = ['category','year','revenue']
    yoy = yoy.sort_values(['category','year'])
    yoy['yoy_sales'] = yoy.groupby('category')['revenue'].pct_change().round(4) * 100
    yoy['yoy_sales'] = yoy['yoy_sales'].round(2)
    st.dataframe(yoy, use_container_width=True)
    chart_data = yoy.dropna(subset=['yoy_sales'])
    chart_data['year'] = chart_data['year'].astype(str)
    fig = px.bar(chart_data, x="category", y="yoy_sales", color="category",
                 text="yoy_sales", title="YoY Sales Growth % (2023 vs 2022)")
    fig.update_traces(texttemplate='%{text:.2f}%')
    fig.update_layout(xaxis_title="Category", yaxis_title="YoY Growth %")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Technology showed the strongest growth at +7.31%, followed by Office Supplies at +6.83%.
            However, Furniture declined by -6.43% —
            a significant warning sign that needs urgent attention in product mix or pricing strategy.""")

# Q12
elif option == "Q12 - Month with Highest Sales":
    st.subheader("📆 Q12: Month with Highest Sales")
    data = df.groupby('order_month')['revenue'].sum().round(2).reset_index()
    data.columns = ['month', 'total_sales']
    month_names = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
                   7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    data['month_name'] = data['month'].map(month_names)
    data = data.sort_values('total_sales', ascending=False)
    top = data.iloc[0]
    st.dataframe(data[['month_name','total_sales']], use_container_width=True)
    st.metric(label=f"🗓️ Best Month: {top['month_name']}",
              value=f"${top['total_sales']:,.2f}")
    st.info("""October is the peak sales month — the highest of any month.
            This reflects year-end budget spending by Corporate buyers and early holiday demand.
            Inventory and staffing should be ramped up by September to handle the surge.""")

# Q13
elif option == "Q13 - Top 5 Sub-Categories by Profit Margin":
    st.subheader("📊 Q13: Top 5 Sub-Categories by Profit Margin")
    data = df.groupby('sub_category').agg(profit=('profit','sum'), revenue=('revenue','sum')).reset_index()
    data['profit_margin'] = (data['profit'] / data['revenue'] * 100).round(2)
    data = data.sort_values('profit_margin', ascending=False).head(5)[['sub_category','profit_margin']]
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="sub_category", y="profit_margin", color="profit_margin", text="profit_margin")
    fig.update_traces(texttemplate='%{text:.2f}%')
    fig.update_layout(xaxis_title="Sub Category", yaxis_title="Profit Margin %")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Copiers lead with a 10.91% margin, followed by Machines (10.36%), Appliances (10.33%),
            Binders (10.12%), and Chairs (9.59%).
            All top margin sub-categories are high-ticket items — reinforcing the value of focusing on premium product lines.""")

# Q14
elif option == "Q14 - Products with Discount > 20%":
    st.subheader("🏷️ Q14: Products with Discount > 20%")
    data = df[df['discount_percent'] > 20].groupby('product_id').agg(
        total_revenue=('revenue','sum'),
        total_discount=('discount_amount','sum')
    ).round(2).reset_index()
    data = data.sort_values('total_discount', ascending=False)
    if data.empty:
        st.info("✅ No products have a discount greater than 20%. The business maintains disciplined pricing and avoids aggressive markdowns that could erode margins.")
    else:
        st.dataframe(data, use_container_width=True)
        fig = px.bar(data, x="product_id", y="total_discount", color="total_discount", text="total_discount")
        fig.update_traces(texttemplate='$%{text:,.2f}')
        fig.update_layout(xaxis_title="Product ID", yaxis_title="Total Discount")
        st.plotly_chart(fig, use_container_width=True)

# Q15
elif option == "Q15 - Rank Products by Revenue in Category":
    st.subheader("🥇 Q15: Products Ranked by Revenue within Each Category")
    data = df.groupby(['category','product_id'])['revenue'].sum().round(2).reset_index()
    data.columns = ['category','product_id','total_revenue']
    data['rank'] = data.groupby('category')['total_revenue'].rank(method='dense', ascending=False).astype(int)
    data = data.sort_values(['category','rank'])
    category_filter = st.selectbox("🔍 Filter by Category", data['category'].unique())
    filtered = data[data['category'] == category_filter]
    st.dataframe(filtered, use_container_width=True)
    fig = px.bar(filtered.head(10), x="product_id", y="total_revenue",
                 color="total_revenue", text="total_revenue")
    fig.update_traces(texttemplate='$%{text:,.2f}')
    fig.update_layout(xaxis_title="Product ID", yaxis_title="Revenue",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)

# Q16
elif option == "Q16 - Segment-wise Profit Contribution %":
    st.subheader("🥧 Q16: Segment-wise Profit Contribution %")
    total_profit = df['profit'].sum()
    data = df.groupby('segment')['profit'].sum().round(2).reset_index()
    data.columns = ['segment','segment_profit']
    data['profit_pct'] = (data['segment_profit'] / total_profit * 100).round(2)
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="segment", y="profit_pct", color="profit_pct", text="profit_pct")
    fig.update_traces(texttemplate='%{text:.2f}%')
    fig.update_layout(xaxis_title="Segment", yaxis_title="Profit %")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Consumers contribute 49.52% of total profit, followed by Corporate at 31.79% and Home Office at 18.69%.
            Notably, Corporate places only 3,020 orders but contributes nearly 32% of profit —
            meaning Corporate customers buy higher-value, higher-margin products and deserve dedicated account management.""")

# Q17
elif option == "Q17 - Monthly MoM Revenue Change":
    st.subheader("📉 Q17: Month-over-Month Revenue Change")
    data = df.groupby(['order_year','order_month'])['revenue'].sum().round(2).reset_index()
    data.columns = ['order_year','order_month','revenue']
    data = data.sort_values(['order_year','order_month'])
    data['mom_change'] = data['revenue'].diff().round(2)
    data['period'] = data['order_year'].astype(str) + "-" + data['order_month'].astype(str).str.zfill(2)
    data['order_year'] = data['order_year'].astype(str)
    st.dataframe(data, use_container_width=True)
    fig = px.line(data, x="period", y="mom_change", color="order_year",
                  markers=True, title="Month-over-Month Revenue Change")
    fig.update_layout(xaxis_title="Month", yaxis_title="MoM Change ($)",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Revenue shows a clear zigzag pattern — alternating between positive and negative months.
            October 2022 had the biggest MoM jump. May and September are consistently weak months.
            This seasonal volatility suggests the business needs promotional pushes during dip months.""")

# Q18
elif option == "Q18 - Region with Most Orders per Category":
    st.subheader("🌐 Q18: Region with Most Orders per Category")
    data = df.groupby(['region','category'])['order_id'].count().reset_index()
    data.columns = ['region','category','total_orders']
    data['rank'] = data.groupby('category')['total_orders'].rank(method='dense', ascending=False).astype(int)
    data = data[data['rank'] == 1][['region','category','total_orders']]
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="category", y="total_orders", color="region", text="total_orders")
    fig.update_layout(xaxis_title="Category", yaxis_title="Total Orders")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""The West region leads in Office Supplies with 1,897 orders, making it the busiest region-category combination.
            Office Supplies is the most ordered category across all regions —
            suggesting it's the bread-and-butter product line.""")

# Q19
elif option == "Q19 - Categories where Avg Profit > 100":
    st.subheader("✅ Q19: Categories where Average Profit > 100")
    data = df.groupby('category')['profit'].mean().round(2).reset_index()
    data.columns = ['category','avg_profit']
    data = data[data['avg_profit'] > 100].sort_values('avg_profit', ascending=False)
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="category", y="avg_profit", color="avg_profit", text="avg_profit")
    fig.update_traces(texttemplate='$%{text:,.2f}')
    fig.update_layout(xaxis_title="Category", yaxis_title="Avg Profit",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""Furniture ($161.61) and Technology ($205.59) both cross the average profit of $100,
            while Office Supplies ($52.68) does not qualify.
            Technology leads with the highest average profit per order at $205.59 —
            meaning every Technology order earns more than double a Furniture order.""")

# Q20
elif option == "Q20 - Bottom 5 Loss-Making Products":
    st.subheader("📉 Q20: Bottom 5 Loss-Making Products")
    data = df.groupby('product_id')['profit'].sum().round(2).reset_index()
    data.columns = ['product_id','total_profit']
    data = data.sort_values('total_profit').head(5)
    st.dataframe(data, use_container_width=True)
    fig = px.bar(data, x="product_id", y="total_profit", color="total_profit", text="total_profit")
    fig.update_traces(texttemplate='$%{text:,.2f}')
    fig.update_layout(xaxis_title="Product ID", yaxis_title="Total Profit",
                      yaxis_tickprefix="$", yaxis_tickformat=",.2f")
    st.plotly_chart(fig, use_container_width=True)
    st.info("""OFF-FA-10002280 leads losses at -$48.2. These 5 products are operating at a net loss —
            they cost more than they earn and should be repriced upward or removed from the catalog immediately.""")
