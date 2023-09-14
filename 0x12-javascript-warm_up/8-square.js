#!/usr/bin/node

const args = process.argv;

if (args.length !== 3 || isNaN(parseInt(args[2]))) {
  console.log('Missing size');
} else {
  const size = parseInt(args[2]);
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
