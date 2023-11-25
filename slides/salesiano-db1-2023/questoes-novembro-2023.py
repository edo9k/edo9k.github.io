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
        "question": "O que é a cláusula SELECT no SQL e qual é o seu propósito principal?",
        "answer": "A cláusula SELECT é utilizada para recuperar dados de uma ou mais tabelas em um banco de dados SQL. Ela é fundamental para consultas.",
    },
    {
        "question": "Explique o uso do operador WHERE na cláusula SELECT do SQL.",
        "answer": "O operador WHERE é utilizado para filtrar os resultados de uma consulta. Ele especifica uma condição que as linhas devem atender para serem incluídas no conjunto de resultados.",
    },
    {
        "question": "Como o operador DISTINCT é empregado em conjunto com a cláusula SELECT?",
        "answer": "O operador DISTINCT é usado para retornar valores únicos em uma coluna específica. Ele elimina duplicatas, deixando apenas valores distintos no conjunto de resultados.",
    },
    {
        "question": "Qual é a função do operador ORDER BY na cláusula SELECT e como ele é utilizado?",
        "answer": "O operador ORDER BY é utilizado para classificar os resultados de uma consulta com base em uma ou mais colunas. Pode ser usado para classificar em ordem ascendente (ASC) ou descendente (DESC).",
    },
    {
        "question": "Explique o uso do operador LIKE no SQL e em que situações ele é útil.",
        "answer": "O operador LIKE é utilizado para realizar pesquisas de padrões em dados de texto. Ele permite a utilização de curingas, como '%' para representar qualquer conjunto de caracteres.",
    },
    {
        "question": "O que são operadores de comparação e como eles são aplicados na cláusula WHERE do SQL?",
        "answer": "Operadores de comparação, como '=', '<>', '<', '>', '<=', '>=', são utilizados na cláusula WHERE para comparar valores. Eles ajudam a especificar condições para a seleção de dados.",
    },
    {
        "question": "Como o operador IN é utilizado na cláusula SELECT e quais são os benefícios de sua aplicação?",
        "answer": "O operador IN é usado para filtrar resultados com base em uma lista de valores. Ele simplifica consultas que precisam comparar uma coluna com múltiplos valores possíveis.",
    },
    {
        "question": "Explique a função do operador BETWEEN na cláusula WHERE e dê um exemplo de sua aplicação.",
        "answer": "O operador BETWEEN é utilizado para selecionar valores dentro de um intervalo específico. Ele é útil para filtrar dados em que uma coluna deve estar entre dois valores dados.",
    },
    {
        "question": "Como o operador LIMIT é utilizado em consultas SQL e qual é o propósito principal?",
        "answer": "O operador LIMIT é utilizado para restringir o número de linhas retornadas em uma consulta. Ele é útil para limitar o tamanho do conjunto de resultados, especialmente em consultas que podem retornar muitos registros.",
    },
    {
        "question": "O que significa a cláusula IS NULL em uma consulta SQL e em que situações ela é aplicada?",
        "answer": "A cláusula IS NULL é utilizada para filtrar resultados onde um determinado campo não possui um valor atribuído, ou seja, é nulo. Isso é útil para encontrar registros que não tenham dados em uma coluna específica.",
    },
    {
        "question": "Explique o uso dos tipos de dados INT, FLOAT, CHAR, VARCHAR, DATE e TIME em bancos de dados SQL (com exemplos).",
        "answer": """
        INT   -> utilizados para armazenar números inteiros
        FLOAT -> empregado para números de ponto flutuante
        CHAR  -> utilizado para armazenar strings de tamanho fixo
        VARCHAR -> usado para strings de tamanho variável 
        DATE  -> empregado para armazenar datas, 
        TIME  -> armazenar informações de horário.""",
    },
    {
        "question": "Explique a importância dos índices em um banco de dados.",
        "answer": "Os índices facilitam a rápida localização de registros, reduzem o tempo de busca e melhoram a eficiência das consultas. Por exemplo, ao criar um índice em uma coluna 'Nome' de uma tabela 'Clientes', as consultas que envolvem a ordenação ou busca por nomes serão executadas de maneira mais eficiente.",
    },
    {
        "question": "Qual é a diferença entre chaves primárias e chaves estrangeiras em um contexto de banco de dados relacional?",
        "answer": "Chaves primárias são usada para identificar exclusivamente cada registro em uma tabela, enquanto a chave estrangeira estabelece uma relação entre duas tabelas, referenciando a chave primária de outra tabela. Por exemplo, em um banco de dados com tabelas 'Clientes' e 'Pedidos', a chave primária 'IDCliente' na tabela 'Clientes' pode ser referenciada como chave estrangeira na tabela 'Pedidos', estabelecendo assim uma relação entre os dois conjuntos de dados.",
    },
    {
        "question": "O que é a primeira regra de normalização de dados (1ª Forma Normal) e qual é o seu objetivo ao projetar um banco de dados?",
        "answer": "A primeira regra de normalização, ou 1ª Forma Normal, exige que cada coluna de uma tabela contenha apenas valores atômicos, indivisíveis. O objetivo é evitar a repetição de dados e garantir a integridade dos dados ao projetar um banco de dados.",
    },
    {
        "question": "Explique a segunda regra de normalização de dados (2ª Forma Normal) e em que cenário ela se aplica?",
        "answer": "A segunda regra de normalização, ou 2ª Forma Normal, estabelece que uma tabela deve estar na 1ª Forma Normal e que todos os atributos não chave devem ser totalmente dependentes da chave primária. Isso é especialmente aplicável quando há uma chave primária composta, e os atributos dependem apenas de parte dessa chave.",
    },
    {
        "question": "O que é a terceira regra de normalização de dados (3ª Forma Normal) e por que é importante na modelagem de bancos de dados?",
        "answer": "A terceira regra de normalização, ou 3ª Forma Normal, afirma que uma tabela deve estar na 2ª Forma Normal e que não deve haver dependências transitivas. Isso significa que os atributos não chave devem depender apenas da chave primária. A 3ª Forma Normal é crucial para reduzir redundâncias e melhorar a consistência dos dados na modelagem de bancos de dados.",
    },
    {
        "question": "O que são 'Collation' e 'Charset' em um banco de dados, e qual é a importância de especificar corretamente esses elementos durante a criação de tabelas?",
        "answer": "Em um banco de dados, 'Collation' refere-se às regras de ordenação e comparação de caracteres, enquanto 'Charset' (conjunto de caracteres) define o conjunto de caracteres utilizado para armazenar dados. É crucial especificar corretamente 'Collation' e 'Charset' durante a criação de tabelas para garantir que as operações de ordenação e comparação sejam realizadas de maneira consistente, e que os dados sejam armazenados e recuperados adequadamente, evitando problemas de codificação e ordenação inconsistentes.",
    },
    {
        "question": "Explique a instrução SQL CREATE e de um exemplo de como usá-la.",
        "answer": """A instrução SQL CREATE é utilizada para criar diversos objetos em um banco de dados. Um dos principais objetos que podem ser criados são tabelas. Por exemplo, uma 'Clientes' com as colunas 'ID', 'Nome' e 'Email', pode ser criada com o seguinte comando: 


        CREATE TABLE Clientes (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Nome VARCHAR(50) NOT NULL,
            Email VARCHAR(100) UNIQUE
        );""",
    },
    {
        "question": "Explique o uso da instrução SQL INSERT INTO e dê um exemplo do seu uso.",
        "answer": """A instrução SQL INSERT INTO é utilizada para adicionar novos registros a uma tabela existente em um banco de dados. Essa instrução é aplicada quando você deseja adicionar dados a uma tabela, seja para inicializar registros, atualizar dados ou adicionar novas entradas. 
    Por exemplo, para inserir um novo cliente na tabela 'Clientes' com um ID, Nome e Email específicos, você pode usar a seguinte instrução:

    INSERT INTO Clientes (ID,  Nome          , Email             ) 
    VALUES 
                         (1 ,  'João Silva'  , 'jsilva@email.com'),
                         (2 ,  'Maria Silva' , 'msilva@email.com');
    """,
    },
    {
        "question": "Explique o conceito de JOIN em SQL e dê um exemplo do seu uso.",
        "answer": """Em SQL, a cláusula JOIN é utilizada para combinar dados de duas ou mais tabelas com base em uma condição de relação. Essa técnica é aplicada quando você precisa reunir informações de tabelas relacionadas para realizar consultas mais complexas. 
    Por exemplo, para obter dados combinados de clientes e pedidos de vendas, onde as tabelas 'Clientes' e 'Pedidos' estão relacionadas pelo 'ID do Cliente', você pode usar a seguinte instrução:

    SELECT Clientes.Nome, Pedidos.NumeroPedido
    FROM Clientes
    JOIN Pedidos ON Clientes.ID = Pedidos.IDCliente;
    """,
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
