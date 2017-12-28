#from collections import	Counter
seq = [20,1,-2,3,3,5,5,5,2,4,20,4,1,-2,5]

def find_it(seq):
  #solution1, it didn't	work returns None
  #c = Counter(seq)
  #return [i if	(c[i] %2 != 0) else None for i in c]

  #solution2, it works it requires importing Counter
  #return [ i for i in Counter(seq) if Counter(seq)[i] %2 !=0][0]

  #solution3, best, no need to import, someone in codewars came	with it
  return [x for	x in seq if seq.count(x) % 2][0]

print find_it(seq)
