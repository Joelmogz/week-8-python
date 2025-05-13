import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset from sklearn
try:
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map(dict(zip(range(3), iris.target_names)))
    print("Dataset loaded successfully!\n")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Data structure and missing values
print("\n Dataset info:")
print(df.info())

print("\n Missing values per column:")
print(df.isnull().sum())

# Clean data (no missing values in Iris, but shown here for generality)
df.dropna(inplace=True)



# Basic statistics
print("\n Descriptive statistics:")
print(df.describe())

# Group by species and compute the mean
print("\n Average measurements per species:")
species_mean = df.groupby('species').mean()
print(species_mean)

# Pattern or finding example
print("\n Observation: Setosa flowers tend to have much shorter petals compared to Virginica and Versicolor.")



sns.set(style="whitegrid")  # Nice background for plots

# 1. Line chart: Mean sepal length across species (as a line plot for demo)
plt.figure(figsize=(8, 5))
species_mean['sepal length (cm)'].plot(kind='line', marker='o', title='Average Sepal Length by Species')
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(8, 5))
species_mean['petal length (cm)'].plot(kind='bar', color='skyblue')
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of petal width
plt.figure(figsize=(8, 5))
plt.hist(df['petal width (cm)'], bins=15, color='orange', edgecolor='black')
plt.title("Distribution of Petal Width")
plt.xlabel("Petal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4. Scatter plot: Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species')
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()
