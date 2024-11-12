def gerar_plano_treino(biotipo, dias_treino, tipo_exercicio):
    # Dicionário para plano de treino baseado no biotipo
    planos = {
        "Ectomorfo": {
            "Funcional": "Treino funcional focado em ganho de força e resistência com ênfase em exercícios compostos.",
            "Maquinário": "Treino com máquinas para ganho de massa muscular, focado em grandes grupos musculares.",
            "Peso Livre": "Treino com pesos livres para hipertrofia e força, com cargas progressivas.",
            "Cardio": "Cardio leve para aumentar a resistência cardiovascular sem perda de massa muscular.",
            "HIIT": "Treino HIIT moderado para aumentar a resistência sem impacto na massa magra."
        },
        "Mesomorfo": {
            "Funcional": "Treino funcional equilibrado com foco em resistência e tonificação muscular.",
            "Maquinário": "Treino em máquinas com foco em hipertrofia e definição.",
            "Peso Livre": "Treino intenso com pesos livres para aumentar a massa e a definição muscular.",
            "Cardio": "Cardio moderado para manter o condicionamento físico.",
            "HIIT": "Treino HIIT intenso para queima de gordura e manutenção da massa muscular."
        },
        "Endomorfo": {
            "Funcional": "Treino funcional para queima de calorias e fortalecimento muscular.",
            "Maquinário": "Treino em máquinas com foco em perda de peso e tonificação.",
            "Peso Livre": "Treino com pesos livres, usando séries e repetições para queima de gordura.",
            "Cardio": "Cardio intenso para auxiliar na queima de gordura.",
            "HIIT": "HIIT focado em alta intensidade para maximizar a queima calórica."
        }
    }
    
    # Seleciona o plano de treino baseado no biotipo e no tipo de exercício
    treino_selecionado = planos.get(biotipo, {}).get(tipo_exercicio, "Plano de treino não disponível para essa combinação.")
    
    # Ajusta o plano com base nos dias disponíveis para treino
    plano_final = f"Plano de treino para um {biotipo} com {dias_treino} dias de treino focado em {tipo_exercicio}: {treino_selecionado}"
    return plano_final

# Exemplo de uso
biotipo = input("Digite o biotipo (Ectomorfo, Mesomorfo, Endomorfo): ")
dias_treino = int(input("Digite o número de dias disponíveis para treino: "))
tipo_exercicio = input("Digite o tipo de exercício preferido (Funcional, Maquinário, Peso Livre, Cardio, HIIT): ")

print(gerar_plano_treino(biotipo, dias_treino, tipo_exercicio))
def gerar_plano_treino(biotipo, dias_treino, tipo_exercicio):
    # Dicionário para plano de treino baseado no biotipo
    planos = {
        "Ectomorfo": {
            "Funcional": "Treino funcional focado em ganho de força e resistência com ênfase em exercícios compostos.",
            "Maquinário": "Treino com máquinas para ganho de massa muscular, focado em grandes grupos musculares.",
            "Peso Livre": "Treino com pesos livres para hipertrofia e força, com cargas progressivas.",
            "Cardio": "Cardio leve para aumentar a resistência cardiovascular sem perda de massa muscular.",
            "HIIT": "Treino HIIT moderado para aumentar a resistência sem impacto na massa magra."
        },
        "Mesomorfo": {
            "Funcional": "Treino funcional equilibrado com foco em resistência e tonificação muscular.",
            "Maquinário": "Treino em máquinas com foco em hipertrofia e definição.",
            "Peso Livre": "Treino intenso com pesos livres para aumentar a massa e a definição muscular.",
            "Cardio": "Cardio moderado para manter o condicionamento físico.",
            "HIIT": "Treino HIIT intenso para queima de gordura e manutenção da massa muscular."
        },
        "Endomorfo": {
            "Funcional": "Treino funcional para queima de calorias e fortalecimento muscular.",
            "Maquinário": "Treino em máquinas com foco em perda de peso e tonificação.",
            "Peso Livre": "Treino com pesos livres, usando séries e repetições para queima de gordura.",
            "Cardio": "Cardio intenso para auxiliar na queima de gordura.",
            "HIIT": "HIIT focado em alta intensidade para maximizar a queima calórica."
        }
    }
    
    # Seleciona o plano de treino baseado no biotipo e no tipo de exercício
    treino_selecionado = planos.get(biotipo, {}).get(tipo_exercicio, "Plano de treino não disponível para essa combinação.")
    
    # Ajusta o plano com base nos dias disponíveis para treino
    plano_final = f"Plano de treino para um {biotipo} com {dias_treino} dias de treino focado em {tipo_exercicio}: {treino_selecionado}"
    return plano_final

# Exemplo de uso
biotipo = input("Digite o biotipo (Ectomorfo, Mesomorfo, Endomorfo): ")
dias_treino = int(input("Digite o número de dias disponíveis para treino: "))
tipo_exercicio = input("Digite o tipo de exercício preferido (Funcional, Maquinário, Peso Livre, Cardio, HIIT): ")

print(gerar_plano_treino(biotipo, dias_treino, tipo_exercicio))
