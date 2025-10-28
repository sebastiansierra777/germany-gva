# GDP PPP PER CAPITA LEFT JOIN ON GVAs DATAFRAME
import pandas as pd

# LOAD FILES
df_gva = pd.read_excel(
    r'C:\Users\sebas\Documents\Python\Python Projects\germany_gva\Data\processed\germany_gva_analysis.xlsx',
    sheet_name="schema_1")

df_ppp = pd.read_excel(
    r"C:\Users\sebas\Documents\Python\Python Projects\germany_gva\Data\processed\gdp_pc_tl3\gdp_pc_tl3.xlsx",
    sheet_name="Worksheet")

# FILTER GDP DATA FOR UK ONLY
germany_ppp = df_ppp[df_ppp["Country"] == "DEU"][["TL3", 2021]]

# LEFT JOIN ON TL3
df_merged = df_gva.merge(germany_ppp, on="TL3", how="left")

# EXPORT MERGED DATAFRAME
with pd.ExcelWriter(
        r'C:\Users\sebas\Documents\Python\Python Projects\germany_gva\Data\processed\germany_gva_analysis.xlsx',
        engine='openpyxl',
        mode='a',
        if_sheet_exists='replace'
) as writer:
    df_merged.to_excel(
        writer,
        sheet_name='schema_2',
        index=False)

print("New sheet 'schema_2' added to the existing Excel file.")