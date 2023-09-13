#!/usr/bin/node

const args = process.argv;

if (args.length < 3) {
  console.log('Not a number');
} else {
  const intValue = parseInt(args[2]);
  if (!isNaN(intValue)) {
    console.log('My number:', intValue);
  } else {
    console.log('Not a number');
  }
}
