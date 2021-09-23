import inspect

from rsa_Encrypt_Decrypt import RsaEncryptDecrypt


if __name__ == "__main__":

    print(inspect.isclass(RsaEncryptDecrypt))       # 判断是否为类
    print(inspect.getabsfile(RsaEncryptDecrypt))    # 获取绝对路径
    print(inspect.getsource(RsaEncryptDecrypt))     # 获取源码

    # 更多方法请查看标准库 inspect
