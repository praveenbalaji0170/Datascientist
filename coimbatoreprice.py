import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("coimbatore_prices.csv")


plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Year", y="Price_per_sqft", hue="Area", marker="o")

plt.title("Price Increase Trend for Each Area in Coimbatore")
plt.xlabel("Year")
plt.ylabel("Price per Sq.Ft (₹)")
plt.legend(title="Area", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

area = df[df["Area"] == "RS Puram"]

model = LinearRegression()
model.fit(area[["Year"]], area["Price_per_sqft"])

future_year = [[2026]]
predicted_price = model.predict(future_year)[0]

print("Predicted Price in RS Puram for 2026: ₹", round(predicted_price, 2))
