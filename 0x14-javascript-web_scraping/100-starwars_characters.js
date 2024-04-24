#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

request(url, (err, response, data) => {
  if (err) throw err;

  const dataJson = JSON.parse(data);
  dataJson.characters.forEach((value) => {
    request(value, (err, response, obj) => {
      if (err) throw err;
      const objJson = JSON.parse(obj);
      console.log(objJson.name);
    });
  });
});
