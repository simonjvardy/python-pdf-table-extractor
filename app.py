"""
App to extract table data from PDF files
"""
import camelot as cm

tables = cm.read_pdf('data/background_lines.pdf', flavor='lattice', process_background=True)

# we have a TableList object called tables, which is a list of Table objects
print(tables)

# Loop through the table objects and show the shape of each one
for n in tables:
    print(n)

print(tables[1].df)
print(tables[1].parsing_report)
