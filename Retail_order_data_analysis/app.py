import streamlit as st
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Retail Order Analysis",layout='wide')
st.title("Retail order data analysis")

#DataBase connection

def get_connection():
    conn=pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};" 
    "SERVER=Agamagizhan;"
    "DATABASE=retail_order;"
    "Trusted_Connection=yes;")
    return conn

def run_query(query):
    
    conn = get_connection()

    try:
        df = pd.read_sql(query, conn)
        return df

    finally:
        conn.close()

st.sidebar.title("Select Report")
option=st.sidebar.selectbox("Choose a Query", 
    [ "Q1  - Top 10 Revenue Products",
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
    "Q20 - Bottom 5 Loss-Making Products",])

if option=="Q1  - Top 10 Revenue Products":
    st.subheader("Q1- Top 10 Highest Revenue generating products")
    data = run_query("""
    SELECT TOP 10 
    product_id,
    round(SUM(revenue),2) as total_revenue
    FROM retail_order
    GROUP BY product_id
    ORDER BY total_revenue DESC
    """)

    st.subheader("Top 10 Revenue Products")

    st.dataframe(data)
    fig=px.bar(data,x="product_id",y="total_revenue",color="total_revenue",text='total_revenue')
    fig.update_layout(
    xaxis_title="Product ID",
    yaxis_title="Total Revenue"
    )

    st.plotly_chart(fig,use_container_width=True)
    st.info("""TEC-CO-10004722 is the revenue king at $2,45,056 — nearly 1.5x more than the second-best product. 
            7 out of the top 10 products belong to Technology and Office Supplies (Binders), confirming these segments drive the most sales value in the business.""")

if option=="Q2  - Top 5 Cities by Profit Margin":
    st.subheader("Q2  - Top 5 Cities by Profit Margin")
    data = run_query("""
    SELECT TOP 5 
    city,
    ROUND((SUM(profit)/NULLIF(SUM(revenue),0))*100,2) AS profit_margin
    FROM retail_order
    GROUP BY city
    ORDER BY profit_margin DESC;
    """)

    st.subheader("Top 5 Cities by Profit Margin")

    st.dataframe(data)
    fig=px.bar(data,x="city",y="profit_margin",color="profit_margin",text='profit_margin')
    fig.update_layout(
    xaxis_title="Product ID",
    yaxis_title="Profit Margin"
    )

    st.plotly_chart(fig,use_container_width=True)
    st.info("""Insight: Danbury and Goldsboro share the highest profit margin at 29.82%, followed by Bozeman (25.02%), Rogers (23.47%), and Owensboro (22.87%). 
            These cities are the most efficient markets — small in order volume but extremely profitable per sale.""")
    

if option=="Q3  - Total Discount per Category":
    st.subheader("Q3  - Total Discount per Category")
    data = run_query("""
    SELECT 
	category ,ROUND(SUM(DISCOUNT_AMOUNT),2) AS TOTAL_DISCOUNT
	FROM RETAIL_ORDER 
	GROUP BY category
    """)

    st.subheader("Total Discount per Category")

    st.dataframe(data)
    fig=px.bar(data,x="category",y="TOTAL_DISCOUNT",color="TOTAL_DISCOUNT",text='TOTAL_DISCOUNT')
    fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Total Discount"
    )

    st.plotly_chart(fig,use_container_width=True)
    st.info("""Insight:Technology received the highest total discount , followed by Furniture and Office Supplies . 
    Despite having the most discount given, Technology still leads in profit — showing its strong base pricing absorbs discounts well.""")
   

   
