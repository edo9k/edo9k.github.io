function maiorDe18(idade) {
  if (idade === undefined) return false
  if (idade >= 18) return true 
  else return false
} 

function testes() {
  console.log("a função vazia deveria retornar falso", 
    maiorDe18() === false ? "✅" : "❌")

  console.log("a função deveria retornar falso para idade 17",
    maiorDe18(17) === false ? "✅" : "❌")

  console.log("deveria retornar verdadeiro para idade 18",
    maiorDe18(18) === true ? "✅" : "❌")

  console.log("deveria retornar verdadeiro para idade 19",
    maiorDe18(19) === true ? "✅" : "❌")

}

/* roda os testes */
testes() 



