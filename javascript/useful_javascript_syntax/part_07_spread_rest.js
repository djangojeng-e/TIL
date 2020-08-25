// introduced in es6 spread and rest ...
//
// const slime = {
//   name: '슬라임'
// };
//
// const cuteSlime = {
//   ...slime,
//   attribute: 'cute'
// };
//
// const purpleCuteSlime = {
//   ...cuteSlime,
//   color: 'purple'
// };
//
// const greenCuteSlime = {
//   ...purpleCuteSlime,
//   color: 'green',
// }
//
// console.log(slime);
// console.log(cuteSlime);
// console.log(purpleCuteSlime);
// console.log(greenCuteSlime);
// console.log(greenCuteSlime);


const anmials = ['개', '고양이', '참새'];
const anotherAnimals = [...animals, '비둘기'];

console.log(animals);
console.log(anotherAnimals);


const numbers = [1, 2, 3, 4, 5];

const spreadNumbers = [...numbers, 1000, ...numbers];
