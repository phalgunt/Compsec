#!/usr/bin/python3
# coding: latin-1
blob = """
                �ҷbX&\�����󸑒bI�W���#j9~��Ƥ�����0���A:�N��%��X�*>��D���:����m?@?7��P]� +�&a�Z�7����x]X���@�?UO�Vh�f�)LxK���uFn�E%"""
from hashlib import sha256
total = 0
iter = 1
for char in blob:
    temp = ord(char) 
    temp = temp * iter
    total = total + temp
    iter=iter+1

if (total > 600):
    print("Use SHA-256 instead!")
else:
    print("MD5 is perfectly secure")
