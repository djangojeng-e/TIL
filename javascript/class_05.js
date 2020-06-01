// 조건문

// 조건문을 사용하면, 특수한 상황에 특정 작업을 실행 가능

// 1. if 문
// 특정 조건이 만족될때만, 특정 코드가 실행
// 중괄호 안에 있는 구문이 실행됨
// if 뒤에 오는 소괄호 안에 있는것이 조건
// 소괄호 안의 조건이 맞으면, 중괄호 안에 있는 구문 (코드 블럭)이 실행된다.

const a = 1;
if (a + 1 === 2) {
  console.log('a+1 이 2 입니다.');
}

const b = 2;
if (b + 1 === 3) {
  const b = 1;
  console.log('if 문 안의 b 값은 ' + b);
}

console.log('if문 밖의 b 값은 ' + b);

// if else

const c = 10;
if (a > 15) {
  console.log('c가 15보다 큽니다. ');
} else{
  console.log('c 가 15보다 크지 않습니다. ');
}

// if else if

const d = 10;
if (d === 5) {
  console.log('5 입니다!');
} else if (a === 10) {
  console.log('10 입니다!');
} else {
  console.log('5도 아니고 10도 아닙니다!');
}

// 파이썬과는 다르게 elif 대신에 else if 라고 씀. 
