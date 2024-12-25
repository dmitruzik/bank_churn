import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/Bank_Churn.csv')

# salary distribution
plt.figure(figsize=(8, 5))
sns.histplot(data['EstimatedSalary'], bins=30, kde=True, color='orange')
plt.title('Estimated Salary Distribution of Customers')
plt.xlabel('Estimated Salary')
plt.ylabel('Frequency')
plt.show()