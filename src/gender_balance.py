import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/Bank_Churn.csv')
# 1. Bar Plot for Gender Distribution
plt.figure(figsize=(8, 5))
sns.boxplot(x='Gender', y='Balance', data=data, palette='Set3')
plt.title('Gender-wise Balance Distribution')
plt.xlabel('Gender')
plt.ylabel('Balance')
plt.show()
