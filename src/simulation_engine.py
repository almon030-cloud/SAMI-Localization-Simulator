import pandas as pd
import numpy as np

def recalculate_metrics(target_localization):
    # Simulate recalculation logic
    current_localization = target_localization
    cost_premium = int((100 - target_localization) * 1e6)
    avg_lead_time = round(12 - (target_localization / 100 * 6), 2)
    return current_localization, cost_premium, avg_lead_time