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
st.sidebar.image("https://sami.com.sa/assets/images/logo.png", width=200)
st.sidebar.header("🎯 Localization Strategy")

# Baseline target from resume: 51.03%
target_localization = st.sidebar.slider("Target Localization (%)", 20.0, 100.0, 51.03)

st.sidebar.header("🚢 Geopolitical Risk Parameters")
logistics_risk = st.sidebar.select_slider(
    "Red Sea Logistics Environment",
    options=["Stable", "Moderate Congestion", "Crisis / Blockade"],
    value="Stable"
)

st.sidebar.header("🏭 ERP Operations Controls")
num_suppliers = st.sidebar.slider("Number of Active Suppliers", 3, 15, 8)
avg_lead_time = st.sidebar.slider("Avg Supplier Lead Time (Days)", 5, 60, 21)
on_time_rate = st.sidebar.slider("On-Time Delivery Rate (%)", 50, 100, 78)
budget_planned = st.sidebar.slider("Planned Procurement Budget (M SAR)", 10, 200, 85)
budget_actual = st.sidebar.slider("Actual Spend So Far (M SAR)", 5, 200, 72)
inventory_level = st.sidebar.slider("Current Inventory Level (%)", 0, 100, 65)
reorder_point = st.sidebar.slider("Reorder Point (%)", 10, 50, 30)
open_pos = st.sidebar.slider("Open Purchase Orders", 1, 50, 18)

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
np.random.seed(42)  # Keeps the randomness looking professional
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
tab1, tab2, tab3, tab4 = st.tabs(["📊 Executive Summary", "🌪️ Advanced Risk Analytics", "📥 Data Export", "🏭 ERP Operations"])

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
        mode="gauge+number+delta",
        value=current_localization_est,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Localization Completion", 'font': {'size': 24}},
        delta={'reference': 51.03, 'increasing': {'color': "green"}},
        gauge={
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

    # Strategic Analysis Text
    st.markdown("---")
    st.subheader("📝 Strategic Narrative")
    st.info(f"""
    **Current Analysis:** Under {logistics_risk} conditions, the supply chain is experiencing a
    lead time variance of {impacted_lead_time - 8.94:.2f} days beyond the baseline.
    To maintain the **51.03% localization mandate**, SAMI must offset the **{cost_variance/1e6:,.1f}M SAR** logistics premium through accelerated local vendor onboarding.
    """)

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

# ---------- TAB 4: ERP OPERATIONS ----------
with tab4:

    # --- THEME TOGGLE ---
    theme = st.radio("Display Theme", ["🌙 Dark", "☀️ Light"], horizontal=True)
    plot_theme = "plotly_dark" if theme == "🌙 Dark" else "plotly_white"
    text_color = "#ffffff" if theme == "🌙 Dark" else "#000000"

    st.markdown(f"""
        <style>
        .erp-card {{
            background-color: {'#1e2130' if theme == '🌙 Dark' else '#f0f2f6'};
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            color: {text_color};
        }}
        </style>
    """, unsafe_allow_html=True)

    st.subheader("🏭 ERP Operations Dashboard — SAMI Procurement Module")
    st.markdown("Live procurement intelligence across suppliers, inventory, and budget performance.")
    st.markdown("---")

    # --- SECTION 1: KPI ROW ---
    k1, k2, k3, k4 = st.columns(4)
    budget_variance = budget_actual - budget_planned
    inventory_status = "⚠️ Below Reorder" if inventory_level < reorder_point else "✅ Healthy"
    k1.metric("Active Suppliers", num_suppliers, f"{num_suppliers - 8} vs baseline")
    k2.metric("On-Time Delivery", f"{on_time_rate}%", f"{on_time_rate - 80}% vs target")
    k3.metric("Budget Variance", f"{budget_variance:.1f}M SAR", delta_color="inverse")
    k4.metric("Inventory Status", inventory_status)

    st.markdown("---")

    # --- SECTION 2: SUPPLIER SCOREBOARD ---
    st.subheader("📋 Supplier Performance Scoreboard")

    np.random.seed(99)
    supplier_names = [f"Vendor_{i+1:02d}" for i in range(num_suppliers)]
    categories = np.random.choice(["Electronics", "Mechanical", "Raw Materials", "Logistics", "IT Systems"], num_suppliers)
    lead_times = np.random.normal(avg_lead_time, 5, num_suppliers).clip(3, 90).round(1)
    on_times = np.random.normal(on_time_rate, 8, num_suppliers).clip(40, 100).round(1)
    cost_variances = np.random.normal(0, 2.5, num_suppliers).round(2)

    def performance_label(score):
        if score >= 85: return "🟢 High"
        elif score >= 65: return "🟡 Medium"
        else: return "🔴 Low"

    df_suppliers = pd.DataFrame({
        "Supplier": supplier_names,
        "Category": categories,
        "Lead Time (Days)": lead_times,
        "On-Time Rate (%)": on_times,
        "Cost Variance (M SAR)": cost_variances,
        "Performance": [performance_label(s) for s in on_times]
    })

    st.dataframe(df_suppliers, use_container_width=True)

    fig_supplier = px.bar(
        df_suppliers,
        x="Supplier",
        y="On-Time Rate (%)",
        color="Performance",
        color_discrete_map={"🟢 High": "green", "🟡 Medium": "orange", "🔴 Low": "red"},
        title="Supplier On-Time Delivery Performance",
        template=plot_theme
    )
    fig_supplier.add_hline(y=on_time_rate, line_dash="dash",
                           line_color="white" if theme == "🌙 Dark" else "black",
                           annotation_text="Target Rate")
    st.plotly_chart(fig_supplier, use_container_width=True)

    st.markdown("---")

    # --- SECTION 3: PURCHASE ORDER TRACKER ---
    st.subheader("📦 Purchase Order Pipeline")

    po_statuses = ["Pending", "Approved", "In Transit", "Delivered", "Delayed"]
    po_weights = [0.2, 0.25, 0.2, 0.25, 0.1]
    po_data = {
        "PO Number": [f"PO-{2026000 + i}" for i in range(open_pos)],
        "Item Category": np.random.choice(["Electronics", "Mechanical", "IT Systems", "Raw Materials"], open_pos),
        "Quantity (Units)": np.random.randint(10, 500, open_pos),
        "Value (M SAR)": np.round(np.random.uniform(0.5, 8.0, open_pos), 2),
        "Status": np.random.choice(po_statuses, open_pos, p=po_weights),
        "Lead Time (Days)": np.random.randint(5, avg_lead_time + 15, open_pos)
    }
    df_po = pd.DataFrame(po_data)

    status_counts = df_po["Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]

    fig_po = px.pie(
        status_counts,
        names="Status",
        values="Count",
        title="Purchase Order Status Breakdown",
        template=plot_theme,
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_po.update_traces(textposition='inside', textinfo='percent+label')

    col_po1, col_po2 = st.columns([1, 1])
    with col_po1:
        st.plotly_chart(fig_po, use_container_width=True)
    with col_po2:
        st.dataframe(df_po.head(8), use_container_width=True)
        st.caption(f"Showing 8 of {open_pos} open purchase orders")

    delayed = df_po[df_po["Status"] == "Delayed"]
    if len(delayed) > 0:
        st.warning(f"⚠️ {len(delayed)} Purchase Orders are currently **Delayed** — review supplier performance immediately.")

    st.markdown("---")

    # --- SECTION 4: INVENTORY HEALTH ---
    st.subheader("🏗️ Inventory Health Monitor")

    inv_categories = ["Electronics", "Mechanical Parts", "Raw Materials", "IT Components", "Logistics Equipment"]
    inv_levels = np.random.normal(inventory_level, 12, len(inv_categories)).clip(0, 100).round(1)
    reorder_points = [reorder_point] * len(inv_categories)
    days_supply = (inv_levels / 100 * avg_lead_time * 1.5).round(1)

    df_inv = pd.DataFrame({
        "Category": inv_categories,
        "Stock Level (%)": inv_levels,
        "Reorder Point (%)": reorder_points,
        "Days of Supply": days_supply,
        "Status": ["⚠️ Reorder Now" if l < reorder_point else "✅ OK" for l in inv_levels]
    })

    fig_inv = go.Figure()
    fig_inv.add_trace(go.Bar(
        name="Stock Level",
        x=df_inv["Category"],
        y=df_inv["Stock Level (%)"],
        marker_color=["red" if l < reorder_point else "green" for l in inv_levels]
    ))
    fig_inv.add_trace(go.Scatter(
        name="Reorder Point",
        x=df_inv["Category"],
        y=df_inv["Reorder Point (%)"],
        mode="lines+markers",
        line=dict(color="orange", dash="dash", width=2)
    ))
    fig_inv.update_layout(
        title="Inventory Level vs Reorder Point by Category",
        template=plot_theme,
        barmode="group"
    )
    st.plotly_chart(fig_inv, use_container_width=True)
    st.dataframe(df_inv, use_container_width=True)

    st.markdown("---")

    # --- SECTION 5: BUDGET VS ACTUAL ---
    st.subheader("💰 Budget vs Actual Spend Analysis")

    months = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
    monthly_planned = np.round(np.random.uniform(8, 18, 6), 1)
    monthly_actual = np.round(monthly_planned * np.random.uniform(0.8, 1.2, 6), 1)

    df_budget = pd.DataFrame({
        "Month": months,
        "Planned (M SAR)": monthly_planned,
        "Actual (M SAR)": monthly_actual,
        "Variance (M SAR)": np.round(monthly_actual - monthly_planned, 1)
    })

    fig_budget = go.Figure()
    fig_budget.add_trace(go.Bar(name="Planned", x=months, y=monthly_planned, marker_color="steelblue"))
    fig_budget.add_trace(go.Bar(name="Actual", x=months, y=monthly_actual,
                                marker_color=["red" if a > p else "green" for a, p in zip(monthly_actual, monthly_planned)]))
    fig_budget.update_layout(
        title="Monthly Procurement Budget vs Actual Spend",
        template=plot_theme,
        barmode="group",
        yaxis_title="Million SAR"
    )
    st.plotly_chart(fig_budget, use_container_width=True)

    b1, b2, b3 = st.columns(3)
    b1.metric("Total Planned", f"{budget_planned}M SAR")
    b2.metric("Total Actual", f"{budget_actual}M SAR")
    b3.metric("Overall Variance", f"{budget_variance:+.1f}M SAR",
              delta_color="inverse" if budget_variance > 0 else "normal")

    if budget_variance > 5:
        st.error(f"🚨 Budget overrun of {budget_variance:.1f}M SAR detected. Recommend procurement freeze review.")
    elif budget_variance < -5:
        st.info(f"💡 Budget underspend of {abs(budget_variance):.1f}M SAR — potential reallocation opportunity.")
    else:
        st.success("✅ Procurement spend is within acceptable budget variance range.")

    st.markdown("---")

    # --- EXPORT ---
    st.subheader("📥 Export ERP Intelligence Report")
    erp_export = pd.concat([
        df_suppliers.add_prefix("Supplier_"),
        df_po.add_prefix("PO_").reset_index(drop=True),
    ], axis=1)

    csv_erp = erp_export.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Full ERP Report (CSV)",
        data=csv_erp,
        file_name="SAMI_ERP_Operations_Report.csv",
        mime="text/csv"
    )
