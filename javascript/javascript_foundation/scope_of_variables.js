// scope

// variable scope
// spaces

// const, let
// block scope

// block is aread between { and }



// Block

{
  // this is block
  const variable = 'value';
  console.log(variable);
}

// console.log(variable); this was executed outside the block above
// the variable is declared inside the block above cannot be accessed
// from outside

// Outside to inside the block

let num = 34;

{
  let age = num + 1;
  console.log(age);
}


// nesting

{

  {
      // variable cannot be accesed here
      let value = 1
    {
      let variable = 0
      // value = 1 can be accessed from here
    }
  }
}


// var valid scope

//function scope

// var function scope

var b = 0;

// var can be assigned with othier value any time

 console.log(b);



 // block scope

 var c = 0;

 {
   c++;
   console.log(c);
 }

 {
   var d = 0;
   console.log(d);
 }

 console.log(d);
