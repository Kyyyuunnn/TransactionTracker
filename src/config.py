import pandas as pd
import os

def loadExcel():
    fileName = input(f"What is the file name of your excel sheet? Please include the '.xlsx'! ")

    try:
        file_path = os.path.join(os.path.dirname(__file__), '..', fileName)
        df = pd.read_excel(file_path)
        print("File successfully inputted")
        # print(df.head(10)) this just prints the beginning header files, small check
        return df

    except FileNotFoundError:
        print("File is not found (the file should be inside the folder)")
    except Exception as e: 
        print(f"Unknown error: {e}")

# simply for the check in the data cleaning part
    return None