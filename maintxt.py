import os

print("Bem vindo ao seu livro virtual de receitas ")
first_command = "Escolha o que deseja fazer: "
possible_answers = ["1- Consultar uma receita","2- Escrever uma nova receita"]
possible_numbers = ["1","2"]

choice = None
while choice not in possible_numbers:
    print(first_command)
    for possible_answer in possible_answers:
        print(possible_answer)
    choice = input(">>> ")
choice = float(choice)
#Writing a recipe
if choice == 2:
    number_of_files = len(os.walk("C:/Users/julia/Documents/Python/Livro/List"))
    number_of_files = float(number_of_files)
    path_to_file = "C:/Users/julia/Documents/Python/Livro/List/"+ str(number_of_files) +".txt"
    print (path_to_file)
    name = input("Insira o nome da nova receita: ")
