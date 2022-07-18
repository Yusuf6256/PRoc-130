import pandas as pd
import csv

df = pd.read_csv("dwarf_starss_sorted1.csv")
print(df.shape)

del df["Luminosity"]
print(df.shape)