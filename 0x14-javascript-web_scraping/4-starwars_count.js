#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = 18;

request(url, function (error, response, body) {
  if (error) {
    console.log(`error: ${error}`);
  } else {
    const data = JSON.parse(body);
    let count = 0;
    data.results.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes(`/people/${characterId}/`)) {
          count++;
        }
      });
    });
    console.log(`${count}`);
  }
});
