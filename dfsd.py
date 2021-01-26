#nu inteleg ce nu ajunge programului

with open("nume.txt","r") as f:
      x=f.readlines()
n=sorted(n)
with open("vbvn.txt","w") as f:   
    f.writelines(str(n))