// // // promise 는 비동기 처리를 조금 더 쉽게 할수 있도록 도입된 ES6
// // // 원래는 라이브러리로 존재 했지만, 편리하기 때문에 ES6 스펙에 도입이 됨
// //
// // function increaseAndPrint(n , callback) {
// //   setTimeout(() => {
// //     const increased = n + 1;
// //     console.log(increased);
// //     if (callback) {
// //       callback(increased)
// //     }
// //   }, 1000)
// // }
// //
// // increasedAndPrint(0, n => {
// //   increasedAndPrint(n, n => {
// //     increaseAndPrint(n, n => {
// //       increaseAndPrint(n, n=> {
// //         increasedAndPrint(n, n=> {
// //           console.log('작업 끝!')
// //         })
// //       })
// //     })
// //   });
// // });
//
//
// // promise
//
// const myPromise = new Promise((resolve, reject) => {
//   // 구현...
//   setTimeout(() => {
//     reject(new Error());
//   }, 1000)
// });
//
// myPromise.then(result => {
//   console.log(result);
// }).catch(e => {
//   console.error(e);
// })


function increaseAndPrint(n) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const value = n + 1;
      if (value === 5) {
        const error = new Error();
        error.name = 'ValueIsFiveError';
        reject(error);
        return;
      }
      console.log(value);
      resolve(value);
    }, 1000)
  });
}

increaseAndPrint(0).then(increaseAndPrint)
.then(increaseAndPrint)
.then(increaseAndPrint)
.then(increaseAndPrint)
.then(increaseAndPrint)
.catch(e => {
  console.error(e);
});
