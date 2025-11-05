import numpy as np
import pandas as pd
import plotly.graph_objects as go


data = [
    {
        "Metal": "Mg",
        "Formula": "MgO",
        "DeltaH_kJmol_solid": -1199.90,
        "DeltaS_JmolK_solid": -212.57,
        "reaction_label_solid": "2Mg(s)+O2(g)→2MgO(s)",
        "Melting_Temp_in_C": 650,
        "DeltaH_kJmol_liquid": -1216.82,
        "DeltaS_JmolK_liquid": -230.90,
        "reaction_label_liquid": "2Mg(l)+O2(g)→2MgO(s)",
        "Does_it_vaporize_below_2500 C": "Yes",
        "Boiling_Temp_in_C": 1090,
        "DeltaH_kJmol_gas": -1494.10,
        "DeltaS_JmolK_gas": -444.60,
        "reaction_label_gas": "2Mg(g)+O2(g)→2MgO(s)"


    },
    {
        "Metal": "Ca",
        "Formula": "CaO",
        "DeltaH_kJmol_solid": -1270.18,
        "DeltaS_JmolK_solid": -211.95,
        "reaction_label_solid": "2Ca(s)+O2(g)→2CaO(s)",
        "Melting_Temp_in_C": 842,
        "DeltaH_kJmol_liquid": -1283.67,
        "DeltaS_JmolK_liquid": -235.79,
        "reaction_label_liquid": "2Ca(l)+O2(g)→2CaO(s)",
        "Does_it_vaporize_below_2500 C": "Yes",
        "Boiling_Temp_in_C": 1484,
        "DeltaH_kJmol_gas": -1625.78,
        "DeltaS_JmolK_gas": -438.55,
        "reaction_label_gas": "2Ca(g)+O2(g)→2CaO(s)"
    }
     # Add yours
]

df = pd.DataFrame(data)


def gibbs(deltaH_kJ, deltaS_JmolK, T):
    return deltaH_kJ - T * (deltaS_JmolK / 1000)


fig = go.Figure()

for _, row in df.iterrows():
    metal = row["Metal"]


    T_solid = np.linspace(298, row["Melting_Temp_in_C"] + 273.15, 100)
    G_solid = gibbs(row["DeltaH_kJmol_solid"], row["DeltaS_JmolK_solid"], T_solid)
    fig.add_trace(go.Scatter(
        x=T_solid, y=G_solid, mode='lines', name=row["reaction_label_solid"], showlegend=False
    ))

    mid_idx = len(T_solid) // 2
    fig.add_annotation(
        x=T_solid[mid_idx],
        y=G_solid[mid_idx] + 20,
        text=row["reaction_label_solid"],
        showarrow=False,
        font=dict(size=5)
    )


    T_liquid = np.linspace(row["Melting_Temp_in_C"] + 273.15, row["Boiling_Temp_in_C"] + 273.15, 100)
    G_liquid = gibbs(row["DeltaH_kJmol_liquid"], row["DeltaS_JmolK_liquid"], T_liquid)
    fig.add_trace(go.Scatter(
        x=T_liquid, y=G_liquid, mode='lines', name=row["reaction_label_liquid"], showlegend=False
    ))
    mid_idx = len(T_liquid) // 2
    fig.add_annotation(
        x=T_liquid[mid_idx],
        y=G_liquid[mid_idx] + 20,
        text=row["reaction_label_liquid"],
        showarrow=False,
        font=dict(size=5)
    )

    if row["Does_it_vaporize_below_2500 C"] == "Yes":
        T_gas = np.linspace(row["Boiling_Temp_in_C"] + 273.15, 2500 + 273.15, 100)
        G_gas = gibbs(row["DeltaH_kJmol_gas"], row["DeltaS_JmolK_gas"], T_gas)
        fig.add_trace(go.Scatter(
            x=T_gas, y=G_gas, mode='lines', name=row["reaction_label_gas"], showlegend=False
        ))
        mid_idx = len(T_gas) // 2
        fig.add_annotation(
            x=T_gas[mid_idx],
            y=G_gas[mid_idx] + 20,
            text=row["reaction_label_gas"],
            showarrow=False,
            font=dict(size=5)
        )


fig.update_layout(
    title="Ellingham Diagram",
    xaxis_title="Temperature (K)",
    yaxis_title="ΔG° (kJ/mol O₂)",
    template="plotly_white"
)

fig.show()
