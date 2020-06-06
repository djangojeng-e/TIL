// javascript 배열
// 배열은, 여러개의 항목들이 들어있는 리스트와 같음
// 배열안에 모든 원소들이 똑같을 필요는 없음
// 자바스크립트 안의 배열에 대해 배워보도록 합니다.

const array = [1, 2, 3, 4, 5]
console.log(array)

// 배열안에, 객체도 넣을수 있음
// 배열안에 요소를 조회하고 싶으면, 조회할수 있다.
// 배열안의 인덱스는 0부터 시작함. 파이썬과 비슷함

console.log(array[3])

const objects = [
  {name: '멍멍이'},
  {name: '야옹이'}
];

console.log(objects);
console.log(objects[0]);
console.log(objects[1]);

//  배열에서 첫번째 항목은 0 부터 시작한다.
// 배열에 새로운 항목을 추가할때는 , push 라는 함수를 사용한다

objects.push(
  {name: '멍뭉이'}
);

console.log(objects)

//  배열의 크기를 알아보는 메서드가 존재한다. length 메서드를 사용하여
// 배열의 길이를 알아볼수 있다. 출력할수도 있다.
// 파이썬에서는, len 함수와 매치 될것이다.

console.log(objects.length);
