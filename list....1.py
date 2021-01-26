with open('lista.txt','r') as f:
    n=list(eval(f.readline()))
print("lista initiala: ",n)
x=sorted(n)
print("lista sortata in ordine crescatoare: ",n)
x.sort(reverse=True)
print("lista sortata in ordine descrescatoare: ",x)
print("numărul de elemente din listă: ",len(n))
print("elementul maxim: ",max(n))
print("elementul minim:",min(n))
print("Elementul 111 adaugt la coadă în lista inițiala: ",n+[111])
n[2]=222
print("Adugarea elemtului 222 pe poziția a doua din lista inițială: ",n)
with open('iesire.txt','w') as f:
    f.write("lista initiala: "+str(x)+"\n")
   