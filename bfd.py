tarefas = [] ##teste
taf_pend = []
taf_conclu = []
escolha = 1
while(escolha !=5):
    if(escolha>5 or escolha<1):
      print("por favor selecione uma das opções!")
    else:
        print("digite 1 para adicionar tarefas:")
        print("digite 2 para listar tarefa como pendente:")
        print("digite 3 para listar tarefa como concluida:")
        print("digite 4 para remover tarefa:")
        print("digite 5 para sair:")
        escolha = int(input("opção:"))



        if(escolha==1): #funcao para adicionar
         nt = str(input("tarefa:"))
         tarefas.append(nt)
         print("tarefa adicionada com sucesso!")
        if(escolha==2):#funcao adicionar pendente
            if(len(tarefas)==0):
                print("nao possui tarefas!")
            else:
             for n in range(len(tarefas)):
                print(f"{n+1} {tarefas[n]}")
                esc2=int(input("numero da tarefa:"))
                taf_pend.append(tarefas[esc2 -1])
                print("tarefa adicionada a pendentes!")        
        if(escolha==3):#funcao adicionar como concluida
             if(len(tarefas)==0):
              print("nao possui tarefas!")
             else:
                for n in range(1,len(tarefas)):
                 print(f"{n+1} {tarefas[n]}")
                 esc3=int(input("numero da tarefa:"))
                 taf_conclu.append(tarefas[esc3-1])
                 print("tarefa adicionada a concluidas!") 
    if(escolha==4):#funcao para remover tarefas 
         if(len(tarefas)==0):
            print("nao possui tarefas!")
         else:
            for n in range(1,len(tarefas)):
             print(f"{n+1} {tarefas[n]}")
             esc4=int(input("numero da tarefa:"))
             tarefas.pop(tarefas[esc4 -1])
             print("tarefa removida com sucesso!")
    if(escolha==5):#funcao para sair
       if(len(tarefas)==0):
         print("nao possui tarefas!")
         break
print("FIM!")