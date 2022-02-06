"""Lista 06-Condições - Exercicio 6.

Uma companhia de seguros pretende saber de forma automática qual o contrato que um
determinado cliente deve ter, após um conjunto de perguntas o programa deve concluir qual
o contrato a propor ao cliente.
A seguradora adoptou a seguinte política para um seguro de vida:
-goza de boa saúde e não sofreu acidentes   – contrato A
-goza de boa saúde e já teve um acidente    – contrato B
-não goza de boa saúde                      – exame médico
-já teve mais do que um acidente            – contrato recusado
"""

saude = input("Goza de boa saúde (S/N)...: ")
acidentes = int(input("Número de acidentes...: "))

if saude == "S" or saude == "s" and acidentes == 0:
    print("Goza de boa saúde e não sofreu acidentes - Contrato A")
elif saude == "S" or saude == "s" and acidentes == 1:
    print("Goza de boa saúde e já teve um acidente - Contrato B")
elif saude == "N" or saude == "n":
    print("Não goza de boa saúde - Exame Médico")
elif acidentes > 1:
    print("Já teve mais que um acidente - Contrato Recusado")
else:
    print("Dados errados")
