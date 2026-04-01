# convert bin to dec
a = '0b10010001'
print(a, '=', int(a, 2), '[D]')

# convert hex to dec
b = '0xff'
print(b, '=', int(b, 16), '[D]')

# convert dec to bin/hex
c = 19
print(c, '[D]', '=', bin(c))
# or you can use format string
print(f"{c} [D] = {c:#04x}") # 0 - show 0x, 2 - 4 digit hex(include 0x), x - hex
print(f"{c} [D] = {c:#010b}") # 0 - show 0x, 2 - 10 digit bin(include 0b), b - binary

# show the binary storing of a signed number
# we use numpy, you can install numpy use pip: pip install numpy
import numpy as np
d = -3
print(d, 'is stored as:', '0b' + np.binary_repr(d, 8))