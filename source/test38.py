# @author：Sam
# @date:2017-12-02
# desc：
#

def writeData(data, path):
    if path == '' or path is None:
        f_path = 'file.txt'
    else:
        f_path = path
    if data == '' or data is None:
        print('请输入内容！')
        return
    with open(f_path, 'a+') as f:
        f.write(data)
        print('写入数据成功')
