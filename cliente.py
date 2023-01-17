import requests, json

res = requests.get('http://localhost:8000/banco/api/')
print(res.status_code)
response = json.loads(res.text)
#print(response)

while True:
    print("\nAPI de acesso ao banco de questões\n")
    cont = 0
    for api in response:        
        print('\t['+str(cont+1)+']' +str( response[cont].get('title')))
        cont+=1


    print("\t[0] Sair\n")

    x = int(input('digite uma opção:\n\t'))
    

    if x == 0:
        break
    cont = 0
    for api in response:
        if x == cont+1:            
            while True:
                print("API: " + response[cont].get('title'))

                request = requests.get(response[cont].get('url'))
                print(res.status_code)
                lista = json.loads(request.text)                
                
                cont2 = 0
                for point in lista:
                    if response[cont].get('title') == "Questôes Discursivas":
                        while True:
                            print('\n\t [1] Listar perguntas'+
                                '\n\t [2] Cadastrar pergunta'+
                                '\n\t [0] Sair'
                                )
                            op2 = int(input("Selecione uma opção:\n\t"))
                            if op2 == 0:
                                break
                            if op2 == 1:
                                request2 = requests.get('http://127.0.0.1:8080/discursivas/pergunta/')
                                lista2 = json.loads(request2.text)
                                for pergunta in lista2:
                                    print(pergunta)
                            
                            if op2 == 2:
                                titulo = input('DIgite um titulo:\n')
                                perg = input('Digite uma pergunta:\n')
                                resp = input('Digite uma resposta:\n')
                                jsont = {
                                    'titulo': titulo,
                                    'pergunta': perg,
                                    'resposta': resp,
                                    'lista': 1
                                }
                                request2 = requests.post('http://127.0.0.1:8080/discursivas/pergunta/', json=jsont)
                                lista2 = json.loads(request2.text)
                                for pergunta in lista2:
                                    print(pergunta)
                        break

                    if response[cont].get('title') == "Questôes Multipla Escolha":
                        while True:
                            print('\n\t [1] Listar questões'+
                                '\n\t [2] Cadastrar questão'+
                                '\n\t [3] Listar alternativas'+
                                '\n\t [4] Cadastrar alternativa'+
                                '\n\t [0] Sair'
                                )
                            op2 = int(input("Selecione uma opção:\n\t"))
                            if op2 == 0:
                                break
                            if op2 == 1:
                                request2 = requests.get('http://localhost:8085/mescolha/questao/')
                                lista2 = json.loads(request2.text)
                                for pergunta in lista2:
                                    print(pergunta)
                            
                            if op2 == 2:
                                titulo = input('Digite um titulo:\n')
                                perg = input('Digite uma pergunta:\n')                                
                                jsont = {
                                    'titulo': titulo,
                                    'pergunta': perg,                                    
                                    'lista': 1
                                }
                                request2 = requests.post('http://localhost:8085/mescolha/questao/', json=jsont)                                
                                
                            if op2 == 3:
                                request2 = requests.get('http://localhost:8085/mescolha/alternativa/')
                                lista2 = json.loads(request2.text)
                                for alt in lista2:
                                    print(alt)

                            if op2 == 4:
                                texto = input('Digite o texto da alternativa:\n')
                                correta = bool(input('Essa alternativa está correta?  True/False: '))
                                id = int(input('Digite o id de uma questão'))
                                jsont = {
                                    'texto': texto,
                                    'correta': correta,
                                    'questao': id
                                }
                                request2 = requests.post('http://localhost:8085/mescolha/alternativa/', json=jsont)

                        break
                        

                    cont+=1

                print("\t[0] Sair\n")

                op = int(input("Selecione uma opção:\n\t"))
                if op == 0:
                    break
                if op == 1:
                    request = requests.get(response[cont].get('url'))
                    print(res.status_code)
                    dict = json.loads(request.text)
                    print(dict)
                
                if op == 2:                    
                    #request = requests.post(response[cont].get('url'))
                    #print(res.status_code)
                    #dict = json.loads(request.text)
                    #print(dict)
                    pass
            break
        cont+=1





#res = requests.get('http://localhost:8000/banco/api/')
#response = json.loads(res.text)
#print("fetch api: "+ response[cont].get('title') +res.status_code)

   # while True:
   #     print(
   #     "API de acesso ao banco de questões\n" +
   #     "\t[1] Acessar api de questões discursivas" +
   #     "\t[2] Acessar api de queestões multipla escolha" +
   #     "\t[0] Sair\n"
   # )
   # x = int(input('digite uma opção:\n\t'))
    
