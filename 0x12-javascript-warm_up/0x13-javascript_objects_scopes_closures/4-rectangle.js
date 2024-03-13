#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const holder = [];
    let i;

    for (i = 0; i < this.height; i++) {
      holder[i] = '';
      let j;
      for (j = 0; j < this.width; j++) {
        holder[i] += 'X';
      }
    }
    for (i = 0; i < holder.length; i++) {
      console.log(holder[i]);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
