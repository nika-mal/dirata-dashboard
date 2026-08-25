import pandas as pd
import streamlit as st
import plotly.graph_objects as go


# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="DIRATA Dashboard",
    layout="wide"
)


# --------------------------------
# LOAD DATA
# --------------------------------

df = pd.read_csv("DATA.csv")


# --------------------------------
# PREPARE OVERVIEW DATA
# --------------------------------

yearly_counts = (
    df.groupby(["Year", "Release Type"])
      .size()
      .reset_index(name="Records")
)


# --------------------------------
# COLOURS
# --------------------------------

UN_BLUE = "#009EDB"
ATMOSPHERIC_RED = "#D94A4A"

TEXT_GREY = "#202123"
MUTED_GREY = "#6E6E73"
AXIS_GREY = "#D9D9D9"
WHITE = "#FFFFFF"


# --------------------------------
# PAGE TITLE
# --------------------------------

st.title("DIRATA Dashboard")

st.caption(
    "Explore annual records of radionuclide discharges "
    "to the atmosphere and aquatic environment."
)


# --------------------------------
# OVERVIEW GRAPH
# --------------------------------

fig = go.Figure()


# Liquid
liquid = yearly_counts[
    yearly_counts["Release Type"] == "Liquid"
]

fig.add_trace(
    go.Scatter(
        x=liquid["Year"],
        y=liquid["Records"],
        mode="lines+markers",
        name="Liquid",

        line=dict(
            color=UN_BLUE,
            width=2.5
        ),

        marker=dict(
            color=UN_BLUE,
            size=6
        ),

        hovertemplate=(
            "<b>%{x}</b><br>"
            "Liquid<br>"
            "%{y} records"
            "<extra></extra>"
        )
    )
)


# Atmospheric
atmospheric = yearly_counts[
    yearly_counts["Release Type"] == "Atmospheric"
]

fig.add_trace(
    go.Scatter(
        x=atmospheric["Year"],
        y=atmospheric["Records"],
        mode="lines+markers",
        name="Atmospheric",

        line=dict(
            color=ATMOSPHERIC_RED,
            width=2.5
        ),

        marker=dict(
            color=ATMOSPHERIC_RED,
            size=6
        ),

        hovertemplate=(
            "<b>%{x}</b><br>"
            "Atmospheric<br>"
            "%{y} records"
            "<extra></extra>"
        )
    )
)


# --------------------------------
# OVERVIEW GRAPH DESIGN
# --------------------------------

fig.update_layout(

    paper_bgcolor=WHITE,
    plot_bgcolor=WHITE,

    font=dict(
        family="Roboto, Arial, sans-serif",
        size=14,
        color=TEXT_GREY
    ),

    title=dict(
        text=(
            "<b>Annual discharge records</b>"
            "<br>"
            "<span style='font-size:14px;color:#6E6E73'>"
            "Number of DIRATA records by release type"
            "</span>"
        ),
        x=0,
        xanchor="left",
        y=0.96,
        yanchor="top"
    ),

    legend=dict(
        title=None,
        orientation="h",
        x=0,
        xanchor="left",
        y=1.03,
        yanchor="bottom"
    ),

    hovermode="x unified",

    hoverlabel=dict(
        bgcolor=WHITE,
        bordercolor=AXIS_GREY,
        font=dict(
            family="Roboto, Arial, sans-serif",
            size=13,
            color=TEXT_GREY
        )
    ),

    margin=dict(
        l=50,
        r=20,
        t=90,
        b=40
    ),

    height=400
)


fig.update_xaxes(
    title=None,
    showgrid=False,
    zeroline=False,
    showline=True,
    linecolor=AXIS_GREY,
    linewidth=1,

    ticks="outside",
    tickcolor=AXIS_GREY,

    tickfont=dict(
        size=12,
        color=MUTED_GREY
    )
)


fig.update_yaxes(
    title=dict(
        text="Number of records",
        font=dict(
            size=12,
            color=MUTED_GREY
        )
    ),

    showgrid=False,
    zeroline=False,
    showline=False,

    tickfont=dict(
        size=12,
        color=MUTED_GREY
    )
)


# --------------------------------
# SHOW OVERVIEW GRAPH
# --------------------------------

st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

# --------------------------------
# DATA EXPLORER
# --------------------------------

st.subheader("Explore the data")


# --------------------------------
# YEAR FILTER
# --------------------------------

years = sorted(
    df["Year"]
    .dropna()
    .unique()
)

selected_year = st.selectbox(
    "Year",
    years
)

year_data = df[
    df["Year"] == selected_year
]


# --------------------------------
# NUCLIDE FILTER
# --------------------------------

nuclides = sorted(
    year_data["Nuclide Type"]
    .dropna()
    .unique()
)

selected_nuclide = st.selectbox(
    "Nuclide type",
    nuclides
)

nuclide_data = year_data[
    year_data["Nuclide Type"] == selected_nuclide
]


# --------------------------------
# SITE INFORMATION
# --------------------------------

site_count = nuclide_data["Site"].nunique()

st.metric(
    "Sites represented",
    site_count
)


# --------------------------------
# TEMPORARY DATA PREVIEW
# --------------------------------

st.write(
    f"Data for {selected_nuclide} in {selected_year}"
)

st.dataframe(
    nuclide_data[
        [
            "Year",
            "Release Type",
            "Site",
            "Installation",
            "Nuclide Type",
            "Activity"
        ]
    ],
    use_container_width=True
)