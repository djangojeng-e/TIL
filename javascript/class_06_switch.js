
const device = 'iphone';

switch (device) {
  case 'iphone':
    console.log('아이폰!');
    break;
  case 'ipad':
    console.log('아이패드!');
    break;
  case 'galaxy note':
    console.log('겔럭시 노트!');
    break;
  default:
    console.log('모르겠어요..');
}

// break 를 하지 않았을 경우에는, 다음 케이스를 실행한다
// 모든 case 에 break 를 사용하지 않으면, 모든 케이스에 대한 조건 테스트를 한다.
// 따라서, break 를 사용하여, switch 문을 빠져나오는것이 중요하다.
