import openpyxl
import os


def load(filename, total_row=999999999999):
    """Using module "openpyxl" to load data from excel file(only support '.xlsx' format)

    Make sure you already install "openpyxl".
    :param filepath:
        Source file should be put under the path beneath the file which is calling this method.
        Otherwise you'll have to change some code inside.
    :return:
        list_row is a list consists of list records.
        For example, list_row[0] is a list consists of these cell in 1st row.
        Therefore, use list_row[0][0] represent the value in 1st column in 1st row(A1).
    """
    # Open a workbook by name= filename in READ-ONLY mode
    wb = openpyxl.load_workbook(filename, read_only=True)
    # Select this worksheet
    sheet = wb.get_active_sheet()
    sheet_rows = tuple(sheet.rows)
    # This is the total amount of rows in the excel file opened
    row_count = len(sheet_rows)
    print('row count: %s' % row_count)
    row_count = 0
    list_row = []
    for row in sheet.rows:
        row_count += 1
        temp_list = []
        for cell in row:
            # print(cell.value,end=',')
            temp_list.append(cell.value)
        list_row.append(temp_list)
        if row_count > total_row:
            break
    print("Loading Complete")
    return list_row
