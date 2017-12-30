import re
text = 'Quis custodiet ipsos custodes ?'

def pig_it(text):
    #my solution
    return " ".join([ w if re.match("[!?.,\"-]+", w)  else  w[1:] + w[:1] + 'ay' for w in text.split() ])

    #Creative one in codewars
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)

    #codewar I like the most, no need of re either
    #return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())
print pig_it(text)
