tarefas = []  ##teste
taf_pend = []
taf_conclu = []
escolha = 0

while(escolha != 5):
    print("digite 1 para adicionar tarefas:")
    print("digite 2 para listar tarefa como pendente:")
    print("digite 3 para listar tarefa como concluida:")
    print("digite 4 para remover tarefa:")
    print("digite 5 para sair:")
    escolha = int(input("opção:"))

    if(escolha > 5 or escolha < 1):
        print("por favor selecione uma das opções!")
    else:
        if(escolha == 1):  # funcao para adicionar
            nt = str(input("tarefa:"))
            tarefas.append(nt)
            print("tarefa adicionada com sucesso!")

        if(escolha == 2):  # funcao adicionar pendente
            if(len(tarefas) == 0):
                print("nao possui tarefas!")
            else:
                for n in range(len(tarefas)):
                    print(f"{n+1} {tarefas[n]}")
                esc2 = int(input("numero da tarefa:"))
                if 1 <= esc2 <= len(tarefas):
                    taf_pend.append(tarefas[esc2 - 1])
                    print("tarefa adicionada a pendentes!")
                else:
                    print("Número inválido!")

        if(escolha == 3):  # funcao adicionar como concluida
            if(len(tarefas) == 0):
                print("nao possui tarefas!")
            else:
                for n in range(len(tarefas)):
                    print(f"{n+1} {tarefas[n]}")
                esc3 = int(input("numero da tarefa:"))
                if 1 <= esc3 <= len(tarefas):
                    taf_conclu.append(tarefas[esc3 - 1])
                    print("tarefa adicionada a concluidas!")
                else:
                    print("Número inválido!")

        if(escolha == 4):  # funcao para remover tarefas
            if(len(tarefas) == 0):
                print("nao possui tarefas!")
            else:
                for n in range(len(tarefas)):
                    print(f"{n+1} {tarefas[n]}")
                esc4 = int(input("numero da tarefa:"))
                if 1 <= esc4 <= len(tarefas):
                    tarefas.pop(esc4 - 1)
                    print("tarefa removida com sucesso!")
                else:
                    print("Número inválido!")

print("FIM!")
