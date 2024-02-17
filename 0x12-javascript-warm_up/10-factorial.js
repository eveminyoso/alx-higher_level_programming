#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
const arg1 = process.argv[2];
const n = parseInt(arg1);
if (!isNaN(n)) {
  const result = factorial(n);
  console.log(result);
} else {
  console.log(1);
}
