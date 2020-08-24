// objects
//
// const object = { a: 1, b: 2 };
// // const { a, b } = object;
// // console.log(a);
// // console.log(b);
// //
// // function print({a, b = 2}) {
// //   console.log(a);
// //   console.log(b || 2);
// // }
//
//
//
// const { a, b = 2 } = object;
// console.log(a);
// console.log(b);
//
//
// const animal = {
//   name: '멍멍이',
//   type: '개'
// };
//
// const { name: nickname } = animal;
//
// console.log(nickname);
// console.log(animal);


// const array = [ 1, 2 ];
//
// // const one = array[0];
// // const two = array[1];
//
// const [one, two = 2] = array;
//
// console.log(one);
// console.log(two);
//

const deepObject = {
  state: {
    information: {
      name: 'django',
      languages: ['korean', 'english', 'chinese']
    }
  },
  value: 5
}

const { name, languages } = deepObject.state.information;
const { value } = deepObject;

const extracted = {
  name,
  languages,
  value
};

console.log(extracted)
