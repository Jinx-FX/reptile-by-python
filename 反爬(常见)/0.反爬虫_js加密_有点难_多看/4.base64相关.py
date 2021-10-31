#  base64:常用的一种加密，可以解密
import base64

print(base64.b64encode('abc'.encode()).decode()) #加密
print(base64.b64decode('YWJj'.encode()).decode())#解密

#  01010100  01000000  11111100 11000000 10101000 10000000
#  YWJj
