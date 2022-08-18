import random

temp1 = True


#Função que estabelece os possíveis comandos oferecidos ao usuário
def commands():
    print("\nThese are all the commands available:")
    print(" show password;")
    print(" write password;")
    print(" exit;")
    print(" help;")

#Função responsavel pela visualização das senhas
def show_password(line):
    #abrir o documento onde se guardará ou está guardando as senhas
    with open("senhas.txt", 'r') as f:
        text = f.read()
        result_string = ''

        present = False
        #correção de formatação
        text2 = text.split("\n")
        for itemIndex in range(len(text2)):
            if line in text2[itemIndex]:
                present = True
                password_l = text2[itemIndex].split(': ')
                website = password_l[0]
                password_s = password_l[1]
                del password_l
                password = password_s.split(',')
                del password[-1]
                temp = ""
                for letter in password:
                    temp += chr(int(letter))
                print(website + ': ' + temp)
        
        if not present:
            print("No passwords found.")

#Função responsavel pela criação das senhas
def write_password(website):
    #abrir o documento onde se guardará ou está guardando as senhas
    s_passwords = open("senhas.txt", "a")
    password = ""
    #se estabelece que a senha tera entre 15 e 25 caractéres gerados aleátoriamente entre o decimal 33 e 126 da lista de Unicode
    for i in range(random.randint(15, 25)):
        password += str(random.randint(33, 126)) + ","
    line = '\n' + website + ": " + password
    s_passwords.write(line)


#Função responsavel por fechar o programa por input do usuário
def exit_program():
    global temp1
    temp1 = False


#Main loop onde terá inputs do usuário
print("Welcome to Davi\'s password encryptor!")
while True:
    #check da chave de acesso do usuário
    x = input("Your name: ")
    y = []
    for e in x:
        y.append(e)
    x = ""
    for i in y:
        x += str(ord(i))
    #guardado no próprio codigo fonde de forma incriptada nessa situação a chave seria "exemplo"
    if x == '101120101109112108111':
        while temp1:
            temp2 = input("\n Type help to view the available commands, or exit to exit the program: ")
            if temp2.lower() == "show password" or temp2.lower() == "show":
                print("\nWhich site?")
                specific_line = input("")
                show_password(specific_line.title())

            elif temp2.lower() == "write password" or temp2.lower() == "write":
                website = input("\nWebsite: ").title()
                write_password(website)

            elif temp2.lower() == "help":
                commands()

            elif temp2.lower() == "exit":
                exit_program()

            else:
                print("\nUnrecognizable command")

            continue
    else:
        break
