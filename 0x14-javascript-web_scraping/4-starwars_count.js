#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (err, response, body) => {
  if (err) {console.log(err);}

  const data = JSON.parse(body);
  let count = 0;

  for (let i = 0; i < data.count; i++) {
    for (let j = 0; j < (data.results[i].characters).length; j++) {
      if (data.results[i].characters[j].includes('18')) { count += 1; }
    }
  }
  console.log(count);
});
