// 배열 내장함수 reduce
// 잘 사용할수 있으면 정말 유용한 함수
// 배열안에 값이 주어졌을때, 배열안 값을 사용하여 연산할때 유용

const numbers = [1, 2, 3, 4, 5];

// 배열의 모든 원소를 사용하여, 배열안의 모든값의 합을 구하려면

// let sum = 0;
//
// numbers.forEach(n => {
//   sum += n
// });
//
// console.log(sum);

const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
console.log(sum);


// 0 은 초기값
// accumulator 는 누적된 값

const average = numbers.reduce((accumulator, current, index, array) => {
  if (index === array.length - 1) {
    return (accumulator + current) / array.length;
  }
  return accumulator + current;
}, 0);

console.log(average);
