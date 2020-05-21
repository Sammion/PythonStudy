# -*- coding: utf-8 -*-
"""
Created on 2018/6/22

@author: Samuel
@Desc: 
@dependence: pip install rsa
Successfully installed pyasn1-0.4.3 rsa-3.4.2
"""
import rsa
from binascii import b2a_hex, a2b_hex

def gen_keys(len_key=1024):
    publish_key, private_key = rsa.newkeys(len_key)
    return publish_key, private_key


def gen_password(src_text, publish_key):
    # encrypting the text to ascii string
    cipher_text = rsa.encrypt(src_text.encode(), publish_key)
    # encrypted string transfer to 16 hex
    return b2a_hex(cipher_text)


def gen_text(ency_text, private_key):
    decrypt_text = rsa.decrypt(a2b_hex(ency_text), private_key)
    return decrypt_text


if __name__ == '__main__':
    text = "ebay_welW12312&*@!:"
    pub, private = gen_keys()
    print(pub)
    print(private)
    #
    pass_word = gen_password(text, pub)
    print(pass_word)
    src_text = gen_text(pass_word,private)
    print(src_text)
