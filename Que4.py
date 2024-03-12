# Where do most crimes occur based on the "Location" column?
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
cursor.execute("SELECT Location, COUNT(*) as Crime_Count FROM crimedata.crime_data GROUP BY Location ORDER BY Crime_Count DESC LIMIT 10")
data = cursor.fetchall()
df = pd.DataFrame(data, columns=["Location", "Crime_Count"])

plt.figure(figsize=(15, 8))  # Increase the figure size
sns.barplot(x="Location", y='Crime_Count', data=df, hue="Location")
plt.title('Top 10 Location with the most Crime')
plt.xlabel('Location')
plt.ylabel('Crime Count')
plt.xticks(rotation=45, ha='right')  # Rotate the x-axis labels by 45 degrees
plt.tight_layout()  # Adjust layout for better spacing
plt.show()
