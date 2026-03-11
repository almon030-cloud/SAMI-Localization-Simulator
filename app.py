import streamlit as st
import pandas as pd
import numpy as np

# 1. Professional Page Setup
st.set_page_config(page_title="SAMI Localization Simulator", layout="wide")
st.title("🇸🇦 SAMI Defense Localization Digital Twin")
st.subheader("Vision 2030 Strategic Procurement Modeling")
st.markdown("---")

# 2. Sidebar: Strategic Controls
st.sidebar.header("🎯 Localization Strategy")
target_localization = st.sidebar.slider("Target Localization %", 20.0, 100.0, 51.03)

st.sidebar.header("🚢 Global Logistics Risk")
logistics_risk = st.sidebar.select_slider(
    "Stress Test Scenario",
    options=["Stable", "Moderate Congestion", "Red Sea Crisis"],
    value="Stable"
)

# 3. Math Engine (Grounded in your Resume Data)
# Using your 8.94-day lead time reduction and 49M SAR cost variance
risk_multipliers = {"Stable": 1.0, "Moderate Congestion": 1.4, "Red Sea Crisis": 2.8}
multiplier = risk_multipliers[logistics_risk]

# Real-world impact modeling
impacted_lead_time = 8.94 * multiplier 
cost_variance = 49000000 * (multiplier - 1)

# 4. Top KPI Metrics
c1, c2, c3 = st.columns(3)
c1.metric("Current Target", f"{target_localization}%")
c2.metric("Projected Lead Time Shift", f"{impacted_lead_time:.2f} Days", f"{logistics_risk}")
c3.metric("Supply Chain Cost Delta", f"{cost_variance/1e6:,.1f}M SAR", delta_color="inverse")

# 5. Monte Carlo Risk Engine (Stochastic Modeling)
st.markdown("---")
st.subheader("🌪️ Stochastic Localization Probability (1,000 Scenarios)")
st.write("Simulating 1,000 parallel logistics outcomes to stress-test the 51.03% target.")

sim_data = np.random.normal(target_localization, 5 * multiplier, 1000)
df_sim = pd.DataFrame(sim_data, columns=["Localization Probability Density"])

st.line_chart(df_sim)

# 6. Strategic Alert Logic
if logistics_risk == "Red Sea Crisis":
    st.error(f"🚨 **Strategic Alert:** Localization is now a National Security priority. Supply chain lag is costing an additional {cost_variance/1e6:,.1f}M SAR.")
else:
    st.success(f"✅ Logistics environment: {logistics_risk}. Model operating within baseline parameters.")

# 7. Advanced Visualization: Risk Distribution (The Bell Curve)
st.markdown("---")
st.subheader("📊 Strategic Risk Distribution")
st.write("Visualizing the statistical probability of achieving localization targets under current logistics stress.")

import plotly.figure_factory as ff

# Create a distribution plot (Bell Curve) of our 1,000 scenarios
hist_data = [sim_data]
group_labels = ['Localization % Probability']

fig = ff.create_distplot(hist_data, group_labels, bin_size=1, show_rug=False)
fig.update_layout(title_text='Localization Success Probability Density', template='plotly_dark')

# Add a vertical line for the 51.03% Resume Target
fig.add_vline(x=51.03, line_dash="dash", line_color="green", annotation_text="Vision 2030 Benchmark (51.03%)")

st.plotly_chart(fig, use_container_width=True)

# 8. Executive Decision Matrix
st.subheader("💡 Executive Recommendation")
if impacted_lead_time > 15:
    st.warning(f"⚠️ **Critical Threshold Breached:** Lead time of {impacted_lead_time:.1f} days exceeds strategic buffer. Immediate local inventory ramp-up required.")
else:
    st.success(f"✅ **Safe Harbor:** Current supply chain metrics support the 2030 localization trajectory.")
