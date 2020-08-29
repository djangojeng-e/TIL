// Hoisting
// 아직 선언되지 않은 변수와 함수를 끌어다가 쓰는 작동 방식

// example of hoisting
//
// myFunction();
//
//
//
// function myFunction() {
//   console.log('hello world');
// }
//
//
// myFunction();

// 웬만하면 hoisting 은 피해야 한다.
// to avoid ambiguity
//
// console.log(number);
//
// var number = 2;


// function fn() {
//   console.log(a);
//   let a = 2;
// }
//
// fn();

// const, let doesn't trigger hoisting
// var does hoisting compatible

function myFunction() {
  console.log('hello world');
}

myFunction();
