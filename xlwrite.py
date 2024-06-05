import xlwt
from datetime import datetime
from xlrd import open_workbook
from xlutils.copy import copy
from pathlib import Path

def output(filename, sheet, num, name, present):
    # Construct the full file path with the filename
    full_path = r"D:\Anurag Wadhwa\Projects\FaceID Attendance Tracker\attendance\attendancefiles\\" + filename + str(datetime.now().date()) + '.xls'

    # Check if the file already exists
    my_file = Path(full_path)
    if my_file.is_file():
        rb = open_workbook(full_path, formatting_info=True)
        book = copy(rb)
        sh = book.get_sheet(0)
    else:
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    sh.write(0, 0, datetime.now().date(), style1)

    col1_name = 'Name'
    col2_name = 'Present'

    sh.write(1, 0, col1_name, style0)
    sh.write(1, 1, col2_name, style0)

    sh.write(num + 1, 0, name)
    sh.write(num + 1, 1, present)

    # Save the workbook with the constructed full path
    fullname = filename + str(datetime.now().date()) + '.xls'
    book.save(full_path)
    return fullname
