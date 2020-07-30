// revision 복습 세션!

// forEach 와 =>

const superheroes = ['아이언맨', '캡틴 아메리카', '토르', '닥터 스트레인지']

superheroes.forEach(hero => {
  console.log(hero);
});

// map 이라는 내장함수
// 원소를 다른 형태로 변환할때 사용
// square 라는 함수를 만들어서, 넣어줌

const array = [1, 2, 3, 4, 5, 6, 7, 8]

const square = n => n * n;
const squared = array.map(square);
console.log(squared);

// indexof

const index = superheroes.indexOf('토르')
console.log(index);

// findIndex
// 조건을 만족하는 원소가 어디에 있는지 알아냄

const todos = [{
  id: 1,
  text: '자바스크립트 입문',
  done: true
},
{
  id: 2,
  text: '함수 배우기',
  done: true
},
{
  id: 3,
  text: '객체와 배열 배우기',
  done: true
},
{
  id: 4,
  text: '배열 내장함수 배우기',
  done: false
}
];

const findindex = todos.findIndex(todo => todo.id === 3);
console.log(findindex);

// const find = todos.find(todo=>todo.id===3) 일 경우, 객체 자체를 리턴
// todos.filter() 를 사용하여, 조건에 맞는 원소들을 가진 새로운 배열을 만들수 있다.

// splice
// 특정 인덱스에서 몇개를 지우는 것

const numbers =[10, 20, 30, 40];
const sliced = numbers.slice(0, 2); // 0 부터 시작해서 2 전까지

console.log(sliced);
console.log(numbers);

// splice 는 기존 배열에 변화를 줌
// slice 는 기존 배열에 변화를 주지 않음

// numbers.shift() 맨 왼쪽에 거를 바깥으로 꺼내고, 기존의 배열을 건드림
// numbers.pop() 맨 오른쪽 원소를 바깥으로 꺼내고, 기존의 배열을 건드림

// concat
// 배열을 합쳐서 새로운 배열을 만들어줌
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const concated = arr1.concat(arr2);

console.log(concated);

// join
// 특정 세퍼레이터를 사용해서, 배열 문자열로 만들어줌

const list = [1, 2, 3, 4, 5];
console.log(list.join());  // 1, 2, 3, 4, 5
console.log(list.join(' ')); // 1 2 3 4 5
console.log(list.join(', ')); // 1, 2, 3, 4, 5


// reduce
// reduce 를 사용하여, 누적되는값을 계산
// 매우 유용한 메서드

const reduce_list = [1, 2, 3, 4, 5];
let sum = array.reduce((accumulator, current) => accumulator + current, 0);

console.log(sum);


// 연습문제

function countBiggerThanTen(numbers) {
  // 구현
  let counts = 0
  for (let i = 0; i < numbers.length; i++) {

    if (numbers[i] > 10) {
        counts++;
    };
  };
  return counts
}

const count = countBiggerThanTen([1,2,3,5,10,20,30,40,50,60]);
console.log(count); // 5
