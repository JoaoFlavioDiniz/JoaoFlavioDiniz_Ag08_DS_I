
import os

def pesquisa_tudoweb(numero_entrevistados):
    """
    Pesquisa de satisfação utilizando FOR.
    """
    print("="*10 + "  PESQUISA DE SATISFAÇÃO - TudoWeb  " + "="*10)    

    # Inicializar contadores
    contador_excelente = 0
    contador_ruim = 0

    # FOR para coletar os dados
    for i in range(1, numero_entrevistados + 1):
        print(f"--- Entrevistado {i} ---")
        
        nome = input("Digite seu nome: ")
        
        # Validar idade (número)
        while True:
            try:
                idade = int(input(f"Digite sua idade {nome}: "))
                if idade > 0:
                    break
                else:
                    print(f"Por favor {nome}, digite uma idade válida (maior que zero).")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro por favor.")

        # Coleta Opinião
        print("\nOpinião sobre o atendimento prestado:")
        print("1: EXCELENTE")
        print("2: BOM")
        print("3: RUIM")
        
        while True:
            opiniao = input("Digite o número que expressa a sua opinião: ")
            
            # verificar e validar a opinião
            if opiniao == '1':
                contador_excelente += 1
                break 
            elif opiniao == '2':
                # Opção BOM precisa ser válida
                break
            elif opiniao == '3':
                contador_ruim += 1
                break
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

        # Limpar a tela     
        print("-" * 30 + "\n")
    os.system('cls' if os.name == 'nt' else 'clear')

    # --- Exibe o resultado final    
    print("\n" + "="*10 + "  RESULTADO FINAL DA PESQUISA  " + "="*10)
    print("\n")
    
    print(f"a) Quantidade de respostas 'EXCELENTE' (Opção 1): {contador_excelente}")
    
    print(f"b) Quantidade de respostas 'RUIM' (Opção 3)     : {contador_ruim}")   
    
    print("\n")
    print(f"="*10 + "  Obrigado pela participação!  " + "="*10)
    print("\n")   

# TESTE COM 10, mas posso usar qualquer valor como 50 que foi pedido

if __name__ == "__main__":
    
    TOTAL_ENTREVISTADOS_TESTE = 10
    #Comente a linha de cima e descomente a linha abaixo para realizar o teste com 50 pessoas
    #TOTAL_ENTREVISTADOS = 50
    
    # Para testar altere o valor da variável TOTAL_ENTREVISTADOS
    pesquisa_tudoweb(TOTAL_ENTREVISTADOS_TESTE)
    #Comente a linha de acima e descomente a linha baixo para realizar o teste 50 vezes
    #pesquisa_tudoweb(TOTAL_ENTREVISTADOS)
    