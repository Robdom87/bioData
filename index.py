import pandas as pd

LVRev = pd.read_csv("./REV_B_COMPANY_2022-LV.csv")
LVRev_clean = LVRev.fillna('')


print(LVRev_clean)