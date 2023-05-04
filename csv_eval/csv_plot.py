import pandas as pd
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1)
# make a little extra space between the subplots
fig.subplots_adjust(hspace=0.5)

# Read the CSV file
energy = pd.read_csv('energy_100users_fib5.csv')
response = pd.read_csv('response_100users_fib5.csv')

# Find the minimum and maximum time values in the response dataset
response_min_time = response['time'].min()
response_max_time = response['time'].max()

response['time'] = response['time'].astype(int)
response = response.groupby('time').count().reset_index()

energy['time'] = energy['time'].astype(int)

# Plot the data
energy_line, = ax1.plot(energy['time'], energy['energy'], label='Energy')
response_line, = ax2.plot(response['time'], response['response'], label='Response')

# Write ay line to determine the min and the max
ax1.axvline(x=response_min_time, color='red', linestyle='--', label='Start of load charging')
ax1.axvline(x=response_max_time, color='red', linestyle='--', label='End of load charging')

# Set x axis limits for responses
ax2.set_xlim(energy['time'].min() , energy['time'].max())

# Smooth the energy line
energy_line.set_antialiased(True)


plt.show()
