from os import system
from rich.console import Console

console = Console()


def print(text):
    console.print(text, width=80, overflow="fold")


def clear():
    system("clear")


# perguntas e as respostas
questions = [
    {
        "question": "O que é JavaScript?",
        "answer": "JavaScript é uma linguagem de programação de alto nível, amplamente utilizada para criar interatividade em páginas web. Ela permite que os desenvolvedores adicionem comportamentos dinâmicos aos sites.",
    },
    {
        "question": "Explique o conceito de 'função' em JavaScript.",
        "answer": "Uma função em JavaScript é um bloco de código reutilizável que realiza uma tarefa específica. Ela é definida usando a palavra-chave 'function' e pode receber parâmetros, executar operações e retornar um valor.",
    },
    {
        "question": "O que é uma 'string' em JavaScript?",
        "answer": "Uma 'string' em JavaScript é uma sequência de caracteres, como texto. Ela é delimitada por aspas simples (') ou duplas (\"). Exemplo: 'Hello, World!'",
    },
    {
        "question": "Como declarar e inicializar uma variável em JavaScript?",
        "answer": "Você pode declarar uma variável usando 'let', 'const' ou 'var', seguido pelo nome da variável. Exemplo: 'let idade;' declara uma variável chamada 'idade'. Para inicializá-la, você pode atribuir um valor, como 'idade = 25;' ou fazer as duas etapas em uma linha, como 'let idade = 25;'",
    },
    {
        "question": "O que é 'undefined' em JavaScript?",
        "answer": "'undefined' em JavaScript significa que uma variável foi declarada, mas ainda não recebeu um valor. É o valor padrão atribuído automaticamente a variáveis que não foram inicializadas.",
    },
    {
        "question": "Explique o papel do operador '+' em JavaScript.",
        "answer": "O operador '+' em JavaScript é usado para adicionar números e concatenar strings. Quando aplicado a strings, ele as une. Exemplo: '2 + 3' resulta em 5, e '\"Hello\" + \"World\"' resulta em 'HelloWorld'.",
    },
    {
        "question": "O que são arrays em JavaScript?",
        "answer": "Arrays em JavaScript são estruturas de dados que armazenam coleções de elementos. Os elementos podem ser de diferentes tipos e são acessados por um índice numérico. Exemplo: 'let meuArray = [1, 2, 3];' cria um array com três elementos.",
    },
    {
        "question": "Qual é a diferença entre '==' e '===' em JavaScript?",
        "answer": "'==' compara os valores de duas variáveis, convertendo os tipos se necessário. '===' compara os valores e os tipos, garantindo uma correspondência exata. Recomenda-se usar '===' para evitar comparações inesperadas.",
    },
    {
        "question": "O que é um objeto em JavaScript?",
        "answer": "Um objeto em JavaScript é uma estrutura de dados que armazena pares chave-valor. As chaves são strings e os valores podem ser de qualquer tipo. Exemplo: 'let pessoa = { nome: 'João', idade: 30 };' cria um objeto com duas propriedades.",
    },
    {
        "question": "Como funcionam os loops 'for' em JavaScript?",
        "answer": "Os loops 'for' em JavaScript executam um bloco de código repetidamente por um número específico de vezes. Eles consistem em uma inicialização, uma condição de continuação e uma expressão de incremento. Exemplo: 'for (let i = 0; i < 5; i++) { console.log(i); }' imprime os números de 0 a 4.",
    },
    {
        "question": "O que é o método 'filter' em JavaScript e como ele é usado?",
        "answer": "O método 'filter' em JavaScript é usado para criar um novo array contendo apenas os elementos que atendem a uma condição específica. Ele recebe uma função de callback que determina se cada elemento deve ser incluído no novo array.",
    },
    {
        "question": "Explique o conceito de 'map' em JavaScript e como aplicá-lo.",
        "answer": "Em JavaScript, o método 'map' é utilizado para criar um novo array aplicando uma função a cada elemento do array original. Essa função pode realizar transformações nos elementos, gerando um array resultante.",
    },
    {
        "question": "O que é o método 'reduce' e como ele funciona em JavaScript?",
        "answer": "O método 'reduce' em JavaScript é usado para reduzir os elementos de um array a um único valor. Ele recebe uma função de callback que acumula os resultados, além de um valor inicial opcional. O 'reduce' executa a função para cada elemento, acumulando o resultado ao longo do processo.",
    },
    {
        "question": "O que é uma lista encadeada simples em estruturas de dados?",
        "answer": "Uma lista encadeada simples é uma estrutura de dados onde cada elemento, chamado nó, armazena um valor e uma referência ao próximo nó na sequência. O último nó geralmente aponta para null, indicando o final da lista.",
    },
    {
        "question": "Explique o conceito de lista duplamente encadeada em estruturas de dados.",
        "answer": "Uma lista duplamente encadeada é uma estrutura em que cada nó contém um valor e referências tanto para o próximo quanto para o nó anterior na sequência. Isso permite a navegação bidirecional na lista, proporcionando maior flexibilidade em algumas operações.",
    },
    {
        "question": "O que caracteriza uma lista duplamente encadeada circular com descritor?",
        "answer": "Uma lista duplamente encadeada circular com descritor é uma variação da lista duplamente encadeada. Nessa estrutura, o último nó aponta para o primeiro, formando um ciclo, e um descritor mantém informações sobre a lista, como o número de elementos. Essa configuração facilita operações de inserção e remoção no início e no final da lista.",
    },
    {
        "question": "Explique o método 'push' da classe Array em JavaScript e como ele é usado.",
        "answer": "O método 'push' em JavaScript é utilizado para adicionar um ou mais elementos ao final de um array. Ele modifica o array original e retorna o novo comprimento do array. Como você aplicaria o método 'push' para adicionar um elemento ao final de um array existente?",
    },
    {
        "question": "Qual é a função do método 'pop' na classe Array e como ele é implementado?",
        "answer": "O método 'pop' é utilizado para remover o último elemento de um array. Ele altera o array original e retorna o elemento removido. Como você usaria o método 'pop' para extrair o último elemento de um array e armazená-lo em uma variável?",
    },
    {
        "question": "Descreva o método 'join' da classe Array em JavaScript e seu propósito.",
        "answer": "O método 'join' é usado para converter os elementos de um array em uma string, concatenando-os com um separador especificado. Explique como o método 'join' funciona e forneça um exemplo de uso com um array e um separador de sua escolha.",
    },
    {
        "question": "O que o método 'find' da classe Array faz e em que situações ele é útil?",
        "answer": "O método 'find' é utilizado para encontrar o primeiro elemento em um array que satisfaça uma condição fornecida por uma função de callback. Como você aplicaria o método 'find' para localizar o primeiro elemento em um array que atenda a uma condição específica? Forneça um exemplo.",
    },
]  # fecha o array


def exportar():
    """Exporta questões e respostar para o formato markdown."""

    def json_to_markdown(data):
        markdown_content = ""
        for item in data:
            markdown_content += f"""
## Pergunta: 

{item['question']}

### Resposta:

{item['answer']}

<hr>        
            """
        return markdown_content

    # Converter dados para Markdown
    markdown_output = json_to_markdown(questions)

    # Salvar o conteúdo em um arquivo Markdown
    with open("questoes-novembro-2023.md", "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_output)

    print("Documento Markdown gerado com sucesso!")


def apresentar():
    """Mostra questões e respostas etapa por etapa."""
    contador = 1
    total = len(questions)

    # Um laço que percorre a lista de perguntas
    for q in questions:
        clear()
        print(f"\n --- questão {contador} de {total} ---\n\n\n")

        # Imprime a pergunta
        print(q["question"])
        # Espera o usuário pressionar enter
        input("\n --- ")

        # Imprime a resposta
        print("\n")
        print(q["answer"])
        # Espera o usuário pressionar enter

        input(f"\n\n\n próxima -> ")
        contador = contador + 1

    clear()
    print(" -- fim das questoes -- ")


exportar()
# apresentar()
