#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, (err, response, body) => {
  if (err) throw err;

  const data = JSON.parse(body);
  let count = 0;
  const id = '18';
  const urlS = 'https://swapi-api.alx-tools.com/api/people/';

  for (let i = 0; i < data.count; i++) {
    for (let j = 0; j < (data.results[i].characters).length; j++) {
      if (data.results[i].characters[j] === (urlS + id + '/')) { count += 1; }
    }
  }
  console.log(count);
});
