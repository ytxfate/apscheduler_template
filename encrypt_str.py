#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   encrypt_str.py
@Time    :   2019-08-14 12:17:15
@Desc    :   加密算法 及 解密
'''

# here put the import lib
import hashlib

# ================= md5 ======================== #   
def encrypt_md5(encrypt_str):
    """
    md5 加密
        @param:
            encrypt_str: 需要加密的字符串(str)或字节码(bytes)
        @return:
            返回一个32位加密后的字符串
    """
    if isinstance(encrypt_str, str):
        # 如果是 unicode 先转 utf-8
        encrypt_str = encrypt_str.encode("utf-8")
    m = hashlib.md5()
    m.update(encrypt_str)
    return m.hexdigest()

# ================= hash ======================== #
def encrypt_sha1(encrypt_str):
    """
    hash 加密
        @param:
            encrypt_str: 需要加密的字符串(str)或字节码(bytes)
        @return:
            返回一个40位加密后的字符串
    """
    if isinstance(encrypt_str, str):
        # 如果是 unicode 先转 utf-8
        encrypt_str = encrypt_str.encode("utf-8")
    h = hashlib.sha1()
    h.update(encrypt_str)
    return h.hexdigest()

def encrypt_sha224(encrypt_str):
    """
    hash 加密
        @param:
            encrypt_str: 需要加密的字符串(str)或字节码(bytes)
        @return:
            返回一个56位加密后的字符串
    """
    if isinstance(encrypt_str, str):
        # 如果是 unicode 先转 utf-8
        encrypt_str = encrypt_str.encode("utf-8")
    h = hashlib.sha224()
    h.update(encrypt_str)
    return h.hexdigest()

def encrypt_sha256(encrypt_str):
    """
    hash 加密
        @param:
            encrypt_str: 需要加密的字符串(str)或字节码(bytes)
        @return:
            返回一个64位加密后的字符串
    """
    if isinstance(encrypt_str, str):
        # 如果是 unicode 先转 utf-8
        encrypt_str = encrypt_str.encode("utf-8")
    h = hashlib.sha256()
    h.update(encrypt_str)
    return h.hexdigest()

def encrypt_sha384(encrypt_str):
    """
    hash 加密
        @param:
            encrypt_str: 需要加密的字符串(str)或字节码(bytes)
        @return:
            返回一个96位加密后的字符串
    """
    if isinstance(encrypt_str, str):
        # 如果是 unicode 先转 utf-8
        encrypt_str = encrypt_str.encode("utf-8")
    h = hashlib.sha384()
    h.update(encrypt_str)
    return h.hexdigest()

def encrypt_sha512(encrypt_str):
    """
    hash 加密
        @param:
            encrypt_str: 需要加密的字符串(str)或字节码(bytes)
        @return:
            返回一个128位加密后的字符串
    """
    if isinstance(encrypt_str, str):
        # 如果是 unicode 先转 utf-8
        encrypt_str = encrypt_str.encode("utf-8")
    h = hashlib.sha512()
    h.update(encrypt_str)
    return h.hexdigest()

