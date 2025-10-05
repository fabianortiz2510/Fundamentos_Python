# %%
# Ejercicios de Python Basico

#TIPOS DE VARIABLES
a=5
b=12.5
c="65"
x=True

d=float(a)
e=str(b)
f=int(c)
g=int(x)

print("El valor de a en tipo flotante es ",d)
print("El valor de b en tipo string es", e)
print("el valor de c en entero es",f)
print("el valor de x en entero es",g)


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

A=[1,2,3,4,"Michael",True,"Hard Metal".split()]
B=[1,6,8,14,"Jackson"]

A.extend(["Pop","Rock"])
print(A)

C=A+B
print(C)

del C[1]
print(C)


# %%
#SETS

A={"Rock",1,5,2,6,"Michael",5,16}
B=[2,6,8]

ConjuntoB=set(B)
print(ConjuntoB)

A.add("Jackson")
A.remove("Rock")
print(A)

8 in ConjuntoB
# %%
#DICCIONARIOS

Diccionario1={"Clave1":5,"Clave2":"Hola","Clave3":[3,3,3]}
a=Diccionario1["Clave3"]
Diccionario1["Clave4"]=(2,5,6)
print(a)
print(Diccionario1)

#%%
#CONDICIONALES
años=17

if (años>=18):
    print("puede ingresar al concierto")

else:
    print("No puede ingresar")

#Manejo de elif

edad = 18

if edad < 13:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")


# %%
#Loops
Cuadrados=['Amarillo','Azul','Rojo','Marrón','Naraja','Morado']

for i in range(0,3):
    Cuadrados[i]='White'

    print(Cuadrados)

# %%
