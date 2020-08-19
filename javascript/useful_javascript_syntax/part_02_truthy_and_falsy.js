// Truthy and Falsy

// truthy is like True
// Falsy is just like Falsy

console.log(!undefined);
console.log(!null);

// In javascript, undefined , null are falsy values

console.log(!0);
console.log(!'');
console.log(!NaN);
console.log(!false);


console.log(!3);
console.log(!'hello');
console.log(!['array']);
console.log(![]);
console.log(!{});


const value = { a: 1 };

if (value) {
  console.log('value 가 truthy 하네요');
}

const truthy = value ? true : false;
console.log(truthy);


// falsy values are  undefined, null, 0, '', NaN
