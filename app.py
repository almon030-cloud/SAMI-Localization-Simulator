import streamlit as st
from src.visualizations import create_charts
from src.simulation_engine import recalculate_metrics

# Sidebar
st.sidebar.header("Simulation Controls")
target_localization = st.sidebar.slider("Target Localization %", 20, 100, 51)

# Metrics
current_localization, cost_premium, avg_lead_time = recalculate_metrics(target_localization)
st.title("Saudi Defense Localization Dashboard")
st.metric(label="Current Localization %", value=f"{current_localization}%")
st.metric(label="Cost Premium (SAR)", value=f"{cost_premium:,}")
st.metric(label="Average Lead Time Shift", value=f"{avg_lead_time} days")

# Visualizations
charts = create_charts(target_localization)
for chart in charts:
    st.plotly_chart(chart)