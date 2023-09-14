#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  } else if (n === 0 || n === 1) {
    return 1; // Factorial of 0 and 1 is 1
  } else {
    return n * factorial(n - 1);
  }
}

const args = process.argv;

if (args.length !== 3) {
  console.log(1);
} else {
  const num = parseInt(args[2]);
  const result = factorial(num);
  console.log(result);
}
