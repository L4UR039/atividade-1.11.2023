class Professor:
    def __init__(self):
        self.disciplinas = []
        self.atividades = []
        self.datas = []
    
    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
    
    def adicionar_atividade(self, disciplina, atividade, data):
        if disciplina in self.disciplinas and data not in self.datas:
            self.atividades.append((disciplina, atividade, data))
            self.datas.append(data)
    
    def marcar_atividade_concluida(self, disciplina, atividade, data):
        if (disciplina, atividade, data) in self.atividades:
            self.atividades.remove((disciplina, atividade, data))
    
    def listar_atividades_em_aberto(self):
        return [(disciplina, atividade, data) for disciplina, atividade, data in self.atividades]
    
    def listar_atividades_concluidas(self):
        concluidas = []
        for disciplina, atividade, data in self.atividades:
            if (disciplina, atividade, data) not in concluidas:
                concluidas.append((disciplina, atividade, data))
        return concluidas


professor = Professor()

while True:
    print("Menu:")
    print("1. Adicionar disciplina")
    print("2. Adicionar atividade")
    print("3. Marcar atividade como concluída")
    print("4. Listar atividades em aberto")
    print("5. Listar atividades concluídas")

    opção = int(input("Escolha uma opção: "))

    if opção == 1:
        disciplina = input("Digite o nome da disciplina: ")
        professor.adicionar_disciplina(disciplina)
    
    elif opção == 2:
        disciplina = input("Digite o nome da disciplina: ")
        atividade = input("Digite o nome da atividade: ")
        data = input("Digite a data da atividade: ")
        professor.adicionar_atividade(disciplina, atividade, data)
    
    elif opção == 3:
        disciplina = input("Digite o nome da disciplina: ")
        atividade = input("Digite o nome da atividade: ")
        data = input("Digite a data da atividade: ")
        professor.marcar_atividade_concluida(disciplina, atividade, data)
    
    elif opção == 4:
        atividades_em_aberto = professor.listar_atividades_em_aberto()
        print("Atividades em aberto:")
        for disciplina, atividade, data in atividades_em_aberto:
            print(f"Disciplina: {disciplina}, Atividade: {atividade}, Data: {data}")
    
    elif opção == 5:
        atividades_concluidas = professor.listar_atividades_concluidas()
        print("Atividades concluídas:")
        for disciplina, atividade, data in atividades_concluidas:
            print(f"Disciplina: {disciplina}, Atividade: {atividade}, Data: {data}")
    
    else:
        break
