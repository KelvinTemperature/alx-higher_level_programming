#!/usr/bin/node
const arg = process.argv;
const holder = [];

if (parseInt(arg[2])) {
  let i = 0;
  for (i = 0; i < parseInt(arg[2]); i++) {
    holder[i] = '';
    let j = 0;
    for (j = 0; j < parseInt(arg[2]); j++) {
      holder[i] = holder[i] + 'X';
    }
  }
  for (i = 0; i < holder.length; i++) {
    console.log(holder[i]);
  }
} else {
  console.log('Missing size');
}
