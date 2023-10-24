#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2] || __filename;
const text = process.argv[3];

fs.writeFile(file, text, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
}
);
