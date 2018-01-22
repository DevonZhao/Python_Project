#!/usr/bin/env python
#! _*_ coding:utf8 _*_
import xlrd

def open_excel(file = 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byindex(file='file.xls',colnameindex = 0, by_index = 0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(colnameindex)
    print type(colnames)
    list = []
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list

def print_cell_list(file='file.xls', by_index = 0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    print nrows
    ncols = table.ncols
    try:
        for i in range(nrows):
                print table.cell(i+1,2).value+'.'+str(table.cell(i+1,1).value).split('.')[-1]
    except IndexError,e:
        pass

def main():
    tables = str(excel_table_byindex()).replace('u\'','\'').decode("unicode-escape")
    print tables
    # for row in tables:
    #     print row
if __name__ == "__main__":
    # main()
    print_cell_list()
