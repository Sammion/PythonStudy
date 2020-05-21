# @author Sam
# @date 2018-01-22
# desc 常见内建模块学习（三）
# Base64是一种最常见的二进制编码方法
# Base64是一种用64个字符来表示任意二进制数据的方法
# Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。
# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
# Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

import base64
# 标准编码
bb = base64.b64encode(b'binary string')
print(bb)
bs = base64.b64decode(bb)
print(bs)


# url safe 的base64编码
bb = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(bb)
bbs = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(bbs)