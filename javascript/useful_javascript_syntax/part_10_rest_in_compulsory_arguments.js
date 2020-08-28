// parameters vs arguments


function sum(...rest) {
  return rest.reduce((acc, current) => acc + current, 0);
}

const numbers = [1, 2, 3, 4, 5, 6, 7, 8];
console.log(sum(...numbers));
