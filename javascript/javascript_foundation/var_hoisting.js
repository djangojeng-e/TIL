// var and hoisting

// declare function first

function hello() {
  console.log('hello!');
}

hello();

// calling the function first

hello2();

function hello2() {
  console.log('hello2!');
}

// Delcaration part goes to up only

console.log(name);

name = 'Mark';

console.log(name);

var name = 'Peter';
