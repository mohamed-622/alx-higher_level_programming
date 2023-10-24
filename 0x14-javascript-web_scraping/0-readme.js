#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2] || __filename;

fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
}
);
