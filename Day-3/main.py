import pandas
import hashlib

print("Hi")

# Read and work with a file named 'words.csv'
df = pandas.read_csv('one.csv')
print(df) # This will display first few rows from the words.csv file

# use second module
m = hashlib.sha256()
print(m)