#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.height || this.width) {
      const string = 'x'.repeat(this.width);
      for (let j = 0; j < this.height; j++) {
        console.log(string);
      }
    }
  }
}

module.exports = Rectangle;
