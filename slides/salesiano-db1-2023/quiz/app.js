const store = new Vuex.Store({
  state: {
    currentQuestion: 0,
    score: 0,
    showScore: false,
  },
  mutations: {
    incrementScore(state) {
      state.score += 1;
    },
    nextQuestion(state) {
      state.currentQuestion += 1;
    },
    setShowScore(state, payload) {
      state.showScore = payload;
    },
    resetQuiz(state) {
      state.currentQuestion = 0;
      state.score = 0;
      state.showScore = false;
    },
  },
})

Vue.component('quiz-app', {
  template: `
    <div class="app">
      <div v-if="showScore" class="score-section">
        <h2>Sua pontuação</h2>
        <p>{{ ((score / questions.length) * 100).toFixed(2) }}%</p>

        <div v-if=" Math.round((score / questions.length) * 100) === 100 ">
        <div style="width:100%;height:0;padding-bottom:67%;position:relative;"><iframe src="https://giphy.com/embed/26ufq9mryvc5HI27m" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>
        </div>

        <div v-if=" Math.round((score / questions.length) * 100) < 100 && Math.round((score / questions.length) * 100) > 0">
        <div style="width:100%;height:0;padding-bottom:100%;position:relative;"><iframe src="https://giphy.com/embed/VLzEYLMhEAlUydp4uW" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>        
        </div>

        <div v-if=" Math.round((score / questions.length) * 100) === 0 ">
        <div style="width:100%;height:0;padding-bottom:100%;position:relative;"><iframe src="https://giphy.com/embed/jZnOF0UoupsvKT0gKl" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div>        
        </div>

        <p>Você pode repetir o simulado do teste quantas vezes quiser.</p> 
        <button @click="restartQuiz">Reiniciar Quiz</button>
      </div>
      <div v-else class="question-section">
        <h2>Pergunta &num;{{ currentQuestion + 1 }}</h2>
        <div class="question-text" v-html="questions[currentQuestion].questionText"></div>
        <div class="answer-buttons">
          <button
            v-for="(answerOption, index) in questions[currentQuestion].answerOptions"
            :key="index"
            @click="handleAnswerButtonClick(answerOption.isCorrect)"  
          >
            {{ String.fromCharCode(65 + index) }}) {{ answerOption?.answerText }}
          </button>
        </div>
      </div>
    </div>
  `, 
  computed: {
    currentQuestion() {
      return this.$store.state.currentQuestion;
    },
    score() {
      return this.$store.state.score;
    },
    showScore() {
      return this.$store.state.showScore;
    },
    questions() {
      // Define your questions and answer options here
const questions = [
  {
    questionText:
      "Qual cláusula SQL é usada para filtrar registros em uma consulta?",
    answerOptions: [
      { answerText: "SELECT", isCorrect: false },
      { answerText: "FROM", isCorrect: false },
      { answerText: "WHERE", isCorrect: true },
      { answerText: "ORDER BY", isCorrect: false },
    ],
  },
  {
    questionText:
      "Para ordenar os resultados de uma consulta SQL em ordem ascendente, qual cláusula você usaria?",
    answerOptions: [
      { answerText: "SELECT", isCorrect: false },
      { answerText: "FROM", isCorrect: false },
      { answerText: "ORDER BY", isCorrect: true },
      { answerText: "WHERE", isCorrect: false },
    ],
  },
  {
    questionText:
      "Qual cláusula SQL é usada para limitar o número de resultados retornados por uma consulta?",
    answerOptions: [
      { answerText: "SELECT", isCorrect: false },
      { answerText: "FROM", isCorrect: false },
      { answerText: "LIMIT", isCorrect: true },
      { answerText: "WHERE", isCorrect: false },
    ],
  },
  {
    questionText:
      "Para realizar uma pesquisa de padrão em uma coluna de texto em SQL, qual operador você usaria?",
    answerOptions: [
      { answerText: "=", isCorrect: false },
      { answerText: "<>", isCorrect: false },
      { answerText: "LIKE", isCorrect: true },
      { answerText: "IN", isCorrect: false },
    ],
  },
  {
    questionText:
      "Qual cláusula SQL é usada para especificar quais colunas devem ser incluídas no resultado de uma consulta?",
    answerOptions: [
      { answerText: "SELECT", isCorrect: true },
      { answerText: "FROM", isCorrect: false },
      { answerText: "WHERE", isCorrect: false },
      { answerText: "GROUP BY", isCorrect: false },
    ],
  },

  {
    questionText:
      "Qual é o principal objetivo da primeira forma normal (1NF) em bancos de dados?",
    answerOptions: [
      { answerText: "Eliminar a duplicação de dados", isCorrect: true },
      { answerText: "Garantir a integridade referencial", isCorrect: false },
      {
        answerText: "Dividir a tabela em várias tabelas menores",
        isCorrect: false,
      },
      {
        answerText: "Garantir que cada coluna tenha um valor único",
        isCorrect: false,
      },
    ],
  },
  {
    questionText:
      "Qual é a regra principal da segunda forma normal (2NF) em bancos de dados?",
    answerOptions: [
      {
        answerText: "Cada coluna deve conter apenas valores únicos",
        isCorrect: false,
      },
      {
        answerText: "Cada coluna deve ser do mesmo tipo de dados",
        isCorrect: false,
      },
      {
        answerText: "Toda coluna deve depender da chave primária completa",
        isCorrect: true,
      },
      {
        answerText: "A tabela deve ser dividida em duas tabelas menores",
        isCorrect: false,
      },
    ],
  },
  {
    questionText:
      "Qual dos seguintes é um bom exemplo de uma dependência transitiva em um banco de dados?",
    answerOptions: [
      {
        answerText:
          "A relação entre um cliente e seu número de telefone, onde o número de telefone depende diretamente do cliente.",
        isCorrect: false,
      },
      {
        answerText:
          "A relação entre um produto, seu preço e o código do fabricante, onde o preço depende do produto e o código do fabricante depende do preço.",
        isCorrect: true,
      },
      {
        answerText:
          "A relação entre um aluno, sua nota em um exame e a data do exame, onde a nota depende do aluno e a data do exame depende da nota.",
        isCorrect: false,
      },
      {
        answerText:
          "A relação entre um funcionário, seu endereço residencial e o número do departamento em que trabalha, onde o endereço depende do funcionário e o número do departamento depende do endereço residencial.",
        isCorrect: false,
      },
    ],
  },

  {
    questionText:
      "O que a terceira forma normal (3NF) em bancos de dados busca alcançar?",
    answerOptions: [
      { answerText: "Eliminar a duplicação de dados", isCorrect: false },
      {
        answerText: "Garantir que cada coluna tenha um valor único",
        isCorrect: false,
      },
      {
        answerText: "Reduzir o número de tabelas em um banco de dados",
        isCorrect: false,
      },
      { answerText: "Eliminar dependências transitivas", isCorrect: true },
    ],
  },
  {
    questionText:
      "Quais são os tipos de dados comuns que você pode usar em colunas de um banco de dados?",
    answerOptions: [
      {
        answerText: "Números (integer e float), texto (char e varchar)",
        isCorrect: true,
      },
      {
        answerText: "Cores (RGB) e nomes de animais",
        isCorrect: false,
      },
      {
        answerText: "Cores (RGB) e tamanhos (px)",
        isCorrect: false,
      },
      {
        answerText: "Datas (YYYY-MM-DD) e horas (HH:MM:SS)",
        isCorrect: false,
      },
    ],
  },

  {
    questionText:
      "O que é um Diagrama de Entidade-Relacionamento (DER) em bancos de dados?",
    answerOptions: [
      {
        answerText:
          "Um diagrama que mostra a relação entre frutas cítricas, como laranjas e bananas, em um banco de dados de receitas.",
        isCorrect: false,
      },
      {
        answerText:
          "Um diagrama que representa visualmente as entidades, atributos e relacionamentos em um banco de dados.",
        isCorrect: true,
      },
      {
        answerText:
          "Um diagrama que exibe a conexão de um banco de dados a um servidor web.",
        isCorrect: false,
      },
      {
        answerText:
          "Um diagrama que ilustra a lógica de programação de um aplicativo de banco de dados.",
        isCorrect: false,
      },
    ],
  },

  {
    questionText:
      "O que caracteriza uma relação um-para-um em um modelo de banco de dados?",
    answerOptions: [
      {
        answerText:
          "Cada registro na tabela A pode estar associado a apenas um registro na tabela B, e vice-versa.",
        isCorrect: true,
      },
      {
        answerText:
          "Cada registro na tabela A pode estar associado a vários registros na tabela B, mas não o contrário.",
        isCorrect: false,
      },
      {
        answerText:
          "Cada registro na tabela A pode estar associado a vários registros na tabela B, e vice-versa.",
        isCorrect: false,
      },
      {
        answerText:
          "Não há relação entre as tabelas A e B em uma relação um-para-um.",
        isCorrect: false,
      },
    ],
  },

  {
    questionText:
      "O que caracteriza uma relação um-para-muitos em um modelo de banco de dados?",
    answerOptions: [
      {
        answerText:
          "Cada registro na tabela A pode estar associado a vários registros na tabela B, mas cada registro na tabela B está associado a apenas um registro na tabela A.",
        isCorrect: true,
      },
      {
        answerText:
          "Cada registro na tabela A pode estar associado a apenas um registro na tabela B, e vice-versa.",
        isCorrect: false,
      },
      {
        answerText:
          "Cada registro na tabela A pode estar associado a vários registros na tabela B, e cada registro na tabela B pode estar associado a vários registros na tabela A.",
        isCorrect: false,
      },
      {
        answerText:
          "Não há relação entre as tabelas A e B em uma relação um-para-muitos.",
        isCorrect: false,
      },
    ],
  },

  {
    questionText:
      "O que caracteriza uma relação muitos-para-muitos em um modelo de banco de dados?",
    answerOptions: [
      {
        answerText:
          "Cada registro na tabela A pode estar associado a vários registros na tabela B, e vice-versa.",
        isCorrect: true,
      },
      {
        answerText:
          "Cada registro na tabela A pode estar associado a apenas um registro na tabela B, e vice-versa.",
        isCorrect: false,
      },
      {
        answerText:
          "Cada registro na tabela A pode estar associado a vários registros na tabela B, mas cada registro na tabela B está associado a apenas um registro na tabela A.",
        isCorrect: false,
      },
      {
        answerText:
          "Não há relação entre as tabelas A e B em uma relação muitos-para-muitos.",
        isCorrect: false,
      },
    ],
  },

  {
    questionText: `
onsidere a seguinte tabela de dados chamada 'Pessoas':
<table>
  <tr>
    <th>ID</th>
    <th>Nome</th>
    <th>Idade</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Maria</td>
    <td>30</td>
  </tr>
  <tr>
    <td>2</td>
    <td>João</td>
    <td>25</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Ana</td>
    <td>35</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Carlos</td>
    <td>28</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Beatriz</td>
    <td>22</td>
  </tr>
</table>
<br>
Agora, observe a seguinte consulta SQL:<br>
<pre>
SELECT Nome
FROM Pessoas
WHERE Idade < 30;
</pre>
<br>
Qual será o resultado desta consulta?
`,
    answerOptions: [
      {
        answerText: "Maria, João, Ana",
        isCorrect: false,
      },
      {
        answerText: "Carlos, Beatriz",
        isCorrect: false,
      },
      {
        answerText: "João, Carlos, Beatriz",
        isCorrect: true,
      },
      {
        answerText: "Maria, Ana",
        isCorrect: false,
      },
    ],
  },

  {
    questionText: `
Considere duas tabelas em um banco de dados:

Tabela "Pedidos":
<table>
  <tr>
    <th>ID</th>
    <th>Produto</th>
    <th>Quantidade</th>
    <th>ID do Cliente</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Camiseta</td>
    <td>2</td>
    <td>101</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Tênis</td>
    <td>1</td>
    <td>102</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Jeans</td>
    <td>3</td>
    <td>103</td>
  </tr>
</table>

Tabela "Clientes":
<table>
  <tr>
    <th>ID</th>
    <th>Nome</th>
    <th>Email</th>
  </tr>
  <tr>
    <td>101</td>
    <td>Maria</td>
    <td>maria@email.com</td>
  </tr>
  <tr>
    <td>102</td>
    <td>João</td>
    <td>joao@email.com</td>
  </tr>
  <tr>
    <td>103</td>
    <td>Ana</td>
    <td>ana@email.com</td>
  </tr>
</table>
<br>
Agora, observe a seguinte consulta SQL que utiliza um JOIN entre as tabelas "Pedidos" e "Clientes":
<pre>
SELECT Pedidos.ID, Clientes.Nome
FROM Pedidos
INNER JOIN Clientes ON Pedidos.ID do Cliente = Clientes.ID;
</pre> 
<br>
Quais resultados serão retornados como resultado dessa consulta?
`,
    answerOptions: [
      {
        answerText: "1 - Maria, 2 - João, 3 - Ana",
        isCorrect: true,
      },
      {
        answerText: "101 - Maria, 102 - João, 103 - Ana",
        isCorrect: false,
      },
      {
        answerText: "Camiseta - Maria, Tênis - João, Jeans - Ana",
        isCorrect: false,
      },
      {
        answerText: "Camiseta, Tênis, Jeans",
        isCorrect: false,
      },
    ],
  },
];

          questions.forEach((question) => {
            question.answerOptions = this.shuffleArray(question.answerOptions)
          })

          return questions;
        },
    },
    methods: {
      handleAnswerButtonClick(isCorrect) {
        if (isCorrect) {
          this.$store.commit('incrementScore');
        }
        this.$store.commit('nextQuestion');
        if (this.currentQuestion === this.questions.length) {
          this.$store.commit('setShowScore', true);
        }
      },
      restartQuiz() {
        this.$store.commit('resetQuiz');
      },
      shuffleArray(array) {
        // Shuffling algorithm (Fisher-Yates Shuffle)
        for (let i = array.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [array[i], array[j]] = [array[j], array[i]]; // Swap elements
        }
        return array;
      },
    },
  })

new Vue({
  el: '#app',
  store,
})
