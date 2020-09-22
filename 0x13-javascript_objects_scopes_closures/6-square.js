#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    let width = '';
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < this.width; i++) {
      width += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(width);
    }
  }
}
module.exports = Square;
