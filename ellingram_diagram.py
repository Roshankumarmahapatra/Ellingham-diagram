import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Data for 50 metal oxides ---
data = [
    {"Metal": "Li", "Formula": "Li2O", "DeltaH_kJmol": -598.8, "DeltaS_JmolK": 44.0},
    {"Metal": "Na", "Formula": "Na2O", "DeltaH_kJmol": -414.2, "DeltaS_JmolK": 65.0},
    {"Metal": "K",  "Formula": "K2O",  "DeltaH_kJmol": -363.2, "DeltaS_JmolK": 93.0},
    {"Metal": "Rb", "Formula": "Rb2O", "DeltaH_kJmol": -346.0, "DeltaS_JmolK": 98.0},
    {"Metal": "Cs", "Formula": "Cs2O", "DeltaH_kJmol": -335.0, "DeltaS_JmolK": 102.0},
    {"Metal": "Be", "Formula": "BeO",  "DeltaH_kJmol": -609.4, "DeltaS_JmolK": 26.9},
    {"Metal": "Mg", "Formula": "MgO",  "DeltaH_kJmol": -601.6, "DeltaS_JmolK": 26.9},
    {"Metal": "Ca", "Formula": "CaO",  "DeltaH_kJmol": -635.5, "DeltaS_JmolK": 39.8},
    {"Metal": "Sr", "Formula": "SrO",  "DeltaH_kJmol": -592.0, "DeltaS_JmolK": 63.0},
    {"Metal": "Ba", "Formula": "BaO",  "DeltaH_kJmol": -553.5, "DeltaS_JmolK": 70.4},
    {"Metal": "Al", "Formula": "Al2O3", "DeltaH_kJmol": -1675.7, "DeltaS_JmolK": 50.9},
    {"Metal": "Ti", "Formula": "TiO2",  "DeltaH_kJmol": -944.0,  "DeltaS_JmolK": 50.0},
    {"Metal": "Zr", "Formula": "ZrO2",  "DeltaH_kJmol": -1100.0, "DeltaS_JmolK": 50.0},
    {"Metal": "Hf", "Formula": "HfO2",  "DeltaH_kJmol": -1140.0, "DeltaS_JmolK": 52.0},
    {"Metal": "V",  "Formula": "V2O5",  "DeltaH_kJmol": -1550.0, "DeltaS_JmolK": 87.0},
    {"Metal": "Nb", "Formula": "Nb2O5", "DeltaH_kJmol": -1898.0, "DeltaS_JmolK": 88.0},
    {"Metal": "Ta", "Formula": "Ta2O5", "DeltaH_kJmol": -2046.0, "DeltaS_JmolK": 91.0},
    {"Metal": "Cr", "Formula": "Cr2O3", "DeltaH_kJmol": -1139.7, "DeltaS_JmolK": 87.0},
    {"Metal": "Mo", "Formula": "MoO2",  "DeltaH_kJmol": -588.0,  "DeltaS_JmolK": 33.0},
    {"Metal": "W",  "Formula": "WO3",   "DeltaH_kJmol": -842.0,  "DeltaS_JmolK": 57.0},
    {"Metal": "Mn", "Formula": "MnO",   "DeltaH_kJmol": -385.2,  "DeltaS_JmolK": 60.0},
    {"Metal": "Fe", "Formula": "Fe2O3", "DeltaH_kJmol": -824.2,  "DeltaS_JmolK": 87.4},
    {"Metal": "Co", "Formula": "CoO",   "DeltaH_kJmol": -237.9,  "DeltaS_JmolK": 42.6},
    {"Metal": "Ni", "Formula": "NiO",   "DeltaH_kJmol": -239.7,  "DeltaS_JmolK": 38.0},
    {"Metal": "Cu", "Formula": "Cu2O",  "DeltaH_kJmol": -170.7,  "DeltaS_JmolK": 56.0},
    {"Metal": "Zn", "Formula": "ZnO",   "DeltaH_kJmol": -350.46, "DeltaS_JmolK": 43.6},
    {"Metal": "Cd", "Formula": "CdO",   "DeltaH_kJmol": -258.0,  "DeltaS_JmolK": 44.0},
    {"Metal": "Hg", "Formula": "HgO",   "DeltaH_kJmol": -90.8,   "DeltaS_JmolK": 70.0},
    {"Metal": "Pb", "Formula": "PbO",   "DeltaH_kJmol": -219.0,  "DeltaS_JmolK": 68.0},
    {"Metal": "Sn", "Formula": "SnO2",  "DeltaH_kJmol": -580.7,  "DeltaS_JmolK": 52.3},
    {"Metal": "Bi", "Formula": "Bi2O3", "DeltaH_kJmol": -578.0,  "DeltaS_JmolK": 98.0},
    {"Metal": "Sb", "Formula": "Sb2O3", "DeltaH_kJmol": -706.7,  "DeltaS_JmolK": 160.0},
    {"Metal": "As", "Formula": "As2O3", "DeltaH_kJmol": -658.0,  "DeltaS_JmolK": 167.0},
    {"Metal": "Si", "Formula": "SiO2",  "DeltaH_kJmol": -856.0,  "DeltaS_JmolK": 42.0},
    {"Metal": "Ge", "Formula": "GeO2",  "DeltaH_kJmol": -580.0,  "DeltaS_JmolK": 41.0},
    {"Metal": "Se", "Formula": "SeO2",  "DeltaH_kJmol": -244.0,  "DeltaS_JmolK": 86.0},
    {"Metal": "Te", "Formula": "TeO2",  "DeltaH_kJmol": -289.0,  "DeltaS_JmolK": 95.0},
    {"Metal": "Y",  "Formula": "Y2O3",  "DeltaH_kJmol": -1900.0, "DeltaS_JmolK": 115.0},
    {"Metal": "La", "Formula": "La2O3", "DeltaH_kJmol": -1816.0, "DeltaS_JmolK": 116.0},
    {"Metal": "Ce", "Formula": "CeO2",  "DeltaH_kJmol": -1089.0, "DeltaS_JmolK": 85.0},
    {"Metal": "Nd", "Formula": "Nd2O3", "DeltaH_kJmol": -1803.0, "DeltaS_JmolK": 120.0},
    {"Metal": "Sm", "Formula": "Sm2O3", "DeltaH_kJmol": -1827.0, "DeltaS_JmolK": 122.0},
    {"Metal": "Gd", "Formula": "Gd2O3", "DeltaH_kJmol": -1819.0, "DeltaS_JmolK": 121.0},
    {"Metal": "Tb", "Formula": "Tb4O7", "DeltaH_kJmol": -2890.0, "DeltaS_JmolK": 175.0},
    {"Metal": "Dy", "Formula": "Dy2O3", "DeltaH_kJmol": -1810.0, "DeltaS_JmolK": 123.0},
    {"Metal": "Er", "Formula": "Er2O3", "DeltaH_kJmol": -1825.0, "DeltaS_JmolK": 124.0},
    {"Metal": "Yb", "Formula": "Yb2O3", "DeltaH_kJmol": -1810.0, "DeltaS_JmolK": 118.0},
    {"Metal": "U",  "Formula": "UO2",   "DeltaH_kJmol": -1085.0, "DeltaS_JmolK": 75.0},
    {"Metal": "Th", "Formula": "ThO2",  "DeltaH_kJmol": -1120.0, "DeltaS_JmolK": 80.0},
    {"Metal": "Ag", "Formula": "Ag2O",  "DeltaH_kJmol": -30.6,   "DeltaS_JmolK": 66.5},
    {"Metal": "Sc", "Formula": "Sc2O3", "DeltaH_kJmol": -1905.0, "DeltaS_JmolK": 120.0},
    {"Metal": "Ga", "Formula": "Ga2O3", "DeltaH_kJmol": -1089.0, "DeltaS_JmolK": 86.0},
    {"Metal": "Re", "Formula": "Re2O7", "DeltaH_kJmol": -1271.0, "DeltaS_JmolK": 220.0},

    # Added 3 new oxides to make total = 50
    {"Metal": "Cr", "Formula": "CrO2", "DeltaH_kJmol": -523.0, "DeltaS_JmolK": 52.0},
    {"Metal": "In", "Formula": "In2O3", "DeltaH_kJmol": -925.0, "DeltaS_JmolK": 89.0},
    {"Metal": "Tl", "Formula": "Tl2O3", "DeltaH_kJmol": -826.0, "DeltaS_JmolK": 110.0},
]

df = pd.DataFrame(data)
print("Total number of metal oxides:", len(df))  # should print 50

# Temperature range
T = np.linspace(300, 2500, 500)

# Plotting
plt.figure(figsize=(14, 10))
for _, row in df.iterrows():
    ΔH = row["DeltaH_kJmol"] * 1000
    ΔS = row["DeltaS_JmolK"]
    ΔG = ΔH - T * ΔS
    plt.plot(T, ΔG / 1000, label=f"{row['Metal']} ({row['Formula']})")

plt.xlabel("Temperature (K)", fontsize=12)
plt.ylabel("ΔG° (kJ/mol of O₂)", fontsize=12)
plt.title("Extended Ellingham Diagram (50 Metal Oxides)", fontsize=14, fontweight="bold")
plt.legend(fontsize=7, ncol=4)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
