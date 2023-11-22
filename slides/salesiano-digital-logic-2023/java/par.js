
const numeros = [0, 1, 2, 3, 4, 5]

for (numero in numeros) {
  consol.log(Par(numero))
}

function ePar(numero) {
  if (numero % 2 == 0) {
    return numero + " é par."
  } else {
    return numero + " não é par."
  }
}
