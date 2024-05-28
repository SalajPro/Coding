import matplotlib.pyplot as plt

# Data
days = ['12/04/24', '13/04/24', '14/04/24', '15/04/24', '16/04/24', '17/04/24', '18/04/24', '19/04/24', '20/04/24', '21/04/24']
house_1_consumption = [11, 13, 16, 13, 9, 10, 8, 12, 12, 12]
house_2_consumption = [16, 12, 14, 13, 12, 15, 10, 13, 12, 11]

# Plotting
plt.figure(figsize=(12, 6))

plt.plot(days, house_1_consumption, marker='o', color='blue', label='House 1')
plt.plot(days, house_2_consumption, marker='o', color='red', label='House 2')

plt.xlabel('Date', fontweight='bold')
plt.ylabel('Consumption (kWh)', fontweight='bold')
plt.title('Daily Electric Consumption for Two Houses', fontweight='bold')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.grid(True)
plt.show()
