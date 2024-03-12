# Is there a significant difference in crime rates between male and female victims?
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
cursor.execute("SELECT Vict_Sex, count(*) as Crime_Count from crime_data group by Vict_Sex")
data = cursor.fetchall()
df = pd.DataFrame(data, columns=['Vict_Sex', 'Crime_Count'])

plt.bar(df['Vict_Sex'], df['Crime_Count'], color=['blue', 'red'])
plt.title('Crime Rates Between Male and Female Victims')
plt.xlabel('Victim Sex')
plt.ylabel('Crime Count')
plt.show()
