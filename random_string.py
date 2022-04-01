import sys
from random import randint

str_length = int(sys.argv[1])
chr_range = int(sys.argv[2])

string = ''

for k in range(str_length):
    string += chr(randint(26,chr_range+26))

print(string)