if option=="Q4  - Avg Sale Price per Product Category":
    st.subheader("Q4  - Average Sale Price per Product Category")
    data = run_query("""
    SELECT 
    category,
    ROUND(AVG(sales_price),2) AS average_sale_price
    FROM retail_order
    GROUP BY category;
    """)

    st.subheader("Average Sale Price per Product Category")

    st.dataframe(data)

    fig=px.bar(data,x="category",y="average_sale_price",color="average_sale_price",text='average_sale_price')
    fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Average Sale Price"
    )

    st.plotly_chart(fig,use_container_width=True)
    st.info("""Insight: Technology dominates with an average sale price of 436.86 — 
        nearly 4x that of Office Supplies (115.11). Furniture sits at 337.27. 
        This confirms Technology products are premium-priced, making every sale 
        significantly more valuable.""")

    

if option=="Q5  - Region with Highest Avg Sale Price":
    st.subheader("Q5  - Region with Highest Avg Sale Price")
    data = run_query("""
    SELECT
	TOP 5 region ,ROUND(AVG(sales_price),2) as Highest_average_sales_price 
    FROM retail_order 
    GROUP BY region
    ORDER BY avg(sales_price) DESC
    """)

    st.subheader(" Region with Highest Avg Sale Price")

    st.dataframe(data)
   
    st.metric(label=data['region'][0],value=data['Highest_average_sales_price'][0])
    st.info(""" Insight: The South region leads with the highest average sale price, 
            ahead of East, West, and Central. The South is consistently selling 
            higher-value products, making it the most premium market in the country.""")

if option=="Q6  - Total Profit per Category":
    st.subheader("Q6 - Total Profit per Category")
    data = run_query("""
    
    SELECT 
	category,ROUND(SUM(profit),2) AS Total_Profit
	FROM retail_order
	GROUP BY category
    """)

    st.subheader(" Total Profit per Category")

    st.dataframe(data)
    fig=px.bar(data,x="category",y="Total_Profit",color="Total_Profit",text='Total_Profit')
    fig.update_layout(
    xaxis_title="Category",
    yaxis_title="Total Profit"
    )

    st.plotly_chart(fig,use_container_width=True)
    st.info("""Insight: Technology generates 37% of all profit, followed by Furniture  and Office Supplies .
             Profits are fairly well distributed, but Technology has a clear edge — worth investing more in this category.""")

    

if option=="Q7  - Top 3 Segments by Orders":
    st.subheader("Q7  - Top 3 Segments by Orders")
    data = run_query("""
    
   SELECT 
	TOP 3 COUNT(order_id) AS Total_orders, segment 
	FROM retail_order
	GROUP BY SEGMENT
	ORDER BY COUNT(order_id) DESC
    """)

    st.subheader(" Top 3 Segments by Orders")

    st.dataframe(data)
    fig=px.bar(data,x="segment",y="Total_orders",color="Total_orders",text='Total_orders')
    fig.update_layout(
    xaxis_title="Segments",
    yaxis_title="Total orders"
    )

    st.plotly_chart(fig,use_container_width=True)
    st.info("""insight: Consumers place 5,191 orders (52% of all orders), followed by Corporate (3,020) and Home Office (1,783).
             The Consumer segment is by far the most active — marketing and loyalty programs should primarily target this group.""")


if option=="Q8  - Avg Discount % per Region":
    st.subheader("Q8  - Avg Discount % per Region")
    data = run_query("""
    
    SELECT 
	region as Region ,AVG(discount_percent) as Discount_percentage
	FROM retail_order
	GROUP BY region
    """)

    st.subheader(" Avg Discount % per Region")

    st.dataframe(data)

    fig=px.bar(data,x="Region",y="Discount_percentage",color="Discount_percentage",text='Discount_percentage')
    fig.update_layout(
    xaxis_title="Region",
    yaxis_title="Discount_percentage"
    )

    st.plotly_chart(fig,use_container_width=True)
    st.info("""insight: All four regions have almost identical average discounts — between 3.47% and 3.49%. This means discounting is applied uniformly across the country with no region-specific strategy. 
            There's a clear opportunity to use targeted discounting to boost underperforming regions like Central.""")

    
