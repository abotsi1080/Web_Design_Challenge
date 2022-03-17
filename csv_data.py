# Importing pandas dependencies
import pandas as pd

# Referencing the csv file path
csv_data = "Resources/cities.csv"

# Importing the csv file into Pandas DataFrame
csv_data_df = pd.read_csv(csv_data)

# Saving the imported data to html
csv_data_df.to_html("csv_data.html", index=False)

# Assigning the saved data to a table and printing the table
table = csv_data_df.to_html()
print(table)
