// ${} 안에 변수를 넣을수 있음
// 단! `` 안에 있는 내용만 이렇게 사용할수 있다.

function hello(name) {
  return `Hello ${name}!`;
}

const result = hello('djangojenge');
console.log(result)
