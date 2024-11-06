import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\notga\OneDrive\Desktop\Acps\Visualization using matplotlib\CompanySalesData.csv')

plt.figure(figsize=(10, 6))
plt.plot(data['month_number'], data['total_profit'], linestyle=':', marker='o', color='red', linewidth=3, markerfacecolor='black')
plt.title('Month-wise Profit of the Company')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
products = ['Face Cream Sales', 'Face Wash Sales']
for product in products:
    plt.plot(data['month_number'], data['total_profit'], marker='o', linewidth=3, label=product)

plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(10, 6))
bar_width = 0.35
x = range(len(data['month_number']))

plt.bar(x, data['facecream'], width=bar_width, label='Face Cream', color='blue')
plt.bar([p + bar_width for p in x], data['facewash'], width=bar_width, label='Face Wash', color='green')

plt.title('Monthly Sales Comparison: Face Cream vs Face Wash')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks([p + bar_width / 2 for p in x], data['month_number'], rotation=45)
plt.legend()
plt.grid(axis='y')
plt.show()