const numbers = [10, 20, 30, 40];

// splice 는 특정 원소를 제거할때 사용한다

// const index = numbers.indexOf(30);
// console.log(index);
//
// const spliced = numbers.splice(index, 1);
//
// console.log(spliced);
// console.log(numbers);

// slice 는 배열을 잘라낼떄 사용한다. 기존에 배열 원소를 건들지 않는다

const sliced = numbers.slice(0, 2);
console.log(sliced);
console.log(numbers);

// slice 는 기존의 배열을 건들지 않고, Splice 는 기존의 배열을 바꿔줍니다.
