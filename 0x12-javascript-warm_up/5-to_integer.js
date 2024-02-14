#!/usr/bin/node
const arg1 = process.argv[2];
if (isNaN(parseInt(arg1, 10))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(arg1, 10));
}
