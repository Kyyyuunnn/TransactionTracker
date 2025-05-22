from config import loadExcel
import pandas as pd

df = loadExcel()

# #vendorList = [] could track later on
# amtList = []
# categoryList = []
# dateList = []

# removing rows with blanks
df = df.dropna(subset = ["Vendor", "Category", "Amount", "Date"])

# make sure each category is the correct format/type

# grabbing the amounts and round total (by 2 cents)
amounts = df['Amount']
pd.to_numeric(amounts)
amtList = amounts.tolist()
total = sum(amtList)
roundedTotal = round(total, 2)

# Category totals
categoryTotals = df.groupby("Category")["Amount"].sum().round(2)




