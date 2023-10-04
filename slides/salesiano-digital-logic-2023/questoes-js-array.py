from os import system

def clear():
    system('clear') 

# Uma lista de dicionários que armazena as perguntas e as respostas
questions = [
    {
        "question": "O que é push() em JavaScript?",
        "answer": "push() é uma função que adiciona um elemento ao final do array."
    },
    {
        "question": "O que é pop() em JavaScript?",
        "answer": "pop() é uma função que remove e retorna o último elemento do array."
    },
    {
        "question": "O que é shift() em JavaScript?",
        "answer": "shift() é uma função que remove e retorna o primeiro elemento do array."
    },
    {
        "question": "O que é unshift() em JavaScript?",
        "answer": "unshift() é uma função que adiciona elementos ao início do array."
    },
    {
        "question": "O que é indexOf() em JavaScript?",
        "answer": "indexOf() é uma função que retorna o índice de um elemento no array."
    },
    {
        "question": "O que é includes() em JavaScript?",
        "answer": "includes() é uma função que verifica se um elemento está no array."
    },
    {
        "question": "O que é slice() em JavaScript?",
        "answer": "slice() é uma função que retorna uma cópia de parte de um array."
    },
    {
        "question": "O que é forEach() em JavaScript?",
        "answer": "forEach() é uma função que executa uma função em cada elemento do array."
    },
    {
        "question": "O que é filter() em JavaScript?",
        "answer": "filter() é uma função que cria um novo array com elementos que passam em um teste."
    },
    {
        "question": "O que é map() em JavaScript?",
        "answer": "map() é uma função que cria um novo array com os resultados de uma função."
    },
    {
        "question": "O que é reduce() em JavaScript?",
        "answer": "reduce() é uma função que reduz um array a um único valor usando uma função."
    }
]



# Um laço que percorre a lista de perguntas
for q in questions:
    clear()
    print("\n\n")

    # Imprime a pergunta
    print(q["question"])
    # Espera o usuário pressionar enter
    input("\n --- ")

    # Imprime a resposta
    print("\n")
    print(q["answer"])
    # Espera o usuário pressionar enter
    input("\n\n\n --- (enter) -> ") 


clear()
print(" -- fim das questoes -- ") 

