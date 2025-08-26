import pandas as pd
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
data = {"Months":["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Sales":[10000, 12000, 15000, 13000, 17000, 16000],
        "Profits":[2000, 3000, 4000, 2500, 3500, 3000]
        }
df = pd.DataFrame(data)
print(df)
print(df['Months'])

#normal plot
print(plt.plot(df['Months'], df['Sales'], color = 'blue', marker = "o", ls = ":", label = "Sales"))
plt.legend(loc = 'best')
plt.title('Monthly Sales')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

#barplot
plt.figure(figsize=(8,6))
print(plt.bar(df['Months'], df['Sales'], ls = "-", color = "skyblue", label = "Sales"))
print(plt.bar(df['Months'], df['Profits'], ls = "-", color = "green",label = 'Profits', bottom = df["Sales"]))
plt.title("Sales Vs Profits")
plt.grid(True)
plt.xlabel('Months')
plt.ylabel('Amount')
plt.legend()
plt.tight_layout()
plt.show()

#piechart
plt.figure(figsize = (5,5))
plt.pie(df['Profits'], labels = df['Profits'], autopct = '%1.2f%%', colors = plt.cm.Paired.colors)
plt.title("Pie-Chart")
plt.show()

#scatterplot
plt.scatter(df['Sales'], df['Profits'], color = 'yellow', s = 100, edgecolors = 'Black')
plt.xlabel('Sales')
plt.ylabel('Profits')
plt.tight_layout()
plt.title('Sales vs Profits')
plt.show()

# Histogram: Distribution of Sales
plt.figure(figsize=(8, 5))
plt.hist(df['Sales'], bins=5, color='purple', edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Box Plot: Profit Distribution
plt.figure(figsize=(8, 5))
plt.boxplot(df['Profits'], vert=False, patch_artist=True, boxprops=dict(facecolor="lightgreen"))
plt.title('Profit Distribution')
plt.xlabel('Profits ($)')
plt.tight_layout()
plt.show()
