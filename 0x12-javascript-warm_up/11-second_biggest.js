#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const integers = args.map(Number).sort((a, b) => b - a);

  const secondBiggest = integers[1];

  console.log(secondBiggest);
}
