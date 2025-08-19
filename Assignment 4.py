import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load dataset 
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df.head()
print(df.info())
print(df.describe(include='all'))
missing = df.isnull().mean() * 100
print("Missing Value Percentages:\n", missing)

sns.heatmap(df.isnull(), cbar=False, cmap="YlGnBu")
plt.title("Missing Data Heatmap")
plt.show()

# Univariate Analysis

sns.histplot(df['Age'].dropna(), kde=True, bins=30, color='skyblue')
plt.title('Age Distribution')
plt.show()
sns.histplot(df['Fare'], kde=True, bins=40, color='orange')
plt.title('Fare Distribution')
plt.show()
sns.boxplot(x='Survived', y='Age', data=df)
plt.title('Age by Survival')
plt.show()

sns.boxplot(x='Survived', y='Fare', data=df)
plt.title('Fare by Survival')
plt.show()

sns.countplot(x='Survived', data=df)
plt.title('Survival Count')
plt.show()


sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival by Pclass')
plt.show()

sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Sex')
plt.show()

sns.countplot(x='Embarked', hue='Survived', data=df)
plt.title('Survival by Embarkation')
plt.show()

# Outlier detection

sns.boxplot(data=df, x='Pclass', y='Fare')
plt.title('Fare by Pclass (Detecting Outliers)')
plt.show()

df['Log_Fare'] = np.log1p(df['Fare'])
sns.histplot(df['Log_Fare'], kde=True, bins=30)
plt.title('Log-Transformed Fare Distribution')
plt.show()

# Correlation Matrix
corr = df[['Survived', 'Age', 'Fare', 'SibSp', 'Parch']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# feature engineering
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
df['HasCabin'] = df['Cabin'].notnull().astype(int)
df[['FamilySize', 'IsAlone', 'Title', 'HasCabin']].head()
