'''
Created on 2017 11-11
@author: Sam
@Descripution: 
    帮助财务部门实现Excel表的数据自动比对功能
    这里测试了一下pyinstaller打包成可执行程序的功能，执行命令：pyinstaller -F test34.py
'''
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import os

'''
表1和表2对比四列数据
如果销货表里的数据在报关单里面有，给出报关单里的内部编号和报关单号；否则在销货表最后一列输出“差异”
如果报关单里的数据在销货表里面有，给出销货表里的订单行ID和事务处理编号；否则在报关单最后一列输出“差异”
'''

# 文件的位置信息
print('请将文件放置当前目录下，谢谢合作！')
print('请输入文件名（默认为“TOD报关单核对.xls”）：')
i_f_name = input()
print("如果已经放置完成，请按回车键继续！")
os.system('pause'.encode('gb2312').decode('utf-8'))
if i_f_name == '':
    f_name = "TOD报关单核对.xls"
else:
    f_name = i_f_name
# f_path = "../data/" + f_name
# 粗字体
# style = xlwt.easyxf('font: bold 1')
# 加粗，红色字体

style = xlwt.easyxf('font: bold 1, color red;')
# 两个变量分别存储表中的需要获取数据的列号,
# 第一列是可插入数据的列号，第2,3列是需要输出的两列数据，
# 最后四列是需要对比的四列数据
sale_col = [36, 2, 7, 10, 14, 19, 24]
print('销售表里的位置：{0}'.format(sale_col))
custom_col = [83, 4, 5, 14, 53, 63, 70]
print('报关表里的位置：{0}'.format(custom_col))
print('第1个是可插入结果数据的列号，\n第2,3列是需要输出的两列数据，\n最后四列是需要对比的四列数据\n')
# 打开报关和销售数据Excel文件
data = open_workbook(f_name)
wb = copy(data)
# 获取每个文件的table
sale_table = data.sheets()[0]
custom_table = data.sheets()[1]
# 获取每个表的行数
sale_nrows = sale_table.nrows
custom_nrows = custom_table.nrows
print("销货表有%s行，报关表有%s行" % (sale_nrows, custom_nrows))
# 用来存储那些ERROR行里面的不重复Clients，初始值为空。
clients = []


# 追加客户信息
def addClient(s):
    if s not in clients:
        clients.append(s)
        return
    else:
        return


print('开始检查销货表里面的数据是否在报关表里面')
# 检查销货表里面的数据是否在报关表里面
for i in range(1, sale_nrows):
    flag = False
    c1 = 1
    c2 = 2
    sale_client_name = sale_table.row_values(i)[sale_col[3]]
    print(sale_table.row_values(i)[sale_col[4]])
    sale_product_ID = int(sale_table.row_values(i)[sale_col[4]])
    sale_amount = sale_table.row_values(i)[sale_col[5]]
    sale_price = sale_table.row_values(i)[sale_col[6]]
    for j in range(1, custom_nrows):
        cus_client_name = custom_table.row_values(j)[custom_col[3]]
        cus_material_ID = int(custom_table.row_values(j)[custom_col[4]])
        cus_amount = custom_table.row_values(j)[custom_col[5]]
        cus_price = custom_table.row_values(j)[custom_col[6]]
        if sale_client_name == cus_client_name and sale_product_ID == cus_material_ID \
                and sale_amount == cus_amount and sale_price == cus_price and (i != 0 or j != 0):
            flag = True
            # print("销货表中第%s行数据在报关单中找到匹配，对应的内部编号是：%s,对应的报关单号是： %s"
            # % (i + 1, custom_table.row_values(j)[custom_col[1]], custom_table.row_values(j)[custom_col[2]]))
            wb.get_sheet(0).write(i, sale_col[0] + c1, custom_table.row_values(j)[custom_col[1]], style)
            wb.get_sheet(0).write(i, sale_col[0] + c2, custom_table.row_values(j)[custom_col[2]], style)
            c1 += 2
            c2 += 2
            wb.get_sheet(0).write(i, sale_col[0], "OK", style)
    if not flag:
        # print("销货表中第%s行数据在报关单中未找到匹配" % i)
        wb.get_sheet(0).write(i, sale_col[0], "ERROR", style)
        # 记录有问题的记录信息：客户名称，产品编号，行号
        addClient([sale_client_name, sale_product_ID, i])
