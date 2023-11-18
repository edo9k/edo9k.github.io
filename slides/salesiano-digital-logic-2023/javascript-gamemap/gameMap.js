
const sala = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,1], 
  [1,0,0,0,0,0,0,0,0,0,0,0,0,1], 
  [2,0,0,0,0,0,0,0,0,0,0,0,0,2], 
  [1,0,0,0,0,0,0,0,0,0,0,0,0,1], 
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

const salaGerada = s => s.map(
    linha => linha.map(
      tile => {
        if (tile == 3) return '🐈' 
        if (tile == 2) return '🚪' 
        if (tile == 1) return '🧱'
        if (tile == 0) return '⬜'
      }).join('') 
).join('\n') 

const jogador = { x:0, y:3 } 

const intervalID = setInterval(() => {
  if (sala[jogador.y][jogador.x] == undefined) { 
    clearInterval(intervalID) 
  }

  const valorAnterior = sala[jogador.y][jogador.x] 
  sala[jogador.y][jogador.x] = 3 /*'emoji de gato*/
  console.log(salaGerada(sala))
  console.log('\n')

//  console.table(sala) 
//  console.log(jogador) 
//  console.log('\n')

  sala[jogador.y][jogador.x] = valorAnterior
  jogador.x++  
}, 1000)  
