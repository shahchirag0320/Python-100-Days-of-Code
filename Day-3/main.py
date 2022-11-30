import pandas
import hashlib

# Read and work with a file named 'words.csv'
df = pandas.read_csv('one.csv')
print(df) # This will display first few rows from the words.csv file

m = hashlib.sha256()
print(m)