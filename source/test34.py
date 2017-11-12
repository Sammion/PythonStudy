'''
Created on 2017 11-11
@author: Sam
@Descripution: 
    帮助财务部门实现Excel表的数据自动比对功能
'''
import xlrd
import xlwt
import os
# from xlutils.copy import copy
# import openpyxl
# from openpyxl import Workbook

from xlrd import open_workbook
from xlutils.copy import copy

# f = xlwt.Workbook()
# t = f.add_sheet('info', cell_overwrite_ok=True)
# rb = xlrd.open_workbook()
# 打开Excel文件
# data = xlrd.open_workbook("../data/工作表1.xlsx")
# 获取工作表
# table = data.sheets()[0]
# table = data.sheet_by_name(u"sheet1")

# 获取整行和整列的值
# table.row_values(0)
# table.col_values(i)
# 获取行数和列数
# nrows = table.nrows
# print(nrows)
# ncols = table.ncols
# for i in range(nrows):
#     print(table.row_values(i))
# 单元格的数据
# cell_A1 = table.cell(0,0).value

# 按行列索引数据
# cell_A1 = table.row(0)[0].value
# cell_A2 = table.col(1)[0].value
# 使用put_cell写入数据
# row = 5
# col = 0
# 类型 0 empty, 1 string, 2 number, 3 date, 4 boolean, 5 error
# ctype = 1
# value = '单元格的值'
# table.put_cell(row, col, ctype, value, 0)

'''
表1和表2对比四列数据
如果销货表里的数据在报关单里面有，给出报关单里的内部编号和报关单号；否则在销货表最后一列输出“差异”
如果报关单里的数据在销货表里面有，给出销货表里的订单行ID和事务处理编号；否则在报关单最后一列输出“差异”
'''
# 文件的位置信息
f_name = "TOD报关单核对.xls"
f_path = "../data/" + f_name

# 两个变量分别存储表中的需要获取数据的列号,
# 第一列是可插入数据的列号，第2,3列是需要输出的两列数据，
# 最后四列是需要对比的四列数据
sale_col = [36, 2, 7, 10, 14, 19, 24]
custom_col = [83, 4, 5, 14, 53, 63, 70]
# 打开报关和销售数据Excel文件
data = open_workbook(f_path)
wb = copy(data)
# 获取每个文件的table
sale_table = data.sheets()[0]
# sale_wb = copy(sale_table)
custom_table = data.sheets()[1]
# custom_wb = copy(custom_table)
# 获取每个表的行数
sale_nrows = sale_table.nrows
custom_nrows = custom_table.nrows
print("销货表有%s行，报关表有%s行" % (sale_nrows, custom_nrows))

print(sale_table.row_values(1)[sale_col[3]])
print(sale_table.row_values(1)[sale_col[4]])
print(sale_table.row_values(1)[sale_col[5]])
print(sale_table.row_values(1)[sale_col[6]])

print(custom_table.row_values(0)[custom_col[3]])
print(custom_table.row_values(0)[custom_col[4]])
print(custom_table.row_values(0)[custom_col[5]])
print(custom_table.row_values(0)[custom_col[6]])
print("================><================")
print(sale_table.row_values(201)[sale_col[3]] == custom_table.row_values(681)[custom_col[3]])
print(int(sale_table.row_values(201)[sale_col[4]]) == int(custom_table.row_values(681)[custom_col[4]]))
print(sale_table.row_values(201)[sale_col[5]] == custom_table.row_values(681)[custom_col[5]])
print(sale_table.row_values(201)[sale_col[6]] == custom_table.row_values(681)[custom_col[6]])
# 检查销货表里面的数据是否在报关表里面
for i in range(sale_nrows):
    flag = False
    for j in range(custom_nrows):
        if sale_table.row_values(i)[sale_col[3]] == custom_table.row_values(j)[custom_col[3]] \
                and int(sale_table.row_values(i)[sale_col[4]]) == int(custom_table.row_values(j)[custom_col[4]]) \
                and sale_table.row_values(i)[sale_col[5]] == custom_table.row_values(j)[custom_col[5]] \
                and sale_table.row_values(i)[sale_col[6]] == custom_table.row_values(j)[custom_col[6]] \
                and (i != 0 or j != 0):
            # 插入是否匹配
            flag = True
            # print("销货表中第%s行数据在报关单中找到匹配，对应的内部编号是：%s,对应的报关单号是： %s" % (i + 1, custom_table.row_values(j)[custom_col[1]], custom_table.row_values(j)[custom_col[2]]))
            wb.get_sheet(0).write(i, sale_col[0] + 1, custom_table.row_values(j)[custom_col[1]])
            wb.get_sheet(0).write(i, sale_col[0] + 2, custom_table.row_values(j)[custom_col[2]])
            # wb.save(f_path)
    if not flag:
        # print("销货表中第%s行数据在报关单中未找到匹配" % i)
        # print(wb)
        wb.get_sheet(0).write(i, sale_col[0], "ERROR!")
        # wb.save(f_path)
for i in range(custom_nrows):
    flag = False
    for j in range(sale_nrows):
        if sale_table.row_values(j)[sale_col[3]] == custom_table.row_values(i)[custom_col[3]] \
                and int(sale_table.row_values(j)[sale_col[4]]) == int(custom_table.row_values(i)[custom_col[4]]) \
                and sale_table.row_values(j)[sale_col[5]] == custom_table.row_values(i)[custom_col[5]] \
                and sale_table.row_values(j)[sale_col[6]] == custom_table.row_values(i)[custom_col[6]] \
                and (i != 0 or j != 0):
            # 插入是否匹配
            flag = True
            # print("销货表中第%s行数据在报关单中找到匹配，对应的内部编号是：%s,对应的报关单号是： %s" % (i + 1, custom_table.row_values(j)[custom_col[1]], custom_table.row_values(j)[custom_col[2]]))
            wb.get_sheet(1).write(i, custom_col[0] + 1, sale_table.row_values(j)[sale_col[1]])
            wb.get_sheet(1).write(i, custom_col[0] + 2, sale_table.row_values(j)[sale_col[2]])
            # wb.save(f_path)
    if not flag:
        # print("销货表中第%s行数据在报关单中未找到匹配" % i)
        # print(wb)
        wb.get_sheet(1).write(i, custom_col[0], "ERROR!")
        # wb.save(f_path)
wb.save(f_path)
