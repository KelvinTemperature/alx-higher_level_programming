#!/usr/bin/node
const arg = process.argv;

function factorial (num) {
  if (num === 1) {
    return (1);
  }
  return factorial(num - 1) * num;
}

if (parseInt(parseInt(arg[2]))) {
  console.log(factorial(parseInt(arg[2])));
} else {
  console.log(1);
}
