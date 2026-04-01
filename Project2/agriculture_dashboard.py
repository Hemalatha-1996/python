import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Agricultural EDA Dashboard",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
#  LOAD DATA  — place cleaned_dataset.csv in the same folder
# ============================================================
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_dataset.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

COLORS = [
    "#2a7f8f", "#d4853a", "#4a7c59", "#b85c38",
    "#5b8db8", "#8b5e3c", "#4ab3c5", "#c9a84c",
    "#a05c6b", "#6b7fa3",
]

# ============================================================
#  SIDEBAR FILTERS
# ============================================================
with st.sidebar:
    st.title("🌾 Agricultural EDA")
    st.markdown("---")

    all_states = sorted(df["state_name"].unique())
    selected_states = st.multiselect(
        "Filter by State",
        all_states,
        default=all_states,
    )

    year_min = int(df["year"].min())
    year_max = int(df["year"].max())
    year_range = st.slider(
        "Year Range",
        year_min, year_max,
        (year_min, year_max),
    )

    st.markdown("---")
    st.caption(
        f"Dataset: {df.shape[0]:,} rows\n"
        f"States : {df['state_name'].nunique()}\n"
        f"Districts: {df['dist_name'].nunique()}\n"
        f"Years  : {year_min} – {year_max}"
    )

# ============================================================
#  APPLY FILTERS
# ============================================================
fdf = df.copy()
if selected_states:
    fdf = fdf[fdf["state_name"].isin(selected_states)]
fdf = fdf[(fdf["year"] >= year_range[0]) & (fdf["year"] <= year_range[1])]

# ============================================================
#  TITLE
# ============================================================
st.title("🌾 Explorative Data Analysis — Agricultural India")
st.caption(
    f"Showing {fdf.shape[0]:,} records  |  "
    f"{fdf['state_name'].nunique()} states  |  "
    f"{fdf['dist_name'].nunique()} districts  |  "
    f"Years {year_range[0]}–{year_range[1]}"
)
st.markdown("---")

# ============================================================
#  KPI METRICS
# ============================================================
k1, k2, k3, k4, k5, k6 = st.columns(6)

k1.metric(
    "🍚 Rice Production",
    f"{fdf['rice_production_(1000_tons)'].sum()/1000:,.1f} M tons",
)
k2.metric(
    "🌾 Wheat Production",
    f"{fdf['wheat_production_(1000_tons)'].sum()/1000:,.1f} M tons",
)
k3.metric(
    "🌽 Maize Production",
    f"{fdf['maize_production_(1000_tons)'].sum()/1000:,.1f} M tons",
)
k4.metric(
    "🫒 Oilseed Production",
    f"{fdf['oilseeds_production_(1000_tons)'].sum()/1000:,.1f} M tons",
)
k5.metric(
    "🍚 Avg Rice Yield",
    f"{fdf['rice_yield_(kg_per_ha)'].mean():,.0f} kg/ha",
)
k6.metric(
    "🌾 Avg Wheat Yield",
    f"{fdf['wheat_yield_(kg_per_ha)'].mean():,.0f} kg/ha",
)

st.markdown("---")

# ============================================================
#  SECTION 1 — RICE PRODUCTION
# ============================================================
st.subheader("🍚 Rice Production Analysis")

col1, col2, col3 = st.columns([2, 1.5, 1.2])

