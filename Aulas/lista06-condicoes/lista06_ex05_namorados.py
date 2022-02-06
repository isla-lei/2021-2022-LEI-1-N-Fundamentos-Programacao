"""Lista 06-Condições - Exercicio 5.

Pretende-se determinar se dois namorados são ou não compatíveis. Deve considerar-se o seguinte:
1. O rapaz tem de ser mais velho que a rapariga, sem ultrapassar 20 anos.
2. A distância entre as localidades tem de ser inferior a 10 km.
3. Não podem ser irmãos.
"""
idade_rapaz = int(input("Idade rapaz:...............: "))
idade_rapariga = int(input("Idade rapariga:............: "))
distancia = int(input("Distancia em Km entre eles.: "))
irmaos = input("São irmãos? (S/N)..........: ")

if ((idade_rapaz > idade_rapariga) and (idade_rapaz - idade_rapariga <= 20) and (distancia <= 10) and (irmaos == "N" or irmaos == "n")):
   print("Namorados compativeis")
else:
   print("Namorados não compativeis")
