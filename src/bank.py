import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/Bank_Churn.csv')
# 1. Bar Plot for Gender Distribution

plt.figure(figsize=(8, 5))
sns.histplot(data['Age'], bins=20, kde=True, color='skyblue')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 2. Pie Chart for Gender Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='Geography', data=data, palette='Set2')
plt.title('Distribution of Customers Across Regions')
plt.xlabel('Geography')
plt.ylabel('Count')
plt.show()

# Plot for balances column
plt.figure(figsize=(8, 5))
sns.histplot(data['Balance'], bins=30, kde=True, color='green')
plt.title('Balance Distribution of Customers')
plt.xlabel('Balance')
plt.ylabel('Frequency')
plt.show()

