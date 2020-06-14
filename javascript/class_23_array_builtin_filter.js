// filter 는 특정 조건을 만족하는 원소들을 찾아서
// 그 원소들을 가지고 새로운 배열을 만듦

const todos = [
  {
    id: 1,
    text: '자바스크립트 입문',
    done: true,
  },
  {
    id: 2,
    text: '함수 배우기',
    done: true,
  },
  {
    id: 3,
    text: '객체와 배열 배우기',
    done: true,
  },
  {
    id: 4,
    text: '배열 내장함수 배우기',
    done: false,
  }
]

// filter() 안에는 함수를 넣어준다

const tasksNotDone = todos.filter(todo => todo.done);
console.log(tasksNotDone);

// 특정배열에서 특정 조건을 만족하는 원소들을 묶어서 새로운 리스트를 만들어 낼때 굉장히 유용하다 
