# -*- coding: utf-8 -*-

from ucimlrepo import fetch_ucirepo
import pandas as pd
import matplotlib.pyplot as plt


# Fetch dataset
national_poll_on_healthy_aging_npha = fetch_ucirepo(id=936)

# Extract data
X = national_poll_on_healthy_aging_npha.data.features
y = national_poll_on_healthy_aging_npha.data.targets

# Display metadata
print("Metadata:")
print(national_poll_on_healthy_aging_npha.metadata)

# Display variable information
print("\nVariable Information:")
print(national_poll_on_healthy_aging_npha.variables)

# Display all data (features and targets)
print("\nData:")
print(national_poll_on_healthy_aging_npha.data)

#  Draw pie chart for target column
plt.figure(figsize=(8, 8))
y.value_counts().plot.pie(
    labels=['0-1 doctors', '2-3 doctors', '4 or more doctors'],
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Pastel2.colors
)
plt.title('Number_of_Doctors_Visited')
plt.ylabel('')
plt.show()

# Draw pie chart for every feature column
for col in X.columns:
    plt.figure(figsize=(8, 8))
    X[col].value_counts().plot.pie(autopct='%1.1f%%',
                                   startangle=90, colors=plt.cm.Pastel2.colors)
    plt.title(col)
    plt.ylabel('')  # Hide y-label
    plt.show()
