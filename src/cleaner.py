from config import loadExcel
import pandas as pd
import matplot.lib.pyplot as plt

df = loadExcel()

# removing rows with blanks
if df is not None:
    df = df[~(
        df["Amount"].isnull() & 
        df[["Vendor", "Category", "Date"]].isnull().all(axis=1)
    )]


# checking columns
df["Amount"] = pd.to_numeric(df["Amount"], errors = "coerce")
df["Category"] = df["Category"].apply(lambda x: "Miscellaneous" if pd.isna(x) or str(x).strip() == "" else x)
df["Vendor"] = df["Vendor"].apply(lambda x: str(x).strip() if pd.notna(x) else x)



# grabbing the amounts and round total (by 2 cents)
amounts = df['Amount']
pd.to_numeric(amounts)
amtList = amounts.dropna().tolist()
total = sum(amtList)
roundedTotal = round(total, 2)

# Category totals
categoryTotals = df.dropna(subset=["Category", "Amount"]).groupby("Category")["Amount"].sum().round(2)

# graphics for the category (pie chart and totals) WIP

