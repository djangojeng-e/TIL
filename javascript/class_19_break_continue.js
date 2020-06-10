// break 와 continue
// break 와 continue 는 반복문에서 벗어나거나, 다음 반복으로 넘어가고 싶을때 사용한다.

for (let i = 0; i < 10; i++) {
  if (i === 2) continue;
  console.log(i);
  if (i === 5) break;
}
// continue, 특정 조건이 만족되면, 그 구간을 넘어가고, 다음것이 실행된다.

// if 문 내부에서, 실행할 코드가 한줄밖에 없을경우,
// if (i === 2) continue; 이런식으로 사용해도 괜찮다.

// break 는 반복문을 벗어나고, 종료 시킨다.

// continue, break 는 while, for of 같은 다른 반복문 형태에서도 사용 가능하다.
