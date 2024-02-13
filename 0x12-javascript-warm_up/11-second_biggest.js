#!/usr/bin/node
const args = process.argv.slice(2);
const integers = args.map(arg => parseInt(arg));
if (integers.length === 0 || integers.length === 1) {
	  console.log(0);
} else {
	  const max = Math.max(...integers);
	  integers.splice(integers.indexOf(max), 1);
	  const secondMax = Math.max(...integers);
	  console.log(secondMax);
}
