import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/avocado.csv"
df = pd.read_csv(url)

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
print(df.head())

# 1. Lineplot: Average Price Over Time
plt.figure(figsize=(14,6))
sns.lineplot(x='Date', y='AveragePrice', data=df)
plt.title("Average Avocado Price Over Time")
plt.xlabel("Date")
plt.ylabel("Average Price (USD)")
plt.show()

# 2. Compare Price: Organic vs Conventional
plt.figure(figsize=(10,5))
sns.lineplot(data=df, x="Date", y="AveragePrice", hue="type")
plt.title("Average Price of Organic vs Conventional Avocados Over Time")
plt.show()

# 3. Top 10 Regions by Volume Sold
region_volume = df.groupby('region')['Total Volume'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=region_volume.values, y=region_volume.index)
plt.title("Top 10 Regions by Total Avocado Volume Sold")
plt.xlabel("Total Volume")
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Greens')
plt.title("Correlation Heatmap")
plt.show()

#5.Monthly Average Price Trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_avg = df.groupby(['Month', 'type'])['AveragePrice'].mean().reset_index()
monthly_avg['Month'] = monthly_avg['Month'].astype(str)
plt.figure(figsize=(14,6))
sns.lineplot(x='Month', y='AveragePrice', hue='type', data=monthly_avg)
plt.xticks(rotation=45)
plt.title("Monthly Average Avocado Price (Organic vs Conventional)")
plt.show()

#6. Boxplot: Price Distribution by Region
top_regions = df['region'].value_counts().head(5).index
df_top_regions = df[df['region'].isin(top_regions)]

plt.figure(figsize=(12,6))
sns.boxplot(x='region', y='AveragePrice', data=df_top_regions)
plt.title("Price Distribution by Region")
plt.show()

#7. Avocado Sales by Type Over Time (Area Plot)
df_grouped = df.groupby(['Date', 'type'])['Total Volume'].sum().unstack()
df_grouped.plot(kind='area', stacked=True, figsize=(14,6), alpha=0.7)
plt.title("Avocado Sales Over Time (Organic vs Conventional)")
plt.ylabel("Total Volume Sold")
plt.show()