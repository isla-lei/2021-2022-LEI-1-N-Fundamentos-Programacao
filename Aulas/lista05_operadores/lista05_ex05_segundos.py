"""Lista 05-Operadores - Exercicio 5.

Ler um valor em segundos e converter em HH:MM:SS
"""

segundos = float(input("Introduza os segundos: "))

horas = segundos // 3600
seg_restantes = segundos % 3600

minutos = seg_restantes // 60
seg = seg_restantes % 60

print(str(int(horas)).zfill(2), ":", str(int(minutos)).zfill(2), ":", str(int(seg)).zfill(2))

#ou..
print('{:02}'.format(int(horas)), ":", '{:02}'.format(int(minutos)), ":", '{:02}'.format(int(seg)))


