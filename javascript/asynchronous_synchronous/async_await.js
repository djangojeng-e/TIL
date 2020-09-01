// Async and await

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function makeError() {
  await sleep(1000);
  const error = new Error();
  throw error;
}


async function process() {
  try {
    await makeError();
  } catch (e) {
    console.error(e);
  }
}

//
// async function process() {
//     console.log('안녕하세요!');
//     await sleep(1000);
//     console.log('반갑습니다!');
// }

process()
