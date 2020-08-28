// scope theory
// scope 는 변수나 함수가 어디까지 유효한지 영역

// Global
// Function
// Block


const value = 'hello!';

//
// function myFunction() {
//   console.log('myFunction: ');
//   console.log(value);
// }
//
// function otherFunction() {
//   console.log('otherFunction: ');
//   const value = 'bye!';
//   console.log(value);
// }
//
// myFunction();
// otherFunction();
//
// console.log('global scope:');
// console.log(value);
//
// function myFunction() {
//   const value = 'bye!';
//   const anotherValue = 'world';
//   function functionInside() {
//     console.log('functionInside: ')
//     console.log(value);
//     console.log(anotherValue);
//   }
//   functionInside();
// }
//
//
// myFunction();
// console.log('global scope');
// console.log(value);
// console.log(anotherValue);

function myFunction() {
  const value = 'bye!';
  if (true) {
    const value = 'world';
    console.log('block scope:' );
    console.log(value);
  }
  console.log('function scope: ');
  console.log(value);
}

myFunction();
console.log('global scope:');
console.log(value);
