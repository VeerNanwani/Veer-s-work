"""
RECORD CHECK  -  my version
===========================

Name  : Veer Sanjay Nanwani
Lane  : AI 
Date  : 03/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
df = pd.read_csv("GB_report.csv")  
df["percent"] = ((df["used_gb"] / df["total_gb"]) * 100).round(2)
df["status"] = df["percent"].apply(lambda x: "OVER LIMIT" if x > 100 else "WARNING" if x > 90 else "OK")

print(df)
print("="*60)
print(df[df["status"] != "OK"])
print("="*60)
print(df.groupby("status").size())
df.to_csv("GB_report_output.csv")

import matplotlib.pyplot as plt
status_counts = df["status"].value_counts()
status_counts.plot(kind='bar')
plt.title("Counts per Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.savefig("status_counts_bar_chart.png")
