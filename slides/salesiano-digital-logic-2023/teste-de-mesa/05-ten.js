
function f(l) {
  return l
    .filter(n => n % 2 == 0) // -> manter só os pares 
    .map(n => n * 10) // -> multiplica por 10 
    .reduce((a,b) => a + b, 0) // -> somar os valores 
}

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

console.log(f(numbers))

