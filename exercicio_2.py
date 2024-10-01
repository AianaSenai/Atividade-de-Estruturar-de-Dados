def menu():
 def adicionar_familia():
  def exibir_resultados():

    while True:
       print("1 - Adicionar família")  
       print("2- Exibir resultados")
       print("3- Sair")

       opção = input("Escolha uma opção: ")

       if opção == "1":
           adicionar_familia()
       elif opção == "2":
           exibir_resultados()
       elif opção == "3":
            break
    else:
        print("Opção inválida.")

menu()