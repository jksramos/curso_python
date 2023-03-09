"""
EXERCÍCIO:

-> Peça para o usuário digitar seu nome;
-> Peça para o usuário digitar sua idade;
    Se nome e idade forem digitados:
        Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}
    Se nada for digitado em nome e idade:
        Exiba:
            'Desculpe, você deixou campos vazios.'
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print('Seu nome Não contém espaços')
    
    n = len(nome)
    print(f'Seu nome contem {n} letras')
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')