if option=="Q9  - Category with Highest Total Profit":
    st.subheader("Q9  - Category with Highest Total Profit")
    data = run_query("""
    
    SELECT
	TOP 1 Category ,round(sum(profit),2) as Total_profit FROM retail_order
	GROUP BY category
	ORDER BY sum(profit) DESC
    """)

    st.subheader("Category with Highest Total Profit")

    st.dataframe(data)

    st.metric(label=data['Category'][0],value=data["Total_profit"][0])
    st.info("""Insight: Technology is the most profitable category""")

if option=="Q10 - Total Revenue per Year":
    st.subheader("Q10 - Total Revenue per Year")
    data = run_query("""
    
    
    SELECT 
	Order_year as year , ROUND(SUM(revenue),2)  as Total_revenue
	FROM retail_order 
	GROUP BY order_year
    ORDER BY order_year
    """)

    st.subheader("Total Revenue per Year")
    
    st.dataframe(data)


    data['year'] = data['year'].astype(str)

    year_data = data.groupby("year")["Total_revenue"].sum().reset_index()

    fig = px.line(
        year_data,
        x="year",
        y="Total_revenue",
        markers=True,
        title="Yearly Revenue Trend"
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Total Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.info("""The business is stable but needs stronger strategies to accelerate revenue expansion.""")

if option == "Q11 - YoY Sales Growth per Category":
    st.subheader("Q11 - YoY Sales Growth per Category")
    data = run_query("""
    SELECT 
        category,
        YEAR(order_date) AS year,
        ROUND(
            (SUM(revenue) - LAG(SUM(revenue)) OVER(PARTITION BY category ORDER BY YEAR(order_date)))
            * 100.0 /
            LAG(SUM(revenue)) OVER(PARTITION BY category ORDER BY YEAR(order_date)), 2
        ) AS yoy_sales
    FROM retail_order
    GROUP BY category, YEAR(order_date)
    ORDER BY category, year
    """)

    st.dataframe(data, use_container_width=True)

    # ✅ Drop None/NULL rows before plotting
    chart_data = data.dropna(subset=['yoy_sales'])
    chart_data['year'] = chart_data['year'].astype(str)

    fig = px.bar(
        chart_data,
        x="category",
        y="yoy_sales",
        color="category",
        text="yoy_sales",
        title="YoY Sales Growth % by Category (2023 vs 2022)"
    )
    fig.update_layout(xaxis_title="Category", yaxis_title="YoY Growth %")
    st.plotly_chart(fig, use_container_width=True)

    st.info("""Insight: Technology showed the strongest growth at +7.31%, followed by 
            Office Supplies at +6.83%. However, Furniture declined by -6.43% — 
            a significant warning sign that needs urgent attention in product mix or pricing strategy.""")
    
if option== "Q12 - Month with Highest Sales":
    st.subheader( "Q12 - Month with Highest Sales")
    data = run_query("""
    
    
    SELECT TOP 1
         DATENAME(MONTH, order_date) AS month_name,
         ROUND(SUM(sales_price),2) AS total_sales
    FROM retail_order
        GROUP BY 
        DATENAME(MONTH, order_date),
        MONTH(order_date)
        ORDER BY 
        SUM(sales_price) DESC
    """)

    st.subheader(" Month with Highest Sales")
    
    st.dataframe(data)

        
    st.metric(label=data['month_name'][0], value=f"${data['total_sales'][0]:,.2f}")
    st.info("""Insight: October is the peak sales month with $2,39,974 in revenue — 
        the highest of any month. This reflects year-end budget spending by Corporate 
        buyers and early holiday demand. Inventory and staffing should be ramped up 
        by September to handle the surge.""")
    
if option== "Q13 - Top 5 Sub-Categories by Profit Margin":
    st.subheader( "Q13 - Top 5 Sub-Categories by Profit Margin")
    data = run_query("""
    SELECT TOP 5
    sub_category,
    ROUND(SUM(profit) * 100.0 / NULLIF(SUM(revenue),0),2) AS profit_margin
FROM retail_order
GROUP BY sub_category
ORDER BY profit_margin DESC
    """)

    st.subheader("Top 5 Sub-Categories by Profit Margin")
    
    st.dataframe(data)
    fig=px.bar(data,x="sub_category",y="profit_margin",color="profit_margin",text="profit_margin")
    fig.update_layout(xaxis_title="Sub_Category",yaxis_title="Profit_Margin")
    st.plotly_chart(fig,use_container_width=True)
    st.info("""Insight: Copiers lead with a 10.91% margin, followed by Machines (10.36%), Appliances (10.33%), Binders (10.12%), and Chairs (9.59%).
             All top margin sub-categories are high-ticket Technology and Furniture items — reinforcing the value of focusing on premium product lines.""")

        
    

if option== "Q14 - Products with Discount > 20%":
    st.subheader( "Q14 - Products with Discount > 20%")
    data = run_query("""
    SELECT product_id, 
       
       ROUND(SUM(discount_percent), 2) AS total_discount_given
FROM retail_order
WHERE discount_percent > 20
GROUP BY product_id, discount_percent
ORDER BY total_discount_given DESC;
    """)

    st.subheader("Products with Discount > 20%")
    if data.empty:
        st.info("No products have a discount greater than 20%.")
    else:
        fig = px.bar(data, x="product_id", y="total_discount_given",
                 color="total_discount_given", text="total_discount_given")
        fig.update_layout(xaxis_title="Product ID", yaxis_title="Total Discount")
        st.plotly_chart(fig, use_container_width=True)

    st.info("""Insight:No products in this dataset have a discount greater than 20%.
             The maximum discount applied is well below this threshold, meaning the business maintains disciplined pricing and avoids aggressive markdowns that could erode margins.""")
    
    

if option== "Q15 - Rank Products by Revenue in Category":
    st.subheader("Q15 - Rank Products by Revenue in Category")
    data = run_query("""
   SELECT category, product_id,
       ROUND(SUM(sales_price), 2) AS revenue,
       RANK() OVER (PARTITION BY category ORDER BY SUM(sales_price) DESC) AS rank
    FROM retail_order
    GROUP BY category, product_id;
    """)

    st.subheader("Rank Products by Revenue in Category")
    st.dataframe(data)
    

if option== "Q16 - Segment-wise Profit Contribution %":
    st.subheader("Q16 - Segment-wise Profit Contribution %")
    data = run_query("""
 SELECT segment,
       ROUND(SUM(profit), 2) AS segment_profit,
       ROUND(SUM(profit) / (SELECT SUM(profit) FROM retail_order) * 100, 2) AS profit_pct
FROM retail_order
GROUP BY segment;
    """)

    st.subheader(" Segment-wise Profit Contribution %")
    st.dataframe(data)
    fig=px.bar(data,x="segment",y="profit_pct",color="profit_pct",text="profit_pct")
    fig.update_layout(xaxis_title="Segments",yaxis_title="Profit_Percentage")
    st.plotly_chart(fig,use_container_width=True)
    st.info("""Consumers contribute 49.52% of total profit ($5,14,980), followed by Corporate at 31.79% ($3,30,596) and Home Office at 18.69% ($1,94,352). 
            Notably, Corporate places only 3,020 orders but contributes nearly 32% of profit — meaning Corporate customers buy higher-value,
             higher-margin products and deserve dedicated account management.""")
    

if option == "Q17 - Monthly MoM Revenue Change":
    st.subheader("Q17 - MoM Revenue Change")
    data = run_query("""
        SELECT 
            order_year, 
            order_month,
            ROUND(SUM(sales_price), 2) AS revenue,
            ROUND(SUM(sales_price) - LAG(SUM(sales_price)) 
                  OVER (ORDER BY order_year, order_month), 2) AS mom_change
        FROM retail_order
        GROUP BY order_year, order_month
        ORDER BY order_year, order_month
    """)

    # ✅ Create period column
    data["period"] = data["order_year"].astype(str) + "-" + data["order_month"].astype(str).str.zfill(2)
    
    # ✅ Convert year to string so Plotly treats as category
    data["order_year"] = data["order_year"].astype(str)

    st.dataframe(data, use_container_width=True)

    fig = px.line(
        data,
        x="period",
        y="mom_change",
        color="order_year",        # ✅ now shows 2 separate colored lines
        markers=True,
        title="Month-over-Month Revenue Change"
    )
    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="MoM Change ($)",
        yaxis_tickprefix="$",
        yaxis_tickformat=",.2f"    # ✅ currency format on y-axis
    )
    fig.update_traces(texttemplate='$%{y:,.2f}')

    st.plotly_chart(fig, use_container_width=True)

    st.info("""Insight: Revenue shows a clear zigzag pattern — alternating between 
            positive and negative months. October 2022 had the biggest MoM jump at 
            +$39,770. May and September are consistently weak months with steep drops. 
            This seasonal volatility suggests the business needs promotional pushes 
            during dip months to stabilize revenue.""")

