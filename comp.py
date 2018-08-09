def comp(array1, array2):
	if array2 != None and array1 != None:
		array1.sort()
		array2.sort()
		a1squared = [ i * i for i in array1 ]

		if a1squared == array2: 
			return True
	
	return False
	
	
	


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
a3 = []
a4 = []
a5 = None
a6 = None

print (comp(a1, a2))
print (comp(a3, a4))
print (comp(a5, a6))

""" 
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False"""