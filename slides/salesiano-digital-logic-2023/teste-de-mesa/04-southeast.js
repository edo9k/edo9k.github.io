
function f(l) {
  const res = l
    .map(item => item.length)

  return res
}

function g(l) {
  return l
    .filter(item => item.length > 10) 
}

const states = [
  'Espírito Santo',
  'Minas Gerais',
  'Rio de Janeiro',
  'São Paulo',
];

console.log("#1 ", states)
console.log("#2 ", f(states)) 
console.log("#3 ", g(states))

