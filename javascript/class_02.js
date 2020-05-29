let value = 1;
console.log(value)

// let value = 2;
// 변수는 바뀔수 있는 값

// 상수는, const 를 사용하여 지정
// 값이 바뀔수 없다

const b = 1;
// a = 2; 상수는 바뀔수 없으므로, 에러가 남

// var 라는 키워드는 옛날에 사용했던 방식
// let 이랑 비슷한데, var 를 사용하면, 변수를 바꿀수 있음

var a = 1;
var a = 2;

// 실제 개발을 할때는, var 를 사용하는 경우가 별로 없으므로, 넘어가도 됨

console.log(a)
console.log(b)

// 자바스크립트의 데이터 타입

// 1. 문자열
// * 세미콜론은 있어도 되고 없어도 됨
let text = 'hello';
let name = "헬로우 자바스크립트";

// 2. 불리언
// 참 혹은 거짓
// True 와 False 두가지만 있음

let good = true;
let loading = false;

// null 과 undefined
// null 은 아예 없다를 의미
// undefined 는 아직 정의되지 않았다는것을 의미

let nothing = null;
let no_defined = undefined;
