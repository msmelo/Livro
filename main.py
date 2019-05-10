import csv, os

if os.path.isfile('C:/Users/julia/Documents/Python/Livro/List.csv') == False:
    with open('C:/Users/julia/Documents/Python/Livro/List.csv','w') as f:
        fieldnames = ['Classification','Name','Ingredients','Observation']
        writing_the_rright = csv.DictWriter(f, fieldnames = fieldnames)
        writing_the_rright.writeheader()
if os.path.isfile('C:/Users/julia/Documents/Python/Livro/List.csv') == True:
    print("Bem vindo ao seu livro virtual de receitas! ")

first_command = "Escolha o que deseja fazer: "
possible_answers = ["1- Consultar uma receita","2- Escrever uma nova receita","3- Exit"]
possible_numbers = ["1","2"]
close_programm = ['3']

choice = None
while choice not in close_programm:
    print(first_command)
    for possible_answer in possible_answers:
        print(possible_answer)
    choice = float(input(">>> "))
    #Checking a recipe
    if choice == 1:
        print("Choose the recipe you want to see: ")
        with open('List.csv','r') as file:
            read_data = csv.DictReader(file)
            for row in read_data:
                print(row['Name'])
            choice_recipe = input (">>> ")
            file.seek(0)
            found = 0
            for row in read_data:
                if choice_recipe == row['Name']:
                    print(row['Name'] + "\n" + row['Classification'] + "\n" + "Ingredients: " + row['Ingredients'] + "\n" + "How to prepare: " + row['Observation'])
                else:
                    found = 1
            if found == 1:
                print ("Não encontramos a receita procurada. Tente novamente")
    #Writing a recipe
    elif choice == 2:
        with open('C:/Users/julia/Documents/Python/Livro/List.csv','a') as f:
            fieldnames = ['Classification','Name','Ingredients','Observation']
            thewriter = csv.DictWriter(f, fieldnames = fieldnames)
            pregunta = input("A sua receita é: \n1- Doce\n2- Salgada\n>>>  ")
            if float(pregunta) == 1:
                classification = 'Sweet'
            elif float(pregunta) == 2:
                classification = 'Salty'
            else:
                print("Please insert a valid number")

            name=input("What is the name of your recipe?\n>>> ")
            ingredients=input("What are the ingredients you need?\n>>> ")
            observation=input("How do you do it?\n>>> ")
            thewriter.writerow({'Classification':classification,'Name':name,'Ingredients':ingredients,'Observation':observation})
    elif choice == 3:
        exit()
