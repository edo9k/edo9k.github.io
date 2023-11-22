from os import system
from rich.console import Console

console = Console() 

def print(text):
    console.print(text, width=80, overflow="fold") 

def clear():
    system('clear') 

# perguntas e as respostas
questions =  [
  {
    "question": "O que é a cláusula SELECT no SQL e qual é o seu propósito principal?",
    "answer": "A cláusula SELECT é utilizada para recuperar dados de uma ou mais tabelas em um banco de dados SQL. Ela é fundamental para consultas."
  },
  {
    "question": "Explique o uso do operador WHERE na cláusula SELECT do SQL.",
    "answer": "O operador WHERE é utilizado para filtrar os resultados de uma consulta. Ele especifica uma condição que as linhas devem atender para serem incluídas no conjunto de resultados."
  },
  {
    "question": "Como o operador DISTINCT é empregado em conjunto com a cláusula SELECT?",
    "answer": "O operador DISTINCT é usado para retornar valores únicos em uma coluna específica. Ele elimina duplicatas, deixando apenas valores distintos no conjunto de resultados."
  },
  {
    "question": "Qual é a função do operador ORDER BY na cláusula SELECT e como ele é utilizado?",
    "answer": "O operador ORDER BY é utilizado para classificar os resultados de uma consulta com base em uma ou mais colunas. Pode ser usado para classificar em ordem ascendente (ASC) ou descendente (DESC)."
  },
  {
    "question": "Explique o uso do operador LIKE no SQL e em que situações ele é útil.",
    "answer": "O operador LIKE é utilizado para realizar pesquisas de padrões em dados de texto. Ele permite a utilização de curingas, como '%' para representar qualquer conjunto de caracteres."
  },
  {
    "question": "O que são operadores de comparação e como eles são aplicados na cláusula WHERE do SQL?",
    "answer": "Operadores de comparação, como '=', '<>', '<', '>', '<=', '>=', são utilizados na cláusula WHERE para comparar valores. Eles ajudam a especificar condições para a seleção de dados."
  },
  {
    "question": "Como o operador IN é utilizado na cláusula SELECT e quais são os benefícios de sua aplicação?",
    "answer": "O operador IN é usado para filtrar resultados com base em uma lista de valores. Ele simplifica consultas que precisam comparar uma coluna com múltiplos valores possíveis."
  },
  {
    "question": "Explique a função do operador BETWEEN na cláusula WHERE e dê um exemplo de sua aplicação.",
    "answer": "O operador BETWEEN é utilizado para selecionar valores dentro de um intervalo específico. Ele é útil para filtrar dados em que uma coluna deve estar entre dois valores dados."
  }, 
  {
    "question": "Qual é a função do operador ORDER BY na cláusula SELECT do SQL e como ele é utilizado?",
    "answer": "O operador ORDER BY é utilizado para classificar os resultados de uma consulta com base em uma ou mais colunas. Pode ser usado para classificar em ordem ascendente (ASC) ou descendente (DESC)."
  },
  {
    "question": "Como o operador LIMIT é utilizado em consultas SQL e qual é o propósito principal?",
    "answer": "O operador LIMIT é utilizado para restringir o número de linhas retornadas em uma consulta. Ele é útil para limitar o tamanho do conjunto de resultados, especialmente em consultas que podem retornar muitos registros."
  },
  {
    "question": "O que significa a cláusula IS NULL em uma consulta SQL e em que situações ela é aplicada?",
    "answer": "A cláusula IS NULL é utilizada para filtrar resultados onde um determinado campo não possui um valor atribuído, ou seja, é nulo. Isso é útil para encontrar registros que não tenham dados em uma coluna específica."
  },
  {
    "question": "Qual é a função do operador ORDER BY na cláusula SELECT do SQL e como ele é utilizado?",
    "answer": "O operador ORDER BY é utilizado para classificar os resultados de uma consulta com base em uma ou mais colunas. Pode ser usado para classificar em ordem ascendente (ASC) ou descendente (DESC)."
  },
  {
    "question": "Como o operador LIMIT é utilizado em consultas SQL e qual é o propósito principal?",
    "answer": "O operador LIMIT é utilizado para restringir o número de linhas retornadas em uma consulta. Ele é útil para limitar o tamanho do conjunto de resultados, especialmente em consultas que podem retornar muitos registros."
  },
  {
    "question": "O que significa a cláusula IS NULL em uma consulta SQL e em que situações ela é aplicada?",
    "answer": "A cláusula IS NULL é utilizada para filtrar resultados onde um determinado campo não possui um valor atribuído, ou seja, é nulo. Isso é útil para encontrar registros que não tenham dados em uma coluna específica."
  },
  {
    "question": "Explique o uso dos tipos de dados INT, FLOAT, CHAR, VARCHAR, DATE e TIME em bancos de dados SQL, fornecendo exemplos de situações em que cada um é apropriado.",
    "answer": "Os tipos de dados INT são utilizados para armazenar números inteiros, como identificadores únicos. FLOAT é empregado para números de ponto flutuante, adequado para representar valores decimais. CHAR é utilizado para armazenar strings de tamanho fixo, enquanto VARCHAR é usado para strings de tamanho variável. DATE é empregado para armazenar datas, e TIME para armazenar informações de horário. Por exemplo, um campo DATE pode ser usado para armazenar a data de nascimento de uma pessoa, enquanto um campo TIME pode armazenar o horário de registro de um evento."
  },
  {
    "question": "O que é uma cláusula JOIN em SQL e como ela é utilizada para combinar dados de múltiplas tabelas? Dê um exemplo prático de situação em que um JOIN seria aplicado.",
    "answer": "A cláusula JOIN em SQL é utilizada para combinar dados de duas ou mais tabelas com base em uma condição de relacionamento entre elas. Por exemplo, um JOIN pode ser aplicado para recuperar informações de clientes e pedidos de vendas em que as tabelas 'Clientes' e 'Pedidos' estão relacionadas por um campo comum, como 'ID do Cliente'. Isso permite a criação de um conjunto de resultados consolidado que inclui dados das duas tabelas, facilitando a análise conjunta."
  },
  {
    "question": "O que é a primeira regra de normalização de dados (1ª Forma Normal) e qual é o seu objetivo ao projetar um banco de dados?",
    "answer": "A primeira regra de normalização, ou 1ª Forma Normal, exige que cada coluna de uma tabela contenha apenas valores atômicos, indivisíveis. O objetivo é evitar a repetição de dados e garantir a integridade dos dados ao projetar um banco de dados."
  },
  {
    "question": "Explique a segunda regra de normalização de dados (2ª Forma Normal) e em que cenário ela se aplica?",
    "answer": "A segunda regra de normalização, ou 2ª Forma Normal, estabelece que uma tabela deve estar na 1ª Forma Normal e que todos os atributos não chave devem ser totalmente dependentes da chave primária. Isso é especialmente aplicável quando há uma chave primária composta, e os atributos dependem apenas de parte dessa chave."
  },
  {
    "question": "O que é a terceira regra de normalização de dados (3ª Forma Normal) e por que é importante na modelagem de bancos de dados?",
    "answer": "A terceira regra de normalização, ou 3ª Forma Normal, afirma que uma tabela deve estar na 2ª Forma Normal e que não deve haver dependências transitivas. Isso significa que os atributos não chave devem depender apenas da chave primária. A 3ª Forma Normal é crucial para reduzir redundâncias e melhorar a consistência dos dados na modelagem de bancos de dados."
  },
  {
    "question": "O que são 'Collation' e 'Charset' em um banco de dados, e qual é a importância de especificar corretamente esses elementos durante a criação de tabelas?",
    "answer": "Em um banco de dados, 'Collation' refere-se às regras de ordenação e comparação de caracteres, enquanto 'Charset' (conjunto de caracteres) define o conjunto de caracteres utilizado para armazenar dados. É crucial especificar corretamente 'Collation' e 'Charset' durante a criação de tabelas para garantir que as operações de ordenação e comparação sejam realizadas de maneira consistente, e que os dados sejam armazenados e recuperados adequadamente, evitando problemas de codificação e ordenação inconsistentes."
  }
] # fecha o array 


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

