import pandas as pd

df = pd.read_csv('../Donors.csv')

dfslice = df[ ['Donor ID', 'Donor City'] ]  # カラム名 Donor ID, Donor Cityでスライスする（スライスされたDataFrameが帰る）

donor_series = df[ 'Donor ID' ] # カラム名 Donor IDのSeriesが帰る

gp = dfslice.groupby('Donor City')

for key, dfg in gp:
  print(key, dfg)
