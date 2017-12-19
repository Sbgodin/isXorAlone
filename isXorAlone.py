#!/usr/bin/python3

""" isXorAlone

The XOR binary function is known to have good properties, it's :
* associative   : (A+B)+C == A+(B+C)
* commutative   :     A+B == B+A
* an involution : (A+B)+B == A

Is it the only one?

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

"""

class Operator:

    """ Defines any binary operator """

    def __init__(self, grid):
        """ Ex. Operator('[[1,1],[0,1]]') or Operator('1101')

        "0110" means
                      0 1
                    -----
                   0| 0 1
                   1| 1 0

        Which the XOR function.
        """
        grid = ''.join([g for g in grid if g.isdigit()])
        self.grid = grid
        assert len(grid)==4
        assert all(g in ("0","1") for g in grid)

    def __call__(self, a, b):
        assert a in (0,1) and b in (0,1)
        return int(self.grid[a+b*2])

    def __repr__(self):
        return "["+self.grid+"]"

    def __str__(self):
        return self.grid


# Generates all inputs possible with 2 or 3 bits
allInputs2 = [ (a,b) for a in (0, 1) for b in (0, 1) ]
allInputs3 = [ a+(c,) for a in allInputs2 for c in (0, 1) ]

# Generates all the operators
allOperators = [ Operator(a+b+c+d)
    for a in ("0", "1")
    for b in ("0", "1")
    for c in ("0", "1")
    for d in ("0", "1")
]

def demo():

    # Tests all operators with the 3 good properties
    associatives, commutatives, involutions = set(), set(), set()
    for o in allOperators:
        if all(o(o(a,b),b) == a for a,b in allInputs2):
            associatives.add(o)  # (A^B)^B == A
        if all(o(a,b) == o(b,a) for a,b in allInputs2):
            commutatives.add(o)  #     A^B == B^A
        if all(o(a,o(b,c)) == o(o(a,b),c) for a,b,c in allInputs3):
            involutions.add(o)   # (A^B)^C == A^(B^C)

    def pretty(things):
        return ' '.join([str(t) for t in things])

    # Displays the results, for all combinations of the proporties
    print('A are associatives')
    print('C are commutatives')
    print('I are involutions')
    print('A  ', pretty(associatives))
    print('C  ', pretty(commutatives))
    print('I  ', pretty(involutions))
    print('AC ', pretty(associatives & commutatives))
    print('AI ', pretty(commutatives & involutions))
    print('CI ', pretty(commutatives & involutions))
    print('ACI', pretty(associatives & commutatives & involutions))


if __name__ == "__main__":
    demo()
else:
    print('Type '+__name__+'.demo() to start')

