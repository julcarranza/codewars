import re
class Nonogram:
    def __init__(self, clues):

        self.cc = clues[0]
        self.cr = clues[1]
        self.lc, self.lr = len(clues[1]), len(clues[0]);
        self.expcr = []
        self.expcc = []
        self.solvednn = [[ 'q' for x in range(self.lc)] for y in range(self.lr)]

        for r, y in enumerate(self.cr):
            text1 = []
            for yy in y:
                text1.append('[1]{'+str(yy)+'}')
                i = self.lr - yy
                nofones = yy - i
                while nofones > 0:
                    self.solvednn[r][i] = '1'
                    nofones = nofones - 1
                    i +=1

            #covers 1-0-1-0-1 case
            if self.lr == sum(y)+len(y)-1:
                z = 0
                i = 0
                for yy in y:
                    while z < yy:
                        self.solvednn[r][i] = '1'
                        i += 1
                        z += 1
                        if z == yy and i < sum(y)+len(y)-1:
                            self.solvednn[r][i] = '0'
                            i += 1
                    z = 0


            self.expcr.append( '^[0]*' + '[0]+'.join(text1) + '[0]*$')

        for c, y in enumerate(self.cc):
            text1 = []
            for yy in y:
                text1.append('[1]{'+str(yy)+'}')
                i = self.lc - yy
                nofones = yy - i
                while nofones > 0:
                    self.solvednn[i][c] = '1'
                    nofones = nofones - 1
                    i +=1

            self.expcc.append( '^[0]*' + '[0]+'.join(text1) + '[0]*$')

            #covers 1-0-1-0-1 case
            if self.lc == sum(y)+len(y)-1:
                z = 0
                i = 0

                for yy in y:
                    while z < yy :

                        self.solvednn[i][c] = '1'
                        i += 1
                        z += 1
                        if z == yy and i < sum(y)+len(y)-1:
                            self.solvednn[i][c] = '0'
                            i += 1
                    z = 0


        for r, y in enumerate(self.cr):
            sumr = 0
            for e in self.solvednn[r]:
                if e == '1': sumr +=1
                if sum(y) == sumr:
                    for i, z in enumerate(self.solvednn[r]):
                        if self.solvednn[r][i] == 'q': self.solvednn[r][i] = '0'
        for c, x in enumerate(self.cc):
            sumc = 0
            for t in self.solvednn:
                for s, u in enumerate(t):
                    if s == c:
                        if u == '1':
                            sumc +=1
            if sum(x) == sumc:
                for t in self.solvednn:
                    for s, u in enumerate(t):
                        if s == c and u == 'q':
                            t[s] = '0'


        nnstring = []
        for f in self.solvednn:
            nnstring.append(''.join(f))
        self.nnwq = ''.join(nnstring)

    def solve(self):

        nq = self.nnwq.count('q')
        b = 0
        while b < 2**(nq) :
            nqc = ''
            ia = 2
            a = str(format(b, '#0'+str(nq+2)+'b'))
            for  inq in self.nnwq:
                if inq=='q':
                    nqc +=  a[ia]
                    ia +=1
                else:
                    nqc += inq

            rowexp = '([0|1]{' + str(self.lr)+'})'
            rows = re.findall(rowexp, nqc)
            columns = [ ]
            nonotrue = True
            for i, v in enumerate(rows):
                if nonotrue and re.match(self.expcr[i], v):
                    for l, j in enumerate(v):
                        if i == 0:
                            columns.append(str(j))
                        else:
                            columns[l] += str(j)
                else:
                    nonotrue = False
            if nonotrue:
                for i, v in enumerate(columns):
                    if nonotrue and not re.match(self.expcc[i], v):
                        nonotrue = False
            if nonotrue:
                d = []
                for i in rows:
                    c =[]
                    for j in i:
                        c.append(int(j))
                    d.append(tuple(c))
                return (tuple(d))
            b +=1

clues = (((1, 1), (4,), (1, 1, 1), (3,), (1,)),
((1,), (2,), (3,), (2, 1), (4,)))

clues1 = (((), (), (), (), ()),
((), (), (), (), ()))

clues2 = (((5,), (5,), (5,), (5,), (5,)),
((5,), (5,), (5,), (5,), (5,)))


clues3 = (((1,), (3,), (1,), (3, 1), (3, 1)), ((3,), (2,), (2, 2), (1,), (1, 2)))

nn = Nonogram(clues2)
print (nn.solve())
