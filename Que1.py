# Where are the geographical hotspots for reported crimes?
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rajul1998",
    database="crimedata"
)

cursor = connection.cursor()
cursor.execute("select lat, lon from crime_data where lat is not null and lon is not null")
spatial_data = pd.DataFrame(cursor.fetchall(), columns=['lat', 'lon'])

plt.figure(figsize=(9, 7))
sns.scatterplot(x='lon', y='lat', data=spatial_data, alpha=0.4, label='spatial analysis', color='red', marker='o')
plt.title(label='crime hotspot')
plt.show()

# DB connection close
connection.close()