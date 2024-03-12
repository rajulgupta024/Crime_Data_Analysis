# What is the distribution of victim ages in reported crimes?
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

cursor.execute("select Vict_Age from crime_data where Vict_Age is not null and Vict_Age > 0")
vict_age_df = pd.DataFrame(cursor.fetchall(), columns=['Vict_Age'])

plt.figure(figsize=(9, 5))
sns.histplot(vict_age_df['Vict_Age'], bins=20, kde=True, label='Agewise')
# KDE is best represntation for probability function
plt.title('Distribution fo victim ages in reported crimes')
plt.xlabel('Victim Age')
plt.ylabel('Frequency')
plt.legend()
plt.show()
connection.close()