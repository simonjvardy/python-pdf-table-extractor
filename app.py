"""
App to extract table data from PDF files
"""
import camelot as cm

tables = cm.read_pdf('/data/background_lines.pdf', process_background=True)
print(tables[1].df)
