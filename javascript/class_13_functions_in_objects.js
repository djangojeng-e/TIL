// 객체안에 함수 넣기

const dog = {
  name: '멍멍이',
  sound: '멍멍!',
  say: function() {
    console.log(this.sound);
  }
};

// this.sound 는 python 에서 self 랑 비슷한것 같다

const cat = {
  name: '야옹이',
  sound: '야옹~',
};

cat.say = dog.say;
dog.say()
cat.say()

// 함수안에 this 는, 자신이 속해있는곳을 참조 
