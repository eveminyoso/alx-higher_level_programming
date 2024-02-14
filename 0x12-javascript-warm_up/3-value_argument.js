#!/usr/bin/node
const first = process.argv[2];
if (first) {
  console.log(first);
} else {
  console.log('No argument');
}
