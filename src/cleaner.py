from config import loadExcel
import pandas as pd

df = loadExcel()

#vendorList = [] could track later on
amtList = []
categoryList = []
dateList = []

# grabbing the amounts and round total (by 2 cents)
amounts = df['Amount']
pd.to_numeric(amounts)
amtList = amounts.tolist()
total = sum(amtList)
roundedTotal = round(total, 2)

print(roundedTotal)



