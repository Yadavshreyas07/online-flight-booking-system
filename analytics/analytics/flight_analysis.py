import pandas as pd
import matplotlib.pyplot as plt

# Load booking data
df = pd.read_csv("sample_bookings.csv")

print("=" * 50)
print("ONLINE FLIGHT BOOKING ANALYTICS")
print("=" * 50)

# Total Bookings
print(f"\nTotal Bookings : {len(df)}")

# Total Revenue
print(f"Total Revenue : ₹{df['Price'].sum():,.2f}")

# Most Popular Airline
popular_airline = df["Airline"].value_counts()

print("\nMost Popular Airlines")
print(popular_airline)

# Most Popular Route
routes = df["Source"] + " ➜ " + df["Destination"]

print("\nMost Popular Routes")
print(routes.value_counts())

# Revenue by Airline
revenue = df.groupby("Airline")["Price"].sum()

print("\nRevenue by Airline")
print(revenue)

# Chart
revenue.plot(kind="bar", figsize=(8,5), title="Revenue by Airline")

plt.xlabel("Airline")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.savefig("revenue_chart.png")

print("\nChart saved as revenue_chart.png")
