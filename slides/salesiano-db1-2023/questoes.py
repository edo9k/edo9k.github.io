from os import system

def clear():
    system('clear') 

# Uma lista de dicionários que armazena as perguntas e as respostas
questions = [
    {
        "question": "O que é um banco de dados?",
        "answer": "Um banco de dados é uma coleção de dados que é organizada de forma que possa ser facilmente acessada, gerenciada e atualizada."
    },
    {
        "question": "O que é normalização no projeto de banco de dados?",
        "answer": "Normalização é um processo de organizar os dados em um banco de dados para reduzir a redundância e melhorar a integridade dos dados."
    },
    {
        "question": "O que é a primeira forma normal (1FN) na normalização?",
        "answer": "A primeira forma normal (1FN) é quando cada atributo (coluna) contém apenas valores atômicos e cada linha é única."
    },
    {
        "question": "O que é a segunda forma normal (2FN) na normalização?",
        "answer": "A segunda forma normal (2FN) é quando cada atributo (coluna) depende da chave primária inteira (um identificador único para cada linha)."
    },
    {
        "question": "O que é a terceira forma normal (3FN) na normalização?",
        "answer": "A terceira forma normal (3FN) é quando cada atributo (coluna) depende apenas da chave primária e não de nenhum outro atributo."
    },
    {
        "question": "O que é um diagrama de entidade relacionamento (DER)?",
        "answer": "Um diagrama de entidade relacionamento (DER) é uma representação gráfica das entidades (tabelas) e seus relacionamentos em um banco de dados."
    },
    {
        "question": "O que é um relacionamento um-para-um em um DER?",
        "answer": "Um relacionamento um-para-um é quando cada entidade em uma tabela está relacionada a uma e somente uma entidade em outra tabela."
    },
    {
        "question": "O que é um relacionamento um-para-muitos em um DER?",
        "answer": "Um relacionamento um-para-muitos é quando cada entidade em uma tabela está relacionada a zero ou mais entidades em outra tabela."
    },
    {
        "question": "O que é um relacionamento muitos-para-muitos em um DER?",
        "answer": "Um relacionamento muitos-para-muitos é quando cada entidade em uma tabela está relacionada a zero ou mais entidades em outra tabela, e vice-versa."
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

