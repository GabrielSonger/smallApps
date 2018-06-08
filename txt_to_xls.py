import ast
import xlwt

def get_content(in_file):
    with open(in_file) as infile:
        data = ast.literal_eval(infile.read())
    return data

def write_to_xls(data, outfile):
    row_counter = 0
    column_counter = 0
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet1')

    for k,v in data.iteritems():
        ws.write(row_counter, column_counter, k)
        column_counter += 1
        for value in v:
            ws.write(row_counter, column_counter, value)
            column_counter += 1
        row_counter += 1
        column_counter = 0
    wb.save(outfile)




data = get_content('student.txt')
write_to_xls(data, 'example.xls')