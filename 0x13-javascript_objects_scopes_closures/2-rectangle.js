#!/usr/bin/node
class Rectangle {
  if (typeof w !== 'number'|| typeof h !== 'number'|| w <= 0 || h <= 0)
    this.width = 0;
    this.height = 0;
  } else {
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
