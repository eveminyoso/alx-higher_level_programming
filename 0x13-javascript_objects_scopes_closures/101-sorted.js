#!/usr/bin/node
const { dict } = require('./101-data');
const usersOcc = {};
for (const userId in dict) {
  const occ = dict[userId];
  usersOcc[occ] = usersOcc[occ] || [];
  usersOcc[occ].push(parseInt(userId, 10));
}
console.log(usersOcc);
