// 동기적    (Synchronous)
// 비동기적   (Asynchronous)


function work(callback) {
  setTimeout(() => {
    const start = Date.now();
    for (let i = 0; i < 1000000000; i++) {

    }
    const end = Date.now();
    console.log(end - start + 'ms');
    callback(end - start)
  }, 0)
}

console.log('작업 시작')
work((ms) => {
  console.log('작업이 끝났어요!');
  console.log(ms + 'ms 걸렸다고 해요.')
});
console.log('다음 작업');

// ajax web api requests,
// read files
// task scheduling
