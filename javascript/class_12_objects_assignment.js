// unstrctured assignment
// es6 에서 제공하는, 비구조화 할당을 사용하면, 좀더 편하게 코드를 사용할수 있다.
// 객체 구조 분해라고도 불림


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

// 객체에서 특정 값들을 빼내는 것을 함


// function print(hero) {
//   const { alias, name, actor } = hero;
//   const text = `${alias}(${name}) 역할을 맡은 배우는 ${actor} 입니다.`;
//   console.log(text);
// }


function print({ alias, name, actor }) {
  const text = `${alias}(${name}) 역할을 맡은 배우는 ${actor} 입니다.`;
  console.log(text);
}

print(ironMan);
print(captainAmerica);
