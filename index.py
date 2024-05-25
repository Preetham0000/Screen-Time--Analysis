import pandas as pd
import numpy as np
import matplolib.pyplot as plt
import seaborn as sns

data = pd.read_csv("/kaggle/input/screentime/Screentime-App-Details.csv")
print(data.head())


print(data.isnull().sum())


print(data.describe())

plt.figure(figsize=(10, 6))
sns.barplot(data=data, x="Date", y="Usage", hue="App")
plt.title("Usage")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Usage")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=data, x="Date", y="Notifications", hue="App")
plt.title("Notifications")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Notifications")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=data, x="Date", y="Times opened", hue="App")
plt.title("Times Opened")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Times Opened")
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Notifications", y="Usage", hue="App", size="Notifications")
plt.title("Relationship Between Number of Notifications and Usage")
plt.xlabel("Notifications")
plt.ylabel("Usage")
plt.show()
