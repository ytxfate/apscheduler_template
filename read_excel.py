import xlrd

with open('temp.xlsx', "rb") as f:
    data = xlrd.open_workbook(file_contents=f.read())
    sheets = data.sheets()
    for sheet in sheets:
        sheet_name = sheet.name
        for n in range(sheet.nrows):
            row_value = sheet.row_values(n)
            print(row_value)
        