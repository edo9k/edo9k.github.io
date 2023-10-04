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
          questionText: `<p>What does SQL stand for?</p> <img src="https://devtools.com.br/blog/wp-content/uploads/2013/06/MySQL-Logo.wine_-2048x1365.png">`,
          answerOptions: [
            { answerText: "Standard Query Language", isCorrect: false },
            { answerText: "Structured Query Language", isCorrect: true },
            { answerText: "System Query Language", isCorrect: false },
            { answerText: "Server Query Language", isCorrect: false },
          ],
        },
        {
          questionText: "Which SQL statement is used to retrieve data from a database?",
          answerOptions: [
            { answerText: "GET", isCorrect: false },
            { answerText: "SELECT", isCorrect: true },
            { answerText: "FETCH", isCorrect: false },
            { answerText: "QUERY", isCorrect: false },
          ],
        },
        {
          questionText: "In SQL, which clause is used to filter the result set based on a specified condition?",
          answerOptions: [
            { answerText: "FROM", isCorrect: false },
            { answerText: "WHERE", isCorrect: true },
            { answerText: "HAVING", isCorrect: false },
            { answerText: "GROUP BY", isCorrect: false },
          ],
        },
      ]

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
