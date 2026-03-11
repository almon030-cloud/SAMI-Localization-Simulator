import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

# ==========================================
# 1. ENTERPRISE PAGE CONFIGURATION
# ==========================================
st.set_page_config(page_title="SAMI Digital Twin", page_icon="🇸🇦", layout="wide")

st.title("🇸🇦 SAMI Defense Localization Digital Twin")
st.markdown("**Vision 2030 Strategic Procurement & Risk Modeling Engine**")
st.markdown("---")

# ==========================================
# 2. DYNAMIC SIDEBAR CONTROLS
# ==========================================
st.sidebar.image("https://www.vision2030.gov.sa/media/rc0bc5xt/v2030_logo.png", width=200)
st.sidebar.header("🎯 Localization Strategy")

# Baseline target from resume: 51.03%
target_localization = st.sidebar.slider("Target Localization (%)", 20.0, 100.0, 51.03)

st.sidebar.header("🚢 Geopolitical Risk Parameters")
logistics_risk = st.sidebar.select_slider(
    "Red Sea Logistics Environment",
    options=["Stable", "Moderate Congestion", "Crisis / Blockade"],
    value="Stable"
)

# ==========================================
# 3. CORE MATH & LOGIC ENGINE
# ==========================================
# Grounded in real resume metrics: 8.94 days and 49M SAR variance
risk_multipliers = {"Stable": 1.0, "Moderate Congestion": 1.4, "Crisis / Blockade": 2.8}
multiplier = risk_multipliers[logistics_risk]

impacted_lead_time = 8.94 * multiplier 
cost_variance = 49000000 * (multiplier - 1)
current_localization_est = target_localization - (2.5 * (multiplier - 1))

# Generate 1,000 parallel universe scenarios (Monte Carlo)
np.random.seed(42) # Keeps the randomness looking professional
sim_localization = np.random.normal(current_localization_est, 5 * multiplier, 1000)
sim_costs = np.random.normal(cost_variance, 2000000 * multiplier, 1000)

df_sim = pd.DataFrame({
    "Scenario ID": range(1, 1001),
    "Projected Localization (%)": np.round(sim_localization, 2),
    "Cost Variance (SAR)": np.round(sim_costs, 2)
})

# ==========================================
# 4. APP INTERFACE: TABS
# ==========================================
tab1, tab2, tab3 = st.tabs(["📊 Executive Summary", "🌪️ Advanced Risk Analytics", "📥 Data Export"])

# ---------- TAB 1: EXECUTIVE SUMMARY ----------
with tab1:
    st.subheader("Key Performance Indicators")
    
    # KPI Row
    c1, c2, c3 = st.columns(3)
    c1.metric("Projected Localization", f"{current_localization_est:.1f}%", f"{current_localization_est - 51.03:.1f}% vs Target")
    c2.metric("Projected Lead Time Shift", f"{impacted_lead_time:.2f} Days", f"{logistics_risk} Impact", delta_color="inverse")
    c3.metric("Supply Chain Cost Delta", f"{cost_variance/1e6:,.1f}M SAR", delta_color="inverse")
    
    st.markdown("---")
    
    # Vision 2030 Speedometer Gauge
    st.subheader("Vision 2030 Mandate Tracker")
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = current_localization_est,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Localization Completion", 'font': {'size': 24}},
        delta = {'reference': 51.03, 'increasing': {'color': "green"}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkgreen"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': 'red'},
                {'range': [30, 50], 'color': 'orange'},
                {'range': [50, 100], 'color': 'lightgreen'}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': 51.03}}))
    fig_gauge.update_layout(height=400, template='plotly_dark')
    st.plotly_chart(fig_gauge, use_container_width=True)

# ---------- TAB 2: RISK ANALYTICS ----------
with tab2:
    st.subheader("Stochastic Risk Distribution (1,000 Scenarios)")
    st.write("Visualizing the statistical probability of achieving localization targets under current logistics stress.")
    
    # The SciPy Bell Curve
    hist_data = [df_sim["Projected Localization (%)"]]
    group_labels = ['Localization % Probability']
    fig_dist = ff.create_distplot(hist_data, group_labels, bin_size=1, show_rug=False)
    fig_dist.update_layout(title_text='Localization Success Probability Density', template='plotly_dark')
    fig_dist.add_vline(x=51.03, line_dash="dash", line_color="green", annotation_text="Vision 2030 Benchmark (51.03%)")
    st.plotly_chart(fig_dist, use_container_width=True)

    # Strategic Alert
    if logistics_risk == "Crisis / Blockade":
        st.error(f"🚨 **Strategic Alert:** Localization is now a National Security priority. Supply chain lag is costing an additional {cost_variance/1e6:,.1f}M SAR.")
    else:
        st.success(f"✅ Logistics environment: {logistics_risk}. Model operating within acceptable risk thresholds.")

# ---------- TAB 3: DATA EXPORT ----------
with tab3:
    st.subheader("Corporate Intelligence Export")
    st.write("Generate the raw Monte Carlo simulation dataset for internal auditing and Ministry reporting.")
    
    st.dataframe(df_sim.head(10), use_container_width=True)
    st.caption("Showing preview: Top 10 scenario outcomes...")
    
    # The CSV Download Button
    csv = df_sim.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Full Simulation Report (CSV)",
        data=csv,
        file_name='SAMI_MonteCarlo_Simulation_Data.csv',
        mime='text/csv',
          )
