# lcs_bv

# our $width = int 0.999+log(~0)/log(2);

# import math; int(0.999 + math.log(~0) / math.log(2));

# https://stackoverflow.com/questions/1405913/how-do-i-determine-if-my-python-shell-is-executing-in-32bit-or-64bit-mode-on-os
import sys
sys.maxsize > 2**32

n_bits = 32 << bool(sys.maxsize >> 32)

# https://stackoverflow.com/questions/2269827/how-to-convert-an-int-to-a-hex-string

#  hex(~0 & 0xffffffffffffffff)

