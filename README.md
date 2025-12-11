# isXorAlone?

The XOR binary function is known to have good properties, it's :
* associative   : (A+B)+C == A+(B+C)
* commutative   :     A+B == B+A
* an involution : (A+B)+B == A

## Is it the only one?

All the binary functions takes two arguments as entries and return one result.
As the arguments can be 0 or 1 (False or True), there are 4 different results.
The xor function can be resumed as "0110", that is:

          0 1
        -----
       0| 0 1
       1| 1 0

All the binary functions are then made of strings for "0000", "0001", "0010",
"0011", etc. until "1111". There are 16 such functions. The following piece
of code tests them through the three good properties.

In addition to the XOR function, the XNOR also complies. Here they are:

   XOR    0 1             NXOR    0 1
        -----                   -----
       0| 0 1                  0| 1 0
       1| 1 0                  1| 0 1

