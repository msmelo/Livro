import csv, os

try:
    os.path.isdir('C:/Users/julia/Documents/Python/Livro/Teste.csv')
    print('Certo!')
except False:
    with open('C:/Users/julia/Documents/Python/Livro/Teste.csv','w') as f:
        fieldnames = ['Classification','Name','Ingredients','Observation']
        writing_the_rright = csv.DictWriter(f, fieldnames = fieldnames)
        writing_the_rright.writeheader()
