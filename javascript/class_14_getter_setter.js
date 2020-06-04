// getter and setter in objects
// getter 함수는, 특정값을 조회하려고 할때 사용한다.
// 특정코드를 실행시키고, 연산시켜 나온 값을 사용할때 사용한다.

// const numbers = {
//   a: 1,
//   b: 2,
//   get sum() {
//     console.log('sum 함수가 실행됩니다!');
//     return this.a + this.b;
//   }
// };
//
// console.log(numbers.sum);
// numbers.b = 5;
// console.log(numbers.sum);

// getter 함수를 설정 앞에다가 get 이라고 적음
// setter  함수는 함수를 설정할때, 앞에다가 set 이라고 적음


const dog = {
  _name: '멍멍이',
  set name(value) {
    console.log('이름이 바뀝니다.. ' + value);
    this._name = value;
  }
};

console.log(dog.name);
dog.name = '뭉뭉이';
console.log(dog.name);


const numbers = {
  _a: 1,
  _b: 2,
  sum: 3,
  calculate() {
    console.log('calculate');
    this.sum = this._a + this._b;
  },
  get a() {
    return this._a;
  },
  get b() {
    return this._b;
  },
  set a(value) {
    this._a = value;
    this.calculate();
  },
  set b(value) {
    this._b = value;
    this.calculate();
  }
};

console.log(numbers.sum);
numbers.a = 5;
