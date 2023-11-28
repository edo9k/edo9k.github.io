
function f(l) {
  let mn = l[0]
  let mx = l[0]

  for (let i = 0; i < l.length; i++) {
    if (l[i] < mn) 
      mn = l[i]

    if (l[i] > mx)
      mx = l[i]
  }

  return { mn, mx } 
}

const lista = [1958, 1962, 1970, 1994, 2002] 

console.log(f(lista)) 
