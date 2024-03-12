#!/usr/bin/node
const arg = process.argv;

if (arg.length < 3) {
  console.log('No argument');
} else if (arg.length === 3) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}
