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
