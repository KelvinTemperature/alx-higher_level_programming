#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) throw err;

  const data = JSON.parse(body);
  const output = {};
  for (let i = 1; i <= data.length; i++)
  {
    let completed = 0;
    for (let j = 0; j < data.length; j++){
      if (data[i][j].completed === true) {completed += 1}
    }
    output[i] = completed;
  }
  console.log(output);
});
