import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def create_charts(target_localization):
    # Chart 1: Donut Chart
    local_spend = target_localization / 100 * 1e9
    intl_spend = 1e9 - local_spend
    donut_chart = go.Figure(data=[
        go.Pie(labels=['Local Spend', 'International Spend'],
               values=[local_spend, intl_spend],
               hole=0.5)
    ])

    # Chart 2: 3D Scatter Plot
    df = pd.DataFrame({
        'Unit Cost': np.random.uniform(100, 1000, 100),
        'Lead Time': np.random.uniform(1, 12, 100),
        'Component': [f"Component {i}" for i in range(100)]
    })
    scatter_plot = px.scatter_3d(df, x='Unit Cost', y='Lead Time', z='Component',
                                  hover_name='Component', title="Unit Cost vs Lead Time")

    # Chart 3: Bar Chart
    original_spend = [500, 300, 200]
    simulated_spend = [x * target_localization / 100 for x in original_spend]
    bar_chart = go.Figure(data=[
        go.Bar(name='Original Spend', x=['Category A', 'Category B', 'Category C'], y=original_spend),
        go.Bar(name='Simulated Spend', x=['Category A', 'Category B', 'Category C'], y=simulated_spend)
    ])
    bar_chart.update_layout(barmode='group')

    # Chart 4: Density Curve
    lead_times = np.random.normal(loc=target_localization / 100 * 6, scale=2, size=1000)
    density_curve = px.histogram(lead_times, nbins=50, histnorm='probability density', title="Lead Time Distribution")

    return [donut_chart, scatter_plot, bar_chart, density_curve]