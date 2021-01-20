 #Se citesc elementele unei liste, care reprezintă numere întregi (pozitive și negative). Să se afișeze la ecran:
	
x=[2,-4,7,3,-5,6,-2,4,9]
y=x.copy()
#a) conținutul (elementele) listei /lista1
print(x)
#b) lista sortată în ordine crescătoare / lista2
b=sorted(x)
print(b)
#c) lista sortată în ordine descrescătoare / lista3
c=b
c.sort(reverse=True)
print(c)
#d) numărul de elemente din listă
print(len(x))
#e) elementul MAX
print(max(x))
#f) elementul MIN
print(min(x))
#g) să se adauge la coadă în lista inițială elementul – 111. 
	#Să se afișeze lista nou-formată. / lista4
g=x
g.extend([111])
print(g)
#h) să se adauge pe poziția a doua din lista inițială elementul – 222. 
	#Să se afișeze lista nou-formată. / lista5
y.insert(2,222)
print(y)