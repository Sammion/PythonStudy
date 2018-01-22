# @author Sam
# @date 2018-01-22
# desc 常见内建模块学习（四）
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
# Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。
# 采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

import hashlib
import hmac

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示.
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())


# Hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())