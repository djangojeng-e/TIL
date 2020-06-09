// for of 의 반복문
// 주로 배열을 다룰때 사용된다.

const numbers = [10, 20, 30, 40, 50];

for (let number of numbers) {
  console.log(number)
}

// python 에서 for number in numbers 와 비슷한듯하다.

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}

// for of 가 잘 익숙해 지지 않는다면, 사용하지 않아도 상관 없다.
// 왜냐하면, 배열의 내장함수를 사용하면 더 쉽기 때문

// for in 반복문은 주로 객체에 대한 것을 반복할때 사용한다.

const doggy = {
  name: '멍멍이',
  sound: '멍멍',
  age: 2
};
//
// console.log(Object.entries(doggy));
// console.log(Object.keys(doggy));
// console.log(Object.values(doggy));

// 파이썬에서 사용하는 사전의 keys() 와 values() 와 같다

// for in 은 이런 작업과 동일한것을 해준다

for (let key in doggy) {
  console.log(`${key}: ${doggy[key]}`);
}

// `${}` 는 template literal 이다. 복습이 필요한 중요한 개념이니 복습해야 한다!  
