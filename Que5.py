#What is the distribution of reported crimes based on crime code?

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
cursor.execute("select Crm_Cd, count(*) as Crime_Count from crimedata.crime_data group by Crm_Cd order by Crime_Count desc limit 15")
data = cursor.fetchall()
df = pd.DataFrame(data, columns=["Crm_cd", "Crime_Count"])

plt.pie(df['Crime_Count'], labels=df['Crm_cd'], startangle=0, autopct=lambda p:'{:.0f}'.format(p*sum(df['Crime_Count'])/100), colors= plt.cm.Paired.colors)
plt.title('Top 15 Crime Codes based on Reported Crime')
plt.show()