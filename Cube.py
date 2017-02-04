#Author: Jason Drain
#Defines a Rubik's Cube Object

import numpy as np

class Ring(object):

    def __init__(self, r, rc, number1, number2):
        #numbers are always the same for second col/row
        self.r = r
        self.rc = rc
        self.sr1 = number1
        self.sr2 = [2,2,2,2]
        self.sr3 = number2

class Sets(object):

    def __init__(self, s, ring):
        self.s = s
        self.ring = ring

class Face(object):

    def __init__(self, name, r1, r2, r3, c1, c2, c3):
        self.name = name
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

class Cols(Sets):

    def __init__(self, col=True):
        self.col = col

class Rows(Sets):

    def __init__(self, row=True):
        self.row = row

rc_ls = ['r', 'c', 'r', 'r']
c_ls = ['c', 'c', 'c', 'c']
ls_1 = [3,1,1,1]
ls_2 = [1,3,3,3]
ls_3 = [1,1,1,1]
ls_4 = [3,3,3,3]
ring_ls1 = [6,5,3,2]
ring_ls2 = [6,4,3,1]
ring_ls3 = [1,2,4,5]

ring1 = Ring(r = ring_ls1, rc = rc_ls, number1 = ls_1, number2 = ls_2)
ring2 = Ring(r = ring_ls2, rc = c_ls, number1 = ls_3, number2=ls_4)
ring3 = Ring(r = ring_ls3, rc = rc_ls, number1=ls_1, number2=ls_2)

f1_c = Cols()
f1_c.s = [1,1,1]
f1_c.ring = ring2

f1_r = Rows()
f1_r.s = [1,1,1]
f1_r.ring = ring3

face1_cols = {'f1_c1': f1_c, 'f1_c2': f1_c, 'f1_c3': f1_c}
face1_rows = {'f1_r1': f1_r, 'f1_r2': f1_r, 'f1_r3': f1_r}

f2_c = Cols()
f2_c.s = [2,2,2]
f2_c.ring = ring3

f2_r = Rows()
f2_r.s = [2,2,2]
f2_r.ring = ring1

face2_cols = {'f2_c1': f2_c, 'f2_c2': f2_c, 'f2_c3': f2_c}
face2_rows = {'f2_r1': f2_r, 'f2_r2': f2_r,  'f2_r3': f2_r}

f3_c = Cols()
f3_c.s = [3,3,3]
f3_c.ring = ring2

f3_r = Rows()
f3_r.s = [3,3,3]
f3_r.ring = ring1

face3_cols = {'f3_c1': f3_c, 'f3_c2': f3_c, 'f3_c3': f3_c}
face3_rows = {'f3_r1': f3_r, 'f3_r2': f3_r, 'f3_r3': f3_r}

f4_c = Cols()
f4_c.s = [4,4,4]
f4_c.ring = ring2

f4_r = Rows()
f4_r.s = [4,4,4]
f4_r.ring = ring3

face4_cols = {'f4_c1': f4_c, 'f4_c2': f4_c, 'f4_c3': f4_c}
face4_rows = {'f4_r1': f4_r, 'f4_r2': f4_r, 'f4_r3': f4_r}

f5_c = Cols()
f5_c.s = [5,5,5]
f5_c.ring = ring1

f5_r = Rows()
f5_r.s = [5,5,5]
f5_r.ring = ring3

face5_cols = {'f5_c1': f5_c, 'f5_c2': f5_c, 'f5_c3': f5_c}
face5_rows = {'f5_r1': f5_r, 'f5_r2': f5_r, 'f5_r3': f5_r}

f6_c = Cols()
f6_c.s = [6,6,6]
f6_c.ring = ring2

f6_r = Rows()
f6_r.s = [6,6,6]
f6_r.ring = ring1

face6_cols = {'f6_c1': f6_c, 'f6_c2': f6_c, 'f6_c3': f6_c}
face6_rows = {'f6_r1': f6_r, 'f6_r2': f6_r, 'f6_r3': f6_r}

class Cube(object):

    def __init__(self, name, one, two, three, four, five, six):
        self.name = name
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.face_list = [self.one, self.two, self.three, self.four, self.five, self.six]

    def display(self):
        print self.name, self.one, self.two, self.three, self.four, self.five, self.six