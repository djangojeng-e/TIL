// shift, pop, unshift

// shift 는 배열의 첫번째 원소를 추출해준다
// const numbers =[10, 20, 30, 40]
//
// const value = numbers.shift();
// console.log(value);
// console.log(numbers);

// 추출하고 나서 첫번째 요소는 배열에서 빠져 있는채로 배열이 남아있다

// pop 은 배열의 마지막 원소를 추출, pop 을 통해서 마지막 원소를 뺀 배열을 남긴다.
// 모든 배열을 빼면, 비어있는 배열이 남는다.
//
// const numbers = [10, 20, 30, 40]
//
// const value = numbers.pop();
// console.log(value);
// console.log(numbers);
// numbers.pop()
// numbers.pop()
// console.log(numbers);
// numbers.pop()
// console.log(numbers)


// unshift 는 새로운 요소를 배열의 맨 앞부분에 추가해준다
// const numbers = [10, 20, 30, 40]
// numbers.unshift(5);
// console.log(numbers);
//
//
// const numbers = [10, 20, 30, 40];
// numbers.unshift(0);
// const value = numbers.shift();
// console.log(numbers);


// concat 은 여러개의 배열을 합쳐주는 역할을 해줌
// concat 은 기존의 배열을 건들지 않는다.

const arr1 = [1, 2, 3]
const arr2 = [4, 5, 6]
const concated = arr1.concat(arr2);
console.log(concated);

// join 이라는 내장함수로, 배열안에 원소들을 합쳐서 문자열로 만들어준다
const array = [1, 2, 3, 4, 5]
console.log(array.join());
console.log(array.join(' '));
console.log(array.join(', '));
