import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

print("Sadgurudeva")
print("Ammayya")
print("Sainatha")
print("Darbar Sainatha")
print("Om Sam Saravanabhava")

# Title
st.title("Titanic Dataset Explorer 🚢")

# Load dataset
titanic = sns.load_dataset("titanic")

st.write("### Raw Data Preview")
st.dataframe(titanic.head())

# Survival by gender
st.write("### Survival by Gender")
fig, ax = plt.subplots()
sns.countplot(x="sex", hue="survived", data=titanic, ax=ax)
st.pyplot(fig)

# Survival by class
st.write("### Survival by Class")
fig, ax = plt.subplots()
sns.countplot(x="class", hue="survived", data=titanic, ax=ax)
st.pyplot(fig)

# Age distribution
st.write("### Age Distribution by Survival")
fig, ax = plt.subplots()
sns.histplot(data=titanic, x="age", hue="survived", bins=50, kde=True, ax=ax)
st.pyplot(fig)

# Fare vs survival
st.write("### Fare vs Survival")
fig, ax = plt.subplots()
sns.boxplot(x="survived", y="fare", data=titanic, ax=ax)
st.pyplot(fig)