with col1:
    top3_rice_states = (
        fdf.groupby("state_name")["rice_production_(1000_tons)"]
        .sum().nlargest(3).index.tolist()
    )
    rice_yr = (
        fdf[fdf["state_name"].isin(top3_rice_states)]
        .groupby(["year", "state_name"])["rice_production_(1000_tons)"]
        .sum().reset_index()
    )
    fig1 = px.bar(
        rice_yr,
        x="year",
        y="rice_production_(1000_tons)",
        color="state_name",
        barmode="group",
        title="Year-wise Rice Production — Top 3 States",
        labels={
            "rice_production_(1000_tons)": "Production (1000 tons)",
            "year": "Year",
            "state_name": "State",
        },
        color_discrete_sequence=COLORS,
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    rice_trend = (
        fdf.groupby("year")["rice_production_(1000_tons)"]
        .sum().reset_index()
    )
    fig2 = px.area(
        rice_trend,
        x="year",
        y="rice_production_(1000_tons)",
        title="Overall Rice Production Trend",
        labels={
            "rice_production_(1000_tons)": "Production (1000 tons)",
            "year": "Year",
        },
        color_discrete_sequence=[COLORS[0]],
    )
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    rice_share = (
        fdf.groupby("state_name")["rice_production_(1000_tons)"]
        .sum().nlargest(6).reset_index()
    )
    fig3 = px.pie(
        rice_share,
        names="state_name",
        values="rice_production_(1000_tons)",
        title="Rice Share by State",
        hole=0.5,
        color_discrete_sequence=COLORS,
    )
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# ============================================================
#  SECTION 2 — WHEAT ANALYSIS
# ============================================================
st.subheader("🌾 Wheat Analysis")

c1, c2, c3 = st.columns([1.2, 2, 1.2])

with c1:
    wheat_yield_state = (
        fdf.groupby("state_name")["wheat_yield_(kg_per_ha)"]
        .mean().nlargest(10).reset_index()
    )
    fig4 = px.bar(
        wheat_yield_state,
        x="wheat_yield_(kg_per_ha)",
        y="state_name",
        orientation="h",
        title="Avg Wheat Yield by State",
        labels={
            "wheat_yield_(kg_per_ha)": "Yield (kg/ha)",
            "state_name": "",
        },
        color="wheat_yield_(kg_per_ha)",
        color_continuous_scale="teal",
    )
    fig4.update_coloraxes(showscale=False)
    st.plotly_chart(fig4, use_container_width=True)

with c2:
    top5_wheat_states = (
        fdf.groupby("state_name")["wheat_production_(1000_tons)"]
        .sum().nlargest(5).index.tolist()
    )
    wheat_yield_trend = (
        fdf[fdf["state_name"].isin(top5_wheat_states)]
        .groupby(["year", "state_name"])["wheat_yield_(kg_per_ha)"]
        .mean().reset_index()
    )
    fig5 = px.line(
        wheat_yield_trend,
        x="year",
        y="wheat_yield_(kg_per_ha)",
        color="state_name",
        markers=True,
        title="Wheat Yield Trend — Top 5 States",
        labels={
            "wheat_yield_(kg_per_ha)": "Yield (kg/ha)",
            "year": "Year",
            "state_name": "State",
        },
        color_discrete_sequence=COLORS,
    )
    st.plotly_chart(fig5, use_container_width=True)

with c3:
    wheat_share = (
        fdf.groupby("state_name")["wheat_production_(1000_tons)"]
        .sum().nlargest(6).reset_index()
    )
    fig6 = px.pie(
        wheat_share,
        names="state_name",
        values="wheat_production_(1000_tons)",
        title="Wheat Share by State",
        hole=0.5,
        color_discrete_sequence=COLORS[1:],
    )
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

# ============================================================
#  SECTION 3 — WHEAT vs RICE (Top 5 States, Last 10 Years)
# ============================================================
st.subheader("📊 Wheat vs Rice — Top 5 States Over 10 Years")

top5_combined = (
    fdf.groupby("state_name")
    .apply(
        lambda x:
            x["rice_production_(1000_tons)"].sum() +
            x["wheat_production_(1000_tons)"].sum()
    )
    .nlargest(5).index.tolist()
)
last10_start = fdf["year"].max() - 9
comp = (
    fdf[
        fdf["state_name"].isin(top5_combined) &
        (fdf["year"] >= last10_start)
    ]
    .groupby(["year", "state_name"])
    .agg(
        Rice=("rice_production_(1000_tons)",  "sum"),
        Wheat=("wheat_production_(1000_tons)", "sum"),
    )
    .reset_index()
)
comp_melted = comp.melt(
    id_vars=["year", "state_name"],
    value_vars=["Rice", "Wheat"],
    var_name="Crop",
    value_name="Production (1000 tons)",
)
fig7 = px.bar(
    comp_melted,
    x="year",
    y="Production (1000 tons)",
    color="Crop",
    barmode="group",
    facet_col="state_name",
    facet_col_wrap=3,
    title="Rice vs Wheat Production — Top 5 States (Last 10 Years)",
    color_discrete_map={"Rice": COLORS[0], "Wheat": COLORS[1]},
    labels={"year": "Year"},
)
fig7.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
st.plotly_chart(fig7, use_container_width=True)

st.markdown("---")

# ============================================================
#  SECTION 4 — MAIZE & COTTON
# ============================================================
st.subheader("🌽 Maize & Cotton Production")

c1, c2, c3 = st.columns([2, 1.2, 1.5])

with c1:
    top5_maize = (
        fdf.groupby("state_name")["maize_production_(1000_tons)"]
        .sum().nlargest(5).index.tolist()
    )
    maize_yr = (
        fdf[fdf["state_name"].isin(top5_maize)]
        .groupby(["year", "state_name"])["maize_production_(1000_tons)"]
        .sum().reset_index()
    )
    fig8 = px.area(
        maize_yr,
        x="year",
        y="maize_production_(1000_tons)",
        color="state_name",
        title="Maize Production — Top 5 States",
        labels={
            "maize_production_(1000_tons)": "Production (1000 tons)",
            "year": "Year",
            "state_name": "State",
        },
        color_discrete_sequence=COLORS,
    )
    st.plotly_chart(fig8, use_container_width=True)

with c2:
    maize_share = (
        fdf.groupby("state_name")["maize_production_(1000_tons)"]
        .sum().nlargest(6).reset_index()
    )
    fig9 = px.pie(
        maize_share,
        names="state_name",
        values="maize_production_(1000_tons)",
        title="Maize Share by State",
        hole=0.5,
        color_discrete_sequence=COLORS,
    )
    st.plotly_chart(fig9, use_container_width=True)

with c3:
    top5_cotton = (
        fdf.groupby("state_name")["cotton_production_(1000_tons)"]
        .sum().nlargest(5).index.tolist()
    )
    cotton_yr = (
        fdf[fdf["state_name"].isin(top5_cotton)]
        .groupby(["year", "state_name"])["cotton_production_(1000_tons)"]
        .sum().reset_index()
    )
    fig10 = px.line(
        cotton_yr,
        x="year",
        y="cotton_production_(1000_tons)",
        color="state_name",
        markers=True,
        title="Cotton Production — Top 5 States",
        labels={
            "cotton_production_(1000_tons)": "Production (1000 tons)",
            "year": "Year",
            "state_name": "State",
        },
        color_discrete_sequence=COLORS,
    )
    st.plotly_chart(fig10, use_container_width=True)

st.markdown("---")

# ============================================================
#  SECTION 5 — OILSEEDS, GROUNDNUT & MAIZE YIELD
# ============================================================
st.subheader("🫒 Oilseeds, Groundnut & Maize Yield")

c1, c2, c3 = st.columns(3)

with c1:
    oilseed_state = (
        fdf.groupby("state_name")["oilseeds_area_(1000_ha)"]
        .sum().nlargest(10).reset_index()
    )
    fig11 = px.bar(
        oilseed_state,
        x="state_name",
        y="oilseeds_area_(1000_ha)",
        title="Total Oilseed Area by State",
        labels={
            "oilseeds_area_(1000_ha)": "Area (1000 ha)",
            "state_name": "State",
        },
        color="oilseeds_area_(1000_ha)",
        color_continuous_scale="Oranges",
    )
    fig11.update_coloraxes(showscale=False)
    fig11.update_xaxes(tickangle=40)
    st.plotly_chart(fig11, use_container_width=True)

with c2:
    groundnut_dist = (
        fdf.groupby(["dist_name", "state_name"])["groundnut_production_(1000_tons)"]
        .sum().nlargest(10).reset_index()
    )
    fig12 = px.bar(
        groundnut_dist,
        x="groundnut_production_(1000_tons)",
        y="dist_name",
        orientation="h",
        title="Top 10 Districts — Groundnut Production",
        labels={
            "groundnut_production_(1000_tons)": "Production (1000 tons)",
            "dist_name": "",
        },
        color="groundnut_production_(1000_tons)",
        color_continuous_scale="Reds",
    )
    fig12.update_coloraxes(showscale=False)
    st.plotly_chart(fig12, use_container_width=True)

with c3:
    maize_yield_yr = (
        fdf.groupby("year")["maize_yield_(kg_per_ha)"]
        .mean().reset_index()
    )
    fig13 = px.line(
        maize_yield_yr,
        x="year",
        y="maize_yield_(kg_per_ha)",
        markers=True,
        title="Annual Average Maize Yield (All States)",
        labels={
            "maize_yield_(kg_per_ha)": "Yield (kg/ha)",
            "year": "Year",
        },
        color_discrete_sequence=[COLORS[2]],
    )
    fig13.update_traces(line_width=2.5, marker_size=6)
    st.plotly_chart(fig13, use_container_width=True)

st.markdown("---")

# ============================================================
#  SECTION 6 — OILSEED PRODUCTION TREND + GROUNDNUT 2017
# ============================================================
st.subheader("🫒 Oilseed Trend  &  🥜 Groundnut Top Districts (2017)")

c1, c2 = st.columns(2)

with c1:
    oilseed_trend = (
        fdf.groupby("year")["oilseeds_production_(1000_tons)"]
        .sum().reset_index()
    )
    fig14 = px.area(
        oilseed_trend,
        x="year",
        y="oilseeds_production_(1000_tons)",
        title="Total Oilseed Production Over the Years",
        labels={
            "oilseeds_production_(1000_tons)": "Production (1000 tons)",
            "year": "Year",
        },
        color_discrete_sequence=[COLORS[3]],
    )
    st.plotly_chart(fig14, use_container_width=True)

with c2:
    gnd_2017 = (
        df[df["year"] == 2017]
        .groupby(["dist_name", "state_name"])["groundnut_production_(1000_tons)"]
        .sum().nlargest(10).reset_index()
    )
    fig15 = px.bar(
        gnd_2017,
        x="groundnut_production_(1000_tons)",
        y="dist_name",
        orientation="h",
        color="state_name",
        title="Top Districts — Groundnut Production (2017)",
        labels={
            "groundnut_production_(1000_tons)": "Production (1000 tons)",
            "dist_name": "",
            "state_name": "State",
        },
        color_discrete_sequence=COLORS,
    )
    st.plotly_chart(fig15, use_container_width=True)

st.markdown("---")

# ============================================================
#  SECTION 7 — SUGARCANE & PEARL MILLET
# ============================================================
st.subheader("🎋 Sugarcane & Pearl Millet Production")

c1, c2 = st.columns(2)

with c1:
    top5_sugar = (
        fdf.groupby("state_name")["sugarcane_production_(1000_tons)"]
        .sum().nlargest(5).index.tolist()
    )
    sugar_yr = (
        fdf[fdf["state_name"].isin(top5_sugar)]
        .groupby(["year", "state_name"])["sugarcane_production_(1000_tons)"]
        .sum().reset_index()
    )
    fig16 = px.line(
        sugar_yr,
        x="year",
        y="sugarcane_production_(1000_tons)",
        color="state_name",
        markers=False,
        title="Sugarcane Production — Top 5 States",
        labels={
            "sugarcane_production_(1000_tons)": "Production (1000 tons)",
            "year": "Year",
            "state_name": "State",
        },
        color_discrete_sequence=COLORS,
    )
    st.plotly_chart(fig16, use_container_width=True)

with c2:
    top5_millet = (
        fdf.groupby("state_name")["pearl_millet_production_(1000_tons)"]
        .sum().nlargest(5).index.tolist()
    )
    millet_yr = (
        fdf[fdf["state_name"].isin(top5_millet)]
        .groupby(["year", "state_name"])["pearl_millet_production_(1000_tons)"]
        .sum().reset_index()
    )
    fig17 = px.area(
        millet_yr,
        x="year",
        y="pearl_millet_production_(1000_tons)",
        color="state_name",
        title="Pearl Millet Production — Top 5 States",
        labels={
            "pearl_millet_production_(1000_tons)": "Production (1000 tons)",
            "year": "Year",
            "state_name": "State",
        },
        color_discrete_sequence=COLORS,
    )
    st.plotly_chart(fig17, use_container_width=True)

st.markdown("---")

# ============================================================
#  SECTION 8 — RAW DATA TABLE
# ============================================================
with st.expander("📋 View Filtered Raw Data"):
    show_cols = [
        "year", "state_name", "dist_name",
        "rice_production_(1000_tons)",
        "wheat_production_(1000_tons)",
        "maize_production_(1000_tons)",
        "oilseeds_production_(1000_tons)",
        "groundnut_production_(1000_tons)",
        "cotton_production_(1000_tons)",
        "sugarcane_production_(1000_tons)",
        "pearl_millet_production_(1000_tons)",
    ]
    available = [c for c in show_cols if c in fdf.columns]
    st.dataframe(
        fdf[available].sort_values(["year", "state_name"]).reset_index(drop=True),
        use_container_width=True,
        height=340,
    )

st.caption(
    "Agricultural EDA Dashboard  |  Built with Streamlit & Plotly Express  |  "
    "India District-wise Agriculture Statistics 1966–2017"
)
