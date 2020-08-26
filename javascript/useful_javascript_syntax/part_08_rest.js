//
//
// const purpleCuteSlime = {
//   name: '슬라임',
//   attribute: 'cute',
//   color: 'purple'
// };
//
//
// const {color, ...cuteSlime } = purpleCuteSlime;
//
// console.log(color);
// console.log(cuteSlime);
//
// const { attribute, ...slime } = cuteSlime;
//
// console.log(slime);
//
// // spread 는 특정 객체나 배열안에 다른 객체나 배열을 펼쳐주는 역할을 합니다.
// // rest 는 퍼저 있는것을 다시 모아주는 역할
//
//

const numbers = [0, 1, 2, 3, 4, 5, 6];

const [one, ...rest] = numbers;
console.log(one);
console.log(rest);

// rest cannot be in front of array
