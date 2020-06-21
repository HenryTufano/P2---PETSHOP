import json
import os
users = {}
costumers = {}
pets = {}
op = 99
while op != 0:
    print("SISTEMA DE CONTROLE - PETIKÃO\n[1] - FAZER LOGIN\n[2] - CADASTRAR USUÁRIO\n[0] - FINALIZAR O PROGRAMA")
    op = int(input("Escolha uma opção: "))
    if op ==1:
        login = input("Digite o nome do usuário:  ")
        password = input("Digite a senha:  ")
        l =open("users.json", "r")
        data =json.load(l)
        if login in data :
            if data[login] == password and data[password] == login:
                print('deu certo')
            else :
                print('erro')
        else:
            print('login nao encontrado!')

    elif op == 2:
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
