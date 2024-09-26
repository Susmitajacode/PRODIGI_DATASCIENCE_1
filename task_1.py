import pandas as pd
import matplotlib.pyplot as plt

# Function to load dataset and visualize both bar chart and histogram
def visualize_population_data(csv_file):
    # Load the dataset
    data = pd.read_csv(csv_file, skiprows=4)
    
    # Select a few countries and the population for the year 2020
    countries = ['Aruba', 'Afghanistan', 'Angola', 'India', 'China', 'United States', 'Brazil']
    population_2020 = data[data['Country Name'].isin(countries)][['Country Name', '2020']]

    # Bar chart for population distribution in 2020
    plt.figure(figsize=(10, 6))
    plt.bar(population_2020['Country Name'], population_2020['2020'], color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('Population in 2020')
    plt.title('Population Distribution by Country (2020)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Histogram for population distribution in 2020
    plt.figure(figsize=(10, 6))
    plt.hist(population_2020['2020'], bins=5, color='green', edgecolor='black')
    plt.xlabel('Population')
    plt.ylabel('Frequency')
    plt.title('Histogram of Population Distribution in 2020')
    plt.tight_layout()
    plt.show()

# Specify the path to the CSV file
csv_file = r"C:\Users\HP\OneDrive\Desktop\New folder (3)\API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv"

# Call the function to visualize the data
visualize_population_data(csv_file)
