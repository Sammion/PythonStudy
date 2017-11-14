'''
Created on 2017 11-11
@author: Sam
@Descripution: 
    pip3 install xlutils
    pip3 install pyinstaller
    pip3 install chardet
    帮助财务部门实现Excel表的数据自动比对功能
    这里测试了一下pyinstaller打包成可执行程序的功能，执行命令：pyinstaller -F test34.py
    
'''
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import operator as op
import chardet

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
f_name = "001.xls"
f_path = "../data/" + f_name
# 加粗，红色字体
style = xlwt.easyxf('font: bold 1, color red;')
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
custom_table = data.sheets()[1]
# 获取每个表的行数
sale_nrows = sale_table.nrows
custom_nrows = custom_table.nrows
print("销货表有%s行，报关表有%s行" % (sale_nrows, custom_nrows))

print(sale_table.row_values(200)[sale_col[3]])
print(sale_table.row_values(200)[sale_col[4]])
print(sale_table.row_values(200)[sale_col[5]])
print(sale_table.row_values(200)[sale_col[6]])
print(custom_table.row_values(575)[custom_col[3]])
print(custom_table.row_values(575)[custom_col[4]])
print(custom_table.row_values(575)[custom_col[5]])
print(custom_table.row_values(575)[custom_col[6]])
print("=============================================> 我就是分割线 <====================================")
print(sale_table.row_values(17)[sale_col[3]] == custom_table.row_values(74)[custom_col[3]])
# print(int(sale_table.row_values(200)[sale_col[4]].strip()) == int(custom_table.row_values(575)[custom_col[4]].strip()))
print(sale_table.row_values(17)[sale_col[5]] == custom_table.row_values(74)[custom_col[5]])
print(sale_table.row_values(17)[sale_col[6]] == custom_table.row_values(74)[custom_col[6]])
print(int(sale_table.row_values(17)[sale_col[4]].strip().replace('\u202d', '').replace('\u202c', '')) == int(
    custom_table.row_values(74)[custom_col[4]].strip()))
print('============================================> 我是分割线 <========================================')
tmp1 = sale_table.row_values(200)[sale_col[4]].strip()
print(tmp1, type(tmp1))
tmp2 = custom_table.row_values(575)[custom_col[4]].strip()
print(tmp2, type(tmp2))
a = tmp2 == tmp1
# i_tmp1 = int(tmp1)
# i_tmp2 = int(tmp2)

print(sale_table.row_values(200)[sale_col[4]])
print(custom_table.row_values(575)[custom_col[4]])
# 检查销货表里面的数据是否在报关表里面
for i in range(2, sale_nrows):
    flag = False
    c1 = 1
    c2 = 2
    sale_client_name = sale_table.row_values(i)[sale_col[3]]
    sale_product_ID = int(sale_table.row_values(i)[sale_col[4]].strip().replace('\u202d', '').replace('\u202c', ''))

    sale_amount = sale_table.row_values(i)[sale_col[5]]
    sale_price = sale_table.row_values(i)[sale_col[6]]
    for j in range(1, custom_nrows):

        cus_client_name = custom_table.row_values(j)[custom_col[3]]
        cus_material_ID = int(custom_table.row_values(j)[custom_col[4]].strip())
        cus_amount = custom_table.row_values(j)[custom_col[5]]
        cus_price = custom_table.row_values(j)[custom_col[6]]
        if sale_client_name == cus_client_name and sale_product_ID == cus_material_ID \
                and sale_amount == cus_amount and sale_price == cus_price and (i != 0 or j != 0):
            flag = True
            print("销货表中第%s行数据在报关单中找到匹配，对应的内部编号是：%s,对应的报关单号是： %s" \
                  % (i + 1, custom_table.row_values(j)[custom_col[1]], custom_table.row_values(j)[custom_col[2]]))
            wb.get_sheet(0).write(i, sale_col[0] + c1, custom_table.row_values(j)[custom_col[1]], style)
            wb.get_sheet(0).write(i, sale_col[0] + c2, custom_table.row_values(j)[custom_col[2]], style)
            c1 += 2
            c2 += 2
    if not flag:
        # print("销货表中第%s行数据在报关单中未找到匹配" % i)
        wb.get_sheet(0).write(i, sale_col[0], "ERROR!")
# 检查报关单中的数据是否在销货表中。
for i in range(1,custom_nrows):
    flag = False
    c1 = 1
    c2 = 2
    cus_client_name = custom_table.row_values(i)[custom_col[3]]
    cus_material_ID = int(custom_table.row_values(i)[custom_col[4]].strip())
    cus_amount = custom_table.row_values(i)[custom_col[5]]
    cus_price = custom_table.row_values(i)[custom_col[6]]
    for j in range(2,sale_nrows):
        sale_client_name = sale_table.row_values(j)[sale_col[3]]
        sale_product_ID = int(sale_table.row_values(j)[sale_col[4]].strip().replace('\u202d', '').replace('\u202c', ''))
        sale_amount = sale_table.row_values(j)[sale_col[5]]
        sale_price = sale_table.row_values(j)[sale_col[6]]

        if sale_client_name == cus_client_name and sale_product_ID == cus_material_ID \
                and sale_amount == cus_amount and sale_price == cus_price and (i != 0 or j != 0):
            flag = True
            wb.get_sheet(1).write(i, custom_col[0] + c1, sale_table.row_values(j)[sale_col[1]], style)
            wb.get_sheet(1).write(i, custom_col[0] + c2, sale_table.row_values(j)[sale_col[2]], style)
            c1 += 2
            c2 += 2
    if not flag:
        # print("销货表中第%s行数据在报关单中未找到匹配" % i)
        wb.get_sheet(1).write(i, custom_col[0], "ERROR!")
wb.save(f_path)
