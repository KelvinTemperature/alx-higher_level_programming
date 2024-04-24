#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) throw err;

  const data = JSON.parse(body);
  const output = {};
  const arrangeData = {};
  data.forEach(obj => {
    if (arrangeData[obj.userId] === undefined) {
      arrangeData[obj.userId] = [obj];
    } else {
      arrangeData[obj.userId].push(obj);
    }
  });
  for (let i = 1; i <= Object.keys(arrangeData).length; i++)
  {
    let completed = 0;
    arrangeData[i].forEach(obj => {
      if (obj.completed === true) { completed += 1; }
    });
    output[i] = completed;
  }
  console.log(output);
});
