// const a = 1;
// const b = 2;
// const equals = a === b;
// console.log(equals)

// === 와 == 의 차이점은,
// == 은 타입을 비교하진 않는다.

// == 을 두번 입력하는것은, 실수를 유발하니, 웬만하면 === 을 쓰는 습관을 들이는게 좋음
// == 도 제대로 작동을 하지만, === 가 더욱 정확한 비교를 할수 있음

// !== 같지 않은것을 비교

const a = 10;
const b = 15;
const c = 15;

console.log(a < b);
console.log(b > a);
console.log(b >= a);
console.log(a <= c);
console.log(b < c);

// 문자열을 붙이는 방법

const f = '안녕';
const g = '하세요';

console.log(f + g);
