import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
titanic = sns.load_dataset("titanic")


print("Sadgurudeva")
print("Ammayya")
print("Sainatha")
print("Darbar Sainatha")
print("Om Sam Saravanabhava")

# Survival by gender
sns.countplot(x="sex", hue="survived", data=titanic)
plt.title("Survival by Gender")
plt.show()

# Survival by class
sns.countplot(x="class", hue="survived", data=titanic)
plt.title("Survival by Class")
plt.show()

# Age distribution
sns.histplot(data=titanic, x="age", hue="survived", bins=30, kde=True)
plt.title("Age Distribution by Survival")
plt.show()
