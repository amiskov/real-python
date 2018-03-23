function makeBold (fn) {
  return function () {
    return '<b>' + fn.apply(null, arguments) + '</b>'
  }
}

function addBang (fn) {
  return function () {
    return fn.apply(null, arguments) + '!'
  }
}

function greet (name) {
  return `Hello, my name is ${name}`
}

const boldGreet = makeBold(greet)
const bangGreet = addBang(greet)
const boldBangGreet = addBang(makeBold(greet))

console.log('greet:', greet('Max'))
console.log('boldGreet:', boldGreet('Max'))
console.log('bangGreet:', bangGreet('Max'))
console.log('boldBangGreet:', boldBangGreet('Max'))

