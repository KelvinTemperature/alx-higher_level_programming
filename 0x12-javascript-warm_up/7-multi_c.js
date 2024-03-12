#!/usr/bin/node
const arg = process.argv;
let i = 0;

if (parseInt(arg[2])) {
  for (i = 0; i < parseInt(arg[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
