// 자바스크립트 반복문 연습

function sumOf(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i]
  }

  return sum;
}

const result = sumOf([1, 2, 3, 4, 5]);
console.log(result);

// 숫자로 이루어진 배열이 주어졌을때, 해당 숫자 배열안에 들어가 있는 숫자 중 3 보다
// 큰 숫자로만 이루어진 배열을 새로 만들어서 반환해 보세요

function quiz(array) {
  const new_numbers = []

  for (let i = 0; i < numbers.length; i++) {
    if (array[i] > 3) {
      new_numbers.push(array[i])
    }
  }
  return new_numbers 
}

const numbers = [1, 2, 3, 4, 5, 6, 7];
console.log(quiz(numbers));
