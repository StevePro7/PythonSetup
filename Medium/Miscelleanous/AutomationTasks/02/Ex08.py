# 08. Automate Spreadsheet Data
import openpyxl


def read_excel(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    for row in sheet.iter_row():
        print([cell.value for cell in row])
