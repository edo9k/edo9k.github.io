/* TESTES DE MESA ARRGHH! */ 

function f(a, b, c) {
  return a + b + c
}

function g(a, b, c) {
  return a * b * c
}

function h(a, b, c) {
  return f(a, b, c) / g(a, b, c) 
}

console.log("f 10 20 30 = ", f(10, 20, 30)) // 60 
console.log("g 10 20 30 = ", g(10, 20, 30)) // 6000
console.log("h 10 20 30 = ", h(10, 20, 30)) // 0.01


