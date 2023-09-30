from os import system

def clear():
    system('clear') 

# Uma lista de dicionários que armazena as perguntas e as respostas
questions = [
  {
    "question": "Qual é um exemplo de um banco de dados relacional amplamente utilizado na indústria hoje em dia?",
    "answer": "Um exemplo de um banco de dados relacional amplamente utilizado na indústria hoje em dia é o MySQL. Outros exemplos são o MsSQL (Microsoft SQL Server), o PostgreSQL, o MariaDB, o DB2 e o Oracle DB."
  },
  {
    "question": "O que é normalização de dados em um banco de dados e por que é importante?",
    "answer": "A normalização de dados em um banco de dados é o processo de organizar os dados de forma a reduzir a redundância e melhorar a integridade dos dados. Isso é feito dividindo as tabelas em estruturas menores e relacionadas, garantindo que cada atributo contenha apenas valores atômicos. É importante para melhorar a eficiência do banco de dados, minimizar anomalias de atualização e facilitar operações de consulta."
  },
  {
    "question": "O que é o operador SQL SELECT e como ele é usado em consultas de banco de dados?",
    "answer": "O operador SQL SELECT é usado para recuperar dados de uma ou mais tabelas em um banco de dados. Ele permite que você especifique as colunas desejadas, as tabelas envolvidas e as condições para filtrar os resultados."
  },
  {
    "question": "O que é o operador SQL ORDER BY e como ele afeta o resultado de uma consulta?",
    "answer": "O operador SQL ORDER BY é usado para classificar os resultados de uma consulta em ordem ascendente ou descendente com base em uma ou mais colunas especificadas. Ele afeta a ordem em que os registros são apresentados no resultado da consulta."
  },
  {
    "question": "Qual é a finalidade do operador SQL LIMIT e como ele é aplicado em consultas SQL?",
    "answer": "O operador SQL LIMIT é usado para limitar o número de registros retornados por uma consulta. Ele é aplicado após a cláusula SELECT e permite que você especifique o número máximo de linhas que deseja recuperar."
  },
  {
    "question": "O que é o operador SQL WHERE e forneça um exemplo de seu uso em uma consulta.",
    "answer": "O operador SQL WHERE é usado para filtrar os registros em uma consulta com base em uma condição especificada. Por exemplo, a consulta 'SELECT * FROM clientes WHERE idade > 30' retorna todos os clientes com idade superior a 30 anos."
  },
  {
    "question": "O que é uma junção (join) em SQL e como ela é usada para combinar dados de múltiplas tabelas?",
    "answer": "Uma junção (join) em SQL é usada para combinar dados de múltiplas tabelas com base em colunas relacionadas. Ela permite que você recupere informações de várias tabelas em uma única consulta, combinando registros que atendem aos critérios de junção."
  },
  {
    "question": "O que é um Diagrama Entidade-Relacionamento (DER) em um projeto de banco de dados e como ele ajuda na modelagem de dados?",
    "answer": "Um Diagrama Entidade-Relacionamento (DER) em um projeto de banco de dados é uma representação visual que descreve as entidades (tabelas), os relacionamentos entre essas entidades e os atributos (colunas) associados a cada entidade. Ele ajuda na modelagem de dados fornecendo uma visão clara da estrutura e das relações dos dados em um sistema."
  },
  {
    "question": "Explique qual é a função dos índices em um banco de dados relacional e como eles podem melhorar o desempenho das consultas.",
    "answer": "Os índices em um banco de dados relacional são usados para melhorar o desempenho das consultas. Eles funcionam como estruturas de dados auxiliares que permitem que o sistema de gerenciamento de banco de dados (DBMS) localize os registros mais rapidamente, reduzindo a necessidade de percorrer toda a tabela. Isso resulta em consultas mais eficientes e tempos de resposta mais curtos para operações de busca e junção."
  },
    {
    "question": "O que é a cardinalidade em um relacionamento entre tabelas em um banco de dados e como ela é representada?",
    "answer": "A cardinalidade em um relacionamento entre tabelas em um banco de dados refere-se ao número de ocorrências de uma entidade que podem estar associadas a outra entidade por meio desse relacionamento. Ela é representada por meio de termos como 'um para um' (1:1), 'um para muitos' (1:N) e 'muitos para muitos' (N:N) para descrever quantos registros em uma tabela estão relacionados com registros em outra tabela."
  },
    {
    "question": "Como você implementaria um relacionamento 'muitos para muitos' (N:N) em um design de banco de dados usando uma tabela intermediária?",
    "answer": "Você implementaria um relacionamento 'muitos para muitos' (N:N) criando três tabelas: as duas tabelas principais envolvidas no relacionamento e uma terceira tabela intermediária que armazena pares de chaves estrangeiras referenciando os registros nas tabelas principais. Essa tabela intermediária permite que muitos registros de uma tabela estejam relacionados a muitos registros da outra tabela."
  },
  {
    "question": "Dê um exemplo prático de um cenário em que um relacionamento 'muitos para muitos' (N:N) seja necessário e explique como ele seria modelado em um banco de dados.",
    "answer": "Um exemplo prático seria um sistema de gerenciamento de alunos e cursos em uma universidade. Vários alunos podem se inscrever em vários cursos, e vários cursos podem ter vários alunos matriculados. Esse relacionamento 'muitos para muitos' seria modelado com três tabelas: uma para alunos, uma para cursos e uma terceira tabela intermediária que registra as inscrições dos alunos em cursos específicos."
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

