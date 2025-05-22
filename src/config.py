import pandas as pd

fileName = input(f"What is the file name of your excel sheet? Please include the '.xlsx'!")

try:
    df = pd.read_excel(fileName)
    print("File successfully inputted")
    print(df.head())

except FileNotFoundError:
    print("File is not found (the file should be inside the folder)")
except Exception as e: 
    print(f"Unknown error: {e}")