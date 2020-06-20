import json
import os
users = {}
costumers = {}
op = 99

if os.path.isfile("users.json"): # caso já exista o arquivo
    f = open("users.json", "r")
    data = json.load(f)
    f.close()
    #print (data)
    h = open("max_users.json", "r")
    number_users = json.load(h)
    h.close()
    if number_users["number_users"] == "2":
        print("Não é possível cadastrar mais do que 2 users")
    else:
        login = input("Digite o nome do usuário:  ")
        password = input("Digite a senha:  ")
        users[login] = password
        if login in data: # caso já exista um usuário com esse nome
            print("usuário já cadastrado")
        else:
            data[login] = password
            f = open("users.json", "w")
            json.dump(data, f)
            f.close()
            h = open("max_users.json","w")
            number_users = {"number_users": "2"}
            json.dump(number_users,h)
            h.close
else: # Criar arquivo, caso não exista
    login = input("Digite o nome do usuário:  ")
    password = input("Digite a senha:  ")
    if os.path.isfile("users.json"):
        users[login] = password
        f = open("users.json","w") # w = write = escrita
        json.dump(users, f)
        f.close()
        h = open("max_users.json","w")
        number_users = {"number_users": "1"}
        json.dump(number_users,h)
        h.close

#------------------------------------------------------------------------------------------------#

login = input("Digite o nome do usuário:  ")
password = input("Digite a senha:  ")
#l =open("users.json", "r")
#data =json.load(l)
#user[login] = password

if os.path.isfile("costumers.json"): # caso já exista o arquivo
    j = open("costumers.json", "r")
    datapet = json.load(j)
    j.close()
    #print (data)  
    nome = input("Digite o nome do usuário:  ")
    endereco = input("Digite o endereço:  ")
    telefone = input("Digite o telefone:  ")
    registered_by = login
    if nome in datapet: # caso já exista um usuário com esse nome
        print("Cliente já cadastrado")
    else:
        costumers[nome] = {'endereco': endereco,'fone' : telefone,'registrado' : registered_by}
        j = open("costumers.json", "w")
        json.dump(costumers, j)
        j.close()
else: # Criar arquivo, caso não exista
    nome = input("Digite o nome do usuário:  ")
    endereco = input("Digite o endereço:  ")
    telefone = input("Digite o telefone:  ")
    registered_by = users[login]
    costumers[nome] = {'endereco': endereco,'fone' : telefone,'registrado' : registered_by}
    j = open("costumers.json","w") # w = write = escrita
    json.dump(costumers, j)
    j.close()
    