
numero = int(input(" Digite o valor que deseja para seguencia de numeros pares com while :"))
a = 0
while a <= numero:
     if a % 2 == 0:
         print(a)
     a = a + 1


numero = int(input(" Digite o valor que deseja para seguencia de numeros pares com for :"))
for x in range(0, numero+1):
   print(x)
