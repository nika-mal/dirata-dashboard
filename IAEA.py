import pandas as pd
import plotly.graph_objects as go


# --------------------------------
# 1. LOAD DATA
# --------------------------------

df = pd.read_csv("DATA.csv")


# --------------------------------
# 2. COUNT RECORDS PER YEAR
#    AND RELEASE TYPE
# --------------------------------

yearly_counts = (
    df.groupby(["Year", "Release Type"])
      .size()
      .reset_index(name="Records")
)


# --------------------------------
# 3. COLOURS
# --------------------------------

UN_BLUE = "#0055FF"
ATMOSPHERIC_RED = "#191919"

TEXT_GREY = "#202123"
MUTED_GREY = "#6E6E73"
AXIS_GREY = "#D9D9D9"
WHITE = "#FFFFFF"


# --------------------------------
# 4. CREATE FIGURE
# --------------------------------

fig = go.Figure()


# --------------------------------
# 5. LIQUID
# --------------------------------

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


# --------------------------------
# 6. ATMOSPHERIC
# --------------------------------

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
# 7. GENERAL DESIGN
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
        l=70,
        r=40,
        t=130,
        b=70
    ),

    height=600
)


# --------------------------------
# 8. X AXIS
# --------------------------------

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


# --------------------------------
# 9. Y AXIS
# --------------------------------

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
# 10. SHOW
# --------------------------------

fig.show()