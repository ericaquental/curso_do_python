salario=float (input("Informe o seu salário"))
if salario < 128000:
        percentagem=0.2
        aumento=salario*percentagem
        novo_salario=salario+aumento
elif salario>=128000 and salario<=500000:
        percentagem=0.15
        aumento=salario*percentagem
        novo_salario=salario+aumento
elif salario>=500000 and salario<=1000000:
        percentagem=0.1
        aumento=salario*percentagem
        novo_salario=salario+aumento
else:
    percentagem=0.05
    aumento=salario*percentagem
    novo_salario=salario+aumento
print("Salario antes do reajusto:",salario)
print("Percentagem:",percentagem)
print("Aumento ao ser aplicado:", aumento)
print("Novo salário:",novo_salario)
