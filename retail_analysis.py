import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("retail_sales.csv")
df["Revenue"] = df["Units_Sold"] * df["Price"]
print("Retail Sales Data")
print(df)
print("\nTotal Revenue:")
print(df["Revenue"].sum())
print("\nHighest Revenue Product:")
print(df.loc[df["Revenue"].idxmax()])
plt.figure(figsize=(8,5))
plt.bar(df["Product"], df["Revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()
plt.figure(figsize=(8,5))
plt.pie(
    df["Units_Sold"],
    labels=df["Product"],
    autopct="%1.1f%%"
)
plt.title("Units Sold Distribution")
plt.show()
