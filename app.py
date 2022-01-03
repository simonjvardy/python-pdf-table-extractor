"""
App to extract table data from PDF files
"""
import camelot as cm

"""
Import the PDF data
"""

tables = cm.read_pdf('data/background_lines.pdf', flavor='lattice', process_background=True)

# we have a TableList object called tables, which is a list of Table objects
print(tables)

# Loop through the table objects and show the shape of each one
for n in tables:
    print(n)

# View the table parsing report to see the quality of the extraction
print(tables[1].parsing_report)

"""
Process the DataFrame and cleanse / manipulate the data
"""

# Choose the first main table from the PDF
df = tables[1].df

# Clean up the column data removing the new line chars and number formatting
df = df.replace(' \n',' ', regex=True)
df = df.replace('\n',' ', regex=True)
df = df.replace(',','', regex=True)

# fill empty merged rows from PDF with data
df.loc[2,2:] = df.loc[1,2:]

# Replace the column headers with first row data
df.columns = df.iloc[0]
df.columns = df.columns.str.strip()
df = df[1:]

# Update the column data types from the default string (object) type
df = df.astype({
    'Halt stations':'int64',
    'Halt days':'int64',
    'Persons directly reached (in lakh)':'float64',
    'Persons trained':'int64',
    'Persons counseled':'int64',
    'Persons tested for HIV':'int64'})
print(df.dtypes)  # column data types

print(df)  # Show the table data

"""
Output the data to CSV or XLSX file formats
"""
df.to_csv('data/table_output.csv')
df.to_excel('data/table_output.xlsx')
