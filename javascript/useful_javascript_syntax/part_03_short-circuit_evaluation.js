// true && true // true
// true && true // false
// true || false // true
// false || true // true

// logical operator does not require to be true or false only.
// there are truthy and falsy values

const dog = {
  name: "멍멍이"
};

function getName(animal) {
  return animal && animal.name;
  }

const name = getName();
console.log(name);

console.log(true && 'hello');
console.log(false && 'hello');
console.log('hello' && 'bye');
console.log(null && 'hello');
console.log(undefined && 'hello');
console.log('' && 'hello');
console.log(0 && 'hello');
console.log(1 && 'hello');


// if the first value is true, the later part of logic will be the result
// if the later value is false, returns the first value

console.log(false || 'hello');
console.log('' || 'no value');
console.log(null || 'it is null');
console.log(undefined || 'not defnied');
console.log(0 || '0');
console.log(NaN || 'NaN');

console.log(1 || 'what?');
console.log(true || 'Not looked up this part');
console.log('oh' || 'not looking up here');
console.log([] || 'Result doesn not contain here');
