"""Ciclo For:Ejemplo 3"""

"""----------------------------------
---Múltiplos de 3 entre 0 y 10.000---
------------------------------------"""

contador =0
for i in range(-1,10000+1,+1):
    if (i%33==0):
        contador += 1

print (contador)