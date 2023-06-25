import pandas

data = pandas.read_csv("dvf-communes-2019.csv")
df = pandas.DataFrame(data)
# Split column names by semicolon (;)
column_names = df.columns[0].split(';')

# Assign the split column names to the DataFrame's columns

# Split row values by semicolon (;) and create a new DataFrame
df_values = pandas.DataFrame([row.split(';') for row in df.iloc[:, 0]], columns=column_names)

# Filter the rows where ID is equal to 0
filtered_df = df_values[df_values['NOM_COM_M'] == 'Lille']

print(filtered_df)
