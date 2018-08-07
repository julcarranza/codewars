def duplicate_encode(word):
	
	for l in word.lower():
		print word, l, word.lower().count(l)
		
		
	return "".join([")" if word.lower().count(l) > 1 else  "(" for l in word.lower()])		

examples = [ "lHwx@v)@OH)u(mbP)dJxJPb(vyRJl"]

for e in examples:
	print duplicate_encode(e)