print('开始检查报关单中的数据是否在销货表中。')
# 检查报关单中的数据是否在销货表中。
for i in range(1, custom_nrows):
    flag = False
    c1 = 1
    c2 = 2
    cus_client_name = custom_table.row_values(i)[custom_col[3]]
    cus_material_ID = int(custom_table.row_values(i)[custom_col[4]])
    cus_amount = custom_table.row_values(i)[custom_col[5]]
    cus_price = custom_table.row_values(i)[custom_col[6]]
    for j in range(1, sale_nrows):
        sale_client_name = sale_table.row_values(j)[sale_col[3]]
        sale_product_ID = int(sale_table.row_values(j)[sale_col[4]])
        sale_amount = sale_table.row_values(j)[sale_col[5]]
        sale_price = sale_table.row_values(j)[sale_col[6]]
        if sale_client_name == cus_client_name and sale_product_ID == cus_material_ID \
                and sale_amount == cus_amount and sale_price == cus_price and (i != 0 or j != 0):
            flag = True
            wb.get_sheet(1).write(i, custom_col[0] + c1, sale_table.row_values(j)[sale_col[1]], style)
            wb.get_sheet(1).write(i, custom_col[0] + c2, sale_table.row_values(j)[sale_col[2]], style)
            c1 += 2
            c2 += 2
            wb.get_sheet(1).write(i, custom_col[0], "OK", style)
    if not flag:
        wb.get_sheet(1).write(i, custom_col[0], "ERROR", style)
wb.save(f_name)
# 下面处理Error中存在的正常情况
# 前提条件是，按客户，料号，编号排序
# 找到ERROR的行，销货表里客户和产品编号一致的数据加和汇总sum，然后在报关单里面找同一客户和料号从上往下求和汇总直到与sum相等，
# 在销货表中另起一列输出OK，同时输出报关单里面的内部编号用逗号分隔；同时在报关单里面ERROR后面输出OK，再给出订单行ID用逗号分隔。
# print('下面开始处理ERROR的情况')
# for s in clients:
#     sale_sum = 0
#     cus_sum = 0
#     # 遍历销货表
#     print('客户名称：', s[0], ' 行号：', s[2])
#     for i in range(s[2], 1, -1):
#         cus_client_name = custom_table.row_values(i)[custom_col[3]]
#         if cus_client_name == s[0] and sale_table.row_values(i)[sale_col[0]] == 'ERROR':
#             # 数量和金额求和
#             sale_sum = sale_sum + sale_table.row_values(i)[sale_col[5]] + sale_table.row_values(i)[sale_col[6]]
#     sale_sum = round(sale_sum, 2)
#     print('输出金额： ', sale_sum)
#     # 遍历报关单
#     interID = ''
#     for j in range(1, custom_nrows):
#         cus_client_name = custom_table.row_values(j)[custom_col[3]]
#         cus_material_ID = int(custom_table.row_values(j)[custom_col[4]])
#         cus_amount = float(custom_table.row_values(j)[custom_col[5]])
#         cus_price = float(custom_table.row_values(j)[custom_col[6]])
#         # print(type(custom_table.row_values(j)[custom_col[5]]))
#         # print(type(custom_table.row_values(j)[custom_col[6]]))
#
#         if custom_table.row_values(j)[custom_col[0]] == 'ERROR' and cus_client_name == s[0] and cus_material_ID == s[1]:
#             cus_sum = cus_sum + cus_amount + cus_price
#             interID = interID + ',' + custom_table.row_values(j)[4]
#             cus_sum = round(cus_sum, 2)
#             print('销货表中的总额：', sale_sum)
#             print('报关单中的总额：', cus_sum)
#             if cus_sum == sale_sum:
#                 # 跳出循环，输出结果
#                 wb.get_sheet(0).write(s[2], sale_col[0], "OK")
#                 wb.get_sheet(0).write(s[2], sale_col[0] + 1, interID, style)
#                 break
#             elif cus_sum > sale_sum:
#                 break
#
# wb.save(f_path)
print("Program has finished successfully!")
