#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const args = process.argv;

// Check if there are exactly two arguments (two integers)
if (args.length !== 4) {
  console.log('NaN');
} else {
  const result = add(args[2], args[3]);
  if (!isNaN(result)) {
    console.log(result);
  } else {
    console.log('NaN');
  }
}
