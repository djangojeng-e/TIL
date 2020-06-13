// 배열 내장함수 map
// 배열 안의 변수를 바꾸기 위해 존재

const array = [1, 2, 3, 4, 5, 6, 7, 8];

// 배열 안의 모든 숫자를 제곱해서 숫자를 나열하고 싶다면,
// map 함수를 사용할수 있다.

// const squared = [];
// for (let i = 0; i < array.length; i++) {
//   squared.push(array[i] * array[i])
// }
//
// console.log(squared);
//
//
// const squared = [];
// array.forEach(n => {
//   squared.push(n * n);
// });
//
// console.log(squared);

// map 을 사용하면 얼마나 깔끔해질지 확인해 본다.

// const square = n => n * n;
// const squared = array.map(square)
//
// console.log(squared);
//
// const squared = array.map(n => n * n);
//
// console.log(squared);

const items = [
  {
    id: 1,
    text: 'hello'
  },
  {
    id:2,
    text: 'bye'
  }
];

const texts = items.map(item => item.text);
console.log(texts);


// indexof
// 특정 항목이 배열에서 몇번째 항목인지 알고 싶으면, indexOf 내장함수를 사용하면 된다.

const superheroes = ['아이언맨', '캡틴아메리카', '토르', '닥터스트레인지'];
const index = superheroes.indexOf('토르');
console.log(index);

// findindex

const todos = [
  {
    id: 1,
    text: '자바스크립트 입문',
    done: true,
  },
  {
    id: 2,
    text: '함수 배우기',
    done: true,
  },
  {
    id: 3,
    text: '객체와 배열 배우기',
    done: true,
  },
  {
    id: 4,
    text: '배열 내장함수 배우기',
    done: false,
  }
]

// findindex 의 파라미터는 함수가 된다
// 특수한 조건에 대해서 몇번째인지 알고싶으면, findIndex 를 사용한다

// const index = todos.findIndex(todo => todo.id === 3);


// find
// findIndex 와 비슷하게 특정 조건에 대해서 찾는다.
// 조건에 부합하는 가장 첫번째 값을 찾아냄.

const todo = todos.find(todo => todo.id === 3)
console.log(todo)
