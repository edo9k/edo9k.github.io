from os import system

def clear():
    system('clear') 

# perguntas e as respostas
questions = [
    {
      "question": "O que é uma variável em JavaScript?",
      "answer": "Uma variável em JavaScript é um nome simbólico usado para armazenar dados, como números, strings ou objetos."
    },
    {
      "question": "Qual é a diferença entre 'let', 'const' e 'var' ao declarar variáveis em JavaScript?",
      "answer": "'let' e 'const' são usados ​​para declarar variáveis ​​com escopo de bloco, enquanto 'var' possui escopo de função."
    },
    {
      "question": "O que é um loop 'while' em JavaScript e como ele funciona?",
      "answer": "Um loop 'while' em JavaScript executa um bloco de código repetidamente enquanto uma condição especificada for verdadeira."
    },
    {
      "question": "Como você define uma função em JavaScript?",
      "answer": "Uma função em JavaScript é definida usando a palavra-chave 'function' seguida pelo nome da função e parâmetros, se houver."
    },
    {
      "question": "Qual é a saída do seguinte código JavaScript: 'console.log(5 + \"5\")'?",
      "answer": "A saída será a string '55' porque ocorre uma concatenação de strings."
    },
    {
      "question": "O que é um array em JavaScript e como você declara um?",
      "answer": "Um array em JavaScript é uma estrutura de dados que armazena uma coleção de valores. Você pode declará-lo usando colchetes, por exemplo, 'let meuArray = [1, 2, 3]'."
    },
    {
      "question": "Explique o que é o 'this' em JavaScript e como ele é usado.",
      "answer": "O 'this' em JavaScript se refere ao objeto atual e é usado para acessar propriedades e métodos desse objeto."
    },
    {
      "question": "Como você escreve um comentário de uma única linha em JavaScript?",
      "answer": "Um comentário de uma única linha em JavaScript é precedido por '//' como em '// Este é um comentário de uma linha'."
    },
    {
      "question": "O que é uma condicional 'if-else' e como ela é usada?",
      "answer": "Uma condicional 'if-else' é usada para tomar decisões em JavaScript. Ela executa um bloco de código se uma condição for verdadeira e outro bloco se a condição for falsa."
    },
    {
      "question": "Qual é a função do método 'console.log()' em JavaScript?",
      "answer": "O método 'console.log()' é usado para imprimir mensagens ou valores no console do navegador ou no ambiente de desenvolvimento."
    },
    {
      "question": "O que representa o operador lógico 'NÃO' (NOT) na lógica proposicional?",
      "answer": "O operador lógico 'NÃO' (NOT) inverte o valor de uma proposição. Se a proposição for verdadeira, 'NÃO' a torna falsa e vice-versa."
    },
    {
      "question": "Em lógica proposicional, o que é uma implicação (condicional) representada por 'Se... então...'?",
      "answer": "Uma implicação (condicional) é verdadeira, a menos que a primeira proposição seja verdadeira e a segunda seja falsa."
    },
    {
      "question": "Qual é a tabela verdade do operador lógico 'E' (AND)?",
      "answer": "A tabela verdade do operador lógico 'E' (AND) só é verdadeira quando ambas as proposições são verdadeiras, caso contrário, é falsa."
    },
    {
      "question": "O que é uma contrapositiva em lógica proposicional?",
      "answer": "A contrapositiva de uma implicação inverte e nega as proposições originais, mantendo a mesma validade lógica."
    },
    {
      "question": "Explique o conceito de 'Bicondicional' (SE e SOMENTE SE) na lógica proposicional.",
      "answer": "O 'Bicondicional' (SE e SOMENTE SE) é verdadeiro quando ambas as proposições são iguais, ou seja, ambas verdadeiras ou ambas falsas."
    },
    {
      "question": "Qual é a tabela verdade do operador lógico 'OU' (OR)?",
      "answer": "A tabela verdade do operador lógico 'OU' (OR) é verdadeira quando pelo menos uma das proposições é verdadeira."
    },
    {
      "question": "O que é uma tautologia em lógica proposicional?",
      "answer": "Uma tautologia é uma proposição que é sempre verdadeira, independentemente dos valores das proposições individuais."
    },
    {
      "question": "Como se representa uma proposição composta em lógica proposicional?",
      "answer": "Uma proposição composta é representada pela combinação de proposições individuais usando operadores lógicos."
    },
    {
      "question": "O que é a regra de simplificação em lógica proposicional?",
      "answer": "A regra de simplificação permite simplificar proposições complexas removendo cláusulas redundantes."
    },
    {
      "question": "Como se representa uma negação em lógica proposicional?",
      "answer": "A negação de uma proposição é representada pelo operador 'NÃO' (NOT)."
    }
  ]


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

