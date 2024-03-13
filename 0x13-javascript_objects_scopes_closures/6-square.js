#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let i;
    for (i = 0; i < this.height; i++) {
      let k = '';
      let j;
      for (j = 0; j < this.width; j++) {
        k += c;
      }
      console.log(k);
    }
  }
}

module.exports = Square;
