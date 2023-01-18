#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const sentence = process.argv[3];

fs.writeFile(filePath, sentence, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
