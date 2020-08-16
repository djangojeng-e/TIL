class Food {
  constructor(name) {
    this.name = name;
    this.brands = [];
  }

  addBrand(brand) {
    this.brands.push(brand)
  }

  print() {
    console.log(`${this.name} 을 파는 음식점들:`)
    console.log(this.brands.join(', '));
  }

}


const pizza = new Food('피자');
pizza.addBrand('피자헛');
pizza.addBrand('도미노');

const chicken = new Food('치킨');
chicken.addBrand('굽네치킨');
chicken.addBrand('BBQ');

pizza.print()
chicken.print()


// class 를 사용하면, 같은 반복적으로 히야하는 코드에 대해서 반복을 피할수 있음.
