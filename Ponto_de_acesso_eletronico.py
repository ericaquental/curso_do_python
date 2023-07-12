identidade=input("Qual é o numero do seu BI?")
resultado=identidade.strip()
base_de_dados={"006914006LA043":
    {
        "nome":"erica quental",
        "cursos":["Python"],
        "computador":"Mediateca",
        "contacto":"939263755/925957678"
    }      
                  
}
aluna=base_de_dados.get(resultado)
if aluna:
    print("Aluna foi encontrada com sucesso")
    Hora_de_entrada=input("Hora de entrada")    
else:
    print("O BI não corresponde a nenhuma aluna")
    
