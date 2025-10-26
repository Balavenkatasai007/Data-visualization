import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

file_path = r'C:\Users\saivi\OneDrive\Desktop\aqi_project\AQI_daily_city_level_hyderabad_2023_hyderabad_2023.xlsx'
df = pd.read_excel(file_path)

# Clean data: Remove rows with any empty strings or non-numeric values in critical columns
df['Day'] = pd.to_numeric(df['Day'], errors='coerce')
df['January'] = pd.to_numeric(df['January'], errors='coerce')

# Drop rows with NaN values after conversion
df = df.dropna(subset=['Day', 'January'])

# Plot Matplotlib line chart for January AQI
plt.figure(figsize=(10, 6))
plt.plot(df['Day'], df['January'], marker='o', color='skyblue')
plt.title('Hyderabad - Daily AQI Levels in January 2023')
plt.xlabel('Day')
plt.ylabel('AQI')
plt.grid(True)
plt.show()

# Similarly for Seaborn and other months if required
