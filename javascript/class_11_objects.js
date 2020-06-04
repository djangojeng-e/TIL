// objects 객체
// 자바스크립트는 객체 지향인가?

// 객체는, 어떠한 값을 선언하게 될때
// 하나의 값을, 여러개의 객체에 담게 해줌
//
// const dogName = '멍멍이';
// const dogAge = 2;
//
// console.log(dogName);
// console.log(dogAge);

// 객체를 사용한다면, 아래와 비슷한 구조로 사용한다.
//
// const dog = {
//   name: '멍멍이',
//   age: 2,
//   cute: true,
//   sample: {
//     a: 1,
//     b: 2,
//   }
// }

const dog = {
  name: '멍멍이',
  age: 2
}

console.log(dog)
console.log(dog.name);
console.log(dog.age);

//  자바스크립트에서, 객체는 파이썬 딕셔너리와 비슷해 보임.
// Key 값들을 문자열 형태로 사용하려면, '' 안에 넣어야 한다.

const ironMan = {
  name: '토니 스타크',
  actor: '로버트 다우니 주니어',
  alias: '아이언맨',
};

const captainAmerica = {
  name: '스티븐 로저스',
  actor: '크리스 에반스',
  alias: '캡틴 아메리카'
};

console.log(ironMan)
console.log(captainAmerica)

function print(hero) {
  const text = `${hero.alias}(${hero.name}) 역할을 맡은 배우는 ${hero.actor} 입니다.`;
  console.log(text);
}

print(ironMan);
print(captainAmerica);
