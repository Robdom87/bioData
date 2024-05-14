import pandas as pd

LVRev = pd.read_csv("./REV_B_COMPANY_2022-LV.csv")
LVRev_clean = LVRev.fillna('')


def correctDataTypes(df):
    # using dictionary to convert specific columns
    amtLabel = ["Invoice Amt $", "AMT PAID"]
    for label in amtLabel:
        df[f'{label}'].astype('str')
        df[f'{label}']=df[f'{label}'].str.replace(',','')
        df[f'{label}']=df[f'{label}'].str.replace('$','')
    # convert_dict = {
    #     "Description":str,
    #     "Category":str,
    #     "Type":str,
    #     "Amount":float
    #                 }
    # # convert date column to datetime format
    # dateLabel = ["Start Date", "Date of Completion", "Date invoiced"]
    # df['Date'] = pd.to_datetime(df['Date'])
    # df = df.astype(convert_dict)
    return df
LVRev_remove = correctDataTypes(LVRev_clean)

print(LVRev_remove)