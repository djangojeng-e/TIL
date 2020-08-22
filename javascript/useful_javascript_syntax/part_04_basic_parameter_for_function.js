// basic parameters for function

// when the argument is missing, there can be default argument for function
//





// function calculateCircleArea(r) {
//   const radius = r || 1;
//   return Math.PI * radius * radius;
// }

//
// function calculateCircleArea(r = 1) {
//   return Math.PI * r * r;
// }


const calculateCircleArea = (r = 1) => Math.PI * r * r;


const area = calculateCircleArea()
console.log(area)       // NaN is the result
