from config import loadExcel
import pandas as pd

df = loadExcel()

# #vendorList = [] could track later on
# amtList = []
# categoryList = []
# dateList = []

# removing rows with blanks
if df is not None:
    df = df[~(
        df["Amount"].isnull() & 
        df[["Vendor", "Category", "Date"]].isnull().all(axis=1)
    )]


# make sure each category is the correct format/type
df["Amount"] = pd.to_numeric(df["Amount"], errors = "coerce")


# grabbing the amounts and round total (by 2 cents)
amounts = df['Amount']
pd.to_numeric(amounts)
amtList = amounts.dropna().tolist()
total = sum(amtList)
roundedTotal = round(total, 2)

# Category totals
categoryTotals = df.dropna(subset=["Category", "Amount"]).groupby("Category")["Amount"].sum().round(2)

print(categoryTotals)


