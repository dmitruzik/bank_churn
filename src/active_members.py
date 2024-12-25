import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data/Bank_Churn.csv')
# active and nonactive members

plt.figure(figsize=(6, 4))
sns.countplot(x='IsActiveMember', data=data, palette='Set1')
plt.title('Active vs Inactive Members')
plt.xlabel('Is Active Member')
plt.ylabel('Count')
plt.xticks([0, 1], ['Inactive', 'Active'])
plt.show()
