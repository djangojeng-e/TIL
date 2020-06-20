// 반복문 for
// 반복문은 특정 작업을 반복적으로 행하려고 할때 사용되는 구문

// 시작 -> 조건 -> true 일 경우 -> 특정 구문을 실행 시킴
// 시작 -> 조건 -> false 일 경우 -> 반복을 끝냄

// 특정 조건이 만족하는동안, 계속 실행시키고, 조건이 만족되지  않으면, 반복문을 종료한다

// 여러종류가 있는데, for 문을 먼저 알아본다.
// for (시작지점; 조건; 카운터)
//
// for (let i = 0; i < 10; i++) {
//   console.log(i);
// }

for (let i = 10; i >= 0; i-=2) {
  console.log(i)
}

// for 문의 구조와 사용법을 외워서 사용하면 된다.

// for 문과 배열을 같이 사용해보기

const names = ['멍멍이', '야옹이', '멍뭉이'];

for (let i = 0; i < names.length; i++) {
  console.log(names[i]);
}