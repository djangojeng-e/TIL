// there had been no class in JavaScript previously
// with introduction to es6, there had been an introduction of class into Javascript just similar to other languages


class Animal {
  constructor(type, name, sound) {
    this.type = type;
    this.name = name;
    this.sound = sound;
  }
// 클래스 안에 함수는 자동으로 prototype 으로 등록
  say() {
    console.log(this.sound);
  }
}

class Dog extends Animal {
  constructor(name, sound) {
    super('개', name, sound);
  }
}

class Cat extends Animal {
 constructor(name, sound) {
   super('고양이', name, sound);
 }
}


const dog = new Dog('멍멍이', '멍멍');
const cat = new Cat('야옹이', '야옹');
const cat2 = new Cat('야오오오잉', '야야야아ㅏ아옹');


dog.say();
cat.say();
cat2.say();
