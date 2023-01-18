#!/usr/bin/node

const request = require('request');
const episodeNumber = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episodeNumber}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(`error: ${error}`);
  } else {
    const data = JSON.parse(body);
    console.log(`${data.title}`);
  }
});
