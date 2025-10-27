#%
# FIRST CELL
import pandas as pd
from pathlib import Path

# DEFINE BASE PATH
base_path = Path(r"C:\Users\sebas\Documents\Python\Python Projects\germany_gva\Data\processed")

# GVA SECTORS DICTIONARY
sectors = {
    'Industry & Energy': 'gva_industry_energy.xlsx',
    'Manufacturing': 'gva_manufacturing.xlsx',
}

# PROCESS GVA SECTORS DICTIONARY IN A LOOP
germany_dfs = [] # CREATES EMPTY LIST: "GERMANY DATAFRAMES"
for sector_name, filename in sectors.items(): # START LOOP
    # Read Excel File with correct sheet and skip first row (contains metadata)
    df = pd.read_excel(base_path / filename, sheet_name="Worksheet", skiprows=1)

    germany_df = (df[df["Country"] == "DEU"][["Code", "Country", "Name", 2021]] # Filter for Germany
    .dropna(subset=[2021]) # Drop NaNs
    .rename(columns={2021: f"2021 GVA {sector_name}"})) # Rename year columns according to GVA Sector

    germany_dfs.append(germany_df)

# Merge all dataframes
germany_all = germany_dfs[0]
for df in germany_dfs[1:]:
    germany_all = germany_all.merge(df, on=["Code", "Country", "Name"], how="outer")

# Export the final table
output_path = base_path / 'germany_gva_analysis.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl', mode='a',
                    if_sheet_exists='replace') as writer:
    germany_all.to_excel(writer, sheet_name='schema_1', index=False)

print("New sheet 'schema_1' successfully added to existing Excel File")













