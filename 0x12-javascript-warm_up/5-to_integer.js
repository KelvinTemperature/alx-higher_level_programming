#!/usr/bin/node
const arg = process.argv;

if (parseInt(arg[2])) {
  console.log('My number: ' + parseInt(arg[2]));
} else {
  console.log('Not a number');
}
