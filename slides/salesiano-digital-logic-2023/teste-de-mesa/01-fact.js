
/*
 * Prova: OBJETIVA - 2019
 * FHSTE - RS - Analista de Tecnologia da
 * (modificada) 
 */ 

function f(n) {

  let res = 1
  for (let i = n; i >= 1; i--) { 
    res *= n
    n--
  }

  return res
}

console.log(f(3)) 
