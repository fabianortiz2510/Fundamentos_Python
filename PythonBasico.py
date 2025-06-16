# %%
#TIPOS DE VARIABLES
a=5
b=12.5
c="65"
x=True

d=float(a)
e=str(b)
f=int(c)
g=int(x)

print(d)
print(e)
print(f)
print(g)

a=3
print(a)

# %%
#MANEJO DE STRINGS

Name="Michael Jackson"

longitud=len(Name)
mayusculas=Name.upper()
reemplazo=Name.replace("Jackson","Jose")
print(longitud)
print(mayusculas)
print(reemplazo)

# %%
#Tupplas

Tupla=(0,1,2,3,"Pop",10)
Tupla2=(0,1,2,3,("Pop","Rock"),10)  #Anidamiento

print(Tupla[4])
print(Tupla2[4][1])

# %%
#Listas

A=[1,2,3,4,"Michael",True,"Hard Metal".split]
B=[1,6,8,14,"Jackson"]

A.extend(["Pop","Rock"])

print(A)

C=A+B
print(C)

del C[1]
print(C)


# %%
