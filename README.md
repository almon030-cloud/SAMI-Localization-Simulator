# Supply Chain Localization Simulator: Vision 2030 Strategic Model

## Executive Overview
This project simulates the strategic shift of manufacturing procurement from international vendors to local Saudi Arabian SMEs, aligned with the **Vision 2030** goal of localizing 50% of defense spending. 

Using a Bill of Materials (BOM) of 100 components, this Python-based model identifies high-impact international contracts and calculates the economic trade-offs of localization.

## Key Results
- **Localization Target Achieved:** 51.03% (from a 25% baseline).
- **Cost Impact:** +3.05% Total Procurement Cost variance (Localization Premium).
- **Operational Benefit:** Average lead time reduction of 0.6 days across the entire system.
- **Strategic Insight:** Identification of the 'Electronics' category as the primary area for future localized supplier development.

## Tech Stack
- **Language:** Python
- **Environment:** Google Colab / Jupyter Notebook
- **Libraries:** Pandas (Data Modeling), Matplotlib & Seaborn (Advanced Visualization), NumPy (Simulation Logic)

## Methodology
The simulator follows a four-stage process:
1. **Synthetic Data Generation:** Creating a realistic BOM with unit costs in SAR, annual volumes, and lead-time variables.
2. **Iterative Optimization:** A logic loop that selects components for localization based on total spend impact until the 50% KPI is met.
3. **Constraint Modeling:** Applying a 12% cost penalty (SME scaling) and a 7-day lead-time benefit to simulate local proximity.
4. **Impact Visualization:** A 2x2 executive dashboard comparing KPIs before and after the strategic shift.

---
*Developed as a strategic exercise for supply chain analytics in the Saudi defense sector.*