if option== "Q18 - Region with Most Orders per Category":
    st.subheader("Q18 - Region with Most Orders per Category")
    data = run_query("""
 SELECT region,
        category,
        total_orders
FROM (
    SELECT 
        region,
        category,
        COUNT(order_id) AS total_orders,
        RANK() OVER(
            PARTITION BY category
            ORDER BY COUNT(order_id) DESC
        ) AS rank
    FROM retail_order
    GROUP BY region, category
) t
WHERE rank = 1;""")

    st.subheader("Region with Most Orders per Category")
    
    st.dataframe(data, use_container_width=True)

    if not data.empty:

        fig = px.bar(
            data,
            x="category",
            y="total_orders",
            color="region",
            text="total_orders",
            )

        st.plotly_chart(fig, use_container_width=True)
    st.info("""The West region leads in Office Supplies with 1,897 orders, making it the single busiest region-category combination in the entire dataset.
             East follows with 1,712 Office Supplies orders. 
            Office Supplies is the most ordered category across all regions — suggesting it's the bread-and-butter product line.""")

if option== "Q19 - Categories where Avg Profit > 100":
    st.subheader("Q19 - Categories where Avg Profit > 100")
    data = run_query("""
SELECT 
    category,
    ROUND(AVG(profit), 2) AS avg_profit
FROM retail_order
GROUP BY category
HAVING ROUND(AVG(profit), 2) > 100;
""")

    st.subheader("Categories where Avg Profit > 100")
    
    st.dataframe(data, use_container_width=True)
    fig=px.bar(data,x='category',y='avg_profit',color='avg_profit',text='avg_profit')
    fig.update_layout(xaxis_title='Category',yaxis_title="Average Profit")
    st.plotly_chart(fig,use_container_width=True)
    st.info("""Furniture ($161.61) and Technology ($205.59) both cross the average profit of $100, while Office Supplies ($52.68) does not qualify. 
            Technology leads with the highest average profit per order at $205.59 — meaning every Technology order earns more than double a Furniture order.
     Office Supplies, despite being the highest volume category, fails to cross the threshold due to low-margin, low-priced items..""")

if option== "Q20 - Bottom 5 Loss-Making Products":
    st.subheader("Q20 - Bottom 5 Loss-Making Products")
    data = run_query("""
SELECT TOP 5
    product_id,
    SUM(profit) AS total_profit
FROM retail_order
GROUP BY product_id
ORDER BY total_profit ASC;;""")

    st.subheader("Bottom 5 Loss-Making Products")
    st.dataframe(data)
    fig=px.bar(data,x='product_id',y="total_profit",color="total_profit",text="total_profit")
    fig.update_layout(xaxis_title="Product_id",yaxis_title="Total_Profit")
    st.plotly_chart(fig,use_container_width=True)
    st.info("""OFF-FA-10002280 leads losses at -$48.2, replacing the earlier list which had much smaller losses (-$9 range).""")





        

     




    