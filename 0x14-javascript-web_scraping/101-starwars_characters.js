#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
let id = parseInt(process.argv[2]);
let characters = [];

request(url, (err, response, data) => {
  if (err) throw err;

  const dataJson = JSON.parse(data);
  const result = dataJson.results;

  if (id === 7) {
    id = 7;
  } else if (id < 4) {
    id += 3;
  } else {
    id -= 3;
  }

  for (let i = 0; i < result.length; i++) {
    if (result[i].episode_id === id) {
      characters = result[i].characters;
      break;
    }
  }

  characters.forEach((value) => {
    request(value, (err, response, obj) => {
      if (err) throw err;
      const objJson = JSON.parse(obj);
      console.log(objJson.name);
    });
  });
});
