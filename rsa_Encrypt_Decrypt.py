#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
@File :  rsa_Encrypt_Decrypt_1.py  
@Desc :  RSA 加密解密
'''

'''
pip3 install pycryptodome

pycryptodome==3.9.7
'''

# Standard library imports
from typing import Union, Tuple
import base64
# Third party imports
import Crypto.PublicKey.RSA
import Crypto.Random
import Crypto.PublicKey.RSA
import Crypto.Cipher.PKCS1_v1_5
import Crypto.Random
import Crypto.Signature.PKCS1_v1_5
import Crypto.Hash
# Local application imports


class RsaEncryptDecrypt:
    def __init__(self):
        self.g_rsa = Crypto.PublicKey.RSA.generate(2048, Crypto.Random.new().read)

    def get_pub_pri_keys(self) -> Tuple[str, str]:
        """生公钥私钥
        """
        pri_key = self.g_rsa.exportKey().decode()  # 生成私钥
        pub_key = self.g_rsa.publickey().exportKey().decode() #生成公钥
        return pub_key, pri_key


    def encrypt(self, content: Union[str, bytes],
                pub_key: Union[str, bytes]) -> str:
        """加密"""
        if isinstance(content, str):
            content = content.encode('utf-8')
        if isinstance(pub_key, str):
            pub_key = pub_key.encode('utf-8')
        cipher_public = Crypto.Cipher.PKCS1_v1_5\
            .new(Crypto.PublicKey.RSA.importKey(pub_key))
        cipher_text = cipher_public.encrypt(content) # 使用公钥进行加密
        return base64.b64encode(cipher_text).decode('utf8')

    def decrypt(self, content: Union[str, bytes],
                pri_key: Union[str, bytes]) -> str:
        """解密
        """
        if isinstance(content, str):
            content = base64.b64decode(content)
        if isinstance(pri_key, str):
            pri_key = pri_key.encode('utf-8')
        cipher_private = Crypto.Cipher.PKCS1_v1_5\
            .new(Crypto.PublicKey.RSA.importKey(pri_key))
        text = cipher_private.decrypt(content,
                                      Crypto.Random.new().read)  # 使用私钥进行解密
        return text.decode()


if __name__ == "__main__":
    pub, pri = RsaEncryptDecrypt().get_pub_pri_keys()
    print("==" * 50)
    print(pub)
    print("--" * 50)
    print(pri)
    print("==" * 50)
    c = "hello world"
    mw = RsaEncryptDecrypt().encrypt(c, pub)
    print(mw)
    print("==" * 50)
    e_c = RsaEncryptDecrypt().decrypt(mw, pri)
    print(e_c)
