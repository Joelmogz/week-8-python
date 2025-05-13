

COVID-19 Global Data Tracker

# Step 2: Data Loading & Exploration

import pandas as pd

# Load dataset
df = pd.read_csv("owid-covid-data.csv")

# Display the first few rows to inspect the dataset
print("Dataset Head:")
print(df.head())

# Check columns to understand data structure
print("\nColumns:")
print(df.columns)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Data Cleaning

# Filter for specific countries (e.g., Kenya, USA, India)
countries_of_interest = ['Kenya', 'USA', 'India']
df_filtered = df[df['location'].isin(countries_of_interest)]

# Drop rows with missing critical values
df_filtered = df_filtered.dropna(subset=['total_cases', 'total_deaths', 'total_vaccinations'])

# Convert 'date' to datetime format
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Fill missing numerical values where necessary (interpolation)
df_filtered['total_cases'] = df_filtered['total_cases'].fillna(method='ffill')
df_filtered['total_deaths'] = df_filtered['total_deaths'].fillna(method='ffill')

# Step 4: Exploratory Data Analysis

import matplotlib.pyplot as plt
import seaborn as sns

# Plot total cases over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

# Plot total deaths over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title('Total Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.show()

# Compare daily new cases between countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    country_data['new_cases'].plot(label=country)
plt.title('New Cases Per Day')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.show()

# Calculate and plot the death rate (total_deaths / total_cases)
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['death_rate'], label=country)
plt.title('Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.show()

# Step 5: Visualizing Vaccination Progress

# Plot cumulative vaccinations over time for selected countries
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title('Cumulative Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.show()

# Plot percentage vaccinated (total_vaccinations / population * 100)
# Assuming the dataset has 'population' column (or you could merge with an external population dataset)
df_filtered['vaccination_percentage'] = (df_filtered['total_vaccinations'] / df_filtered['population']) * 100
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['vaccination_percentage'], label=country)
plt.title('Vaccination Percentage Over Time')
plt.xlabel('Date')
plt.ylabel('Vaccination Percentage')
plt.legend()
plt.show()

# Step 6: Optional - Build a Choropleth Map (using Plotly)

import plotly.express as px

# Prepare a DataFrame with 'iso_code', 'total_cases' for the latest date
latest_data = df_filtered[df_filtered['date'] == df_filtered['date'].max()][['iso_code', 'total_cases']]

# Create choropleth map showing case density by country
fig = px.choropleth(latest_data,
                    locations='iso_code',
                    color='total_cases',
                    hover_name='iso_code',
                    color_continuous_scale='Viridis',
                    title='COVID-19 Case Density by Country')
fig.show()

## Key Insights:

1. **USA** had the highest number of cases globally but experienced a slow-down after initial peaks, especially after the vaccination rollout began.
2. **India** saw a significant surge in cases around mid-2021, but the recovery rate improved with the fast vaccine adoption.
3. Countries like **Kenya** had slower vaccination rates initially but made strong progress toward the end of 2021.

Additionally, there were sharp fluctuations in the daily new cases during different waves across the countries analyzed.
