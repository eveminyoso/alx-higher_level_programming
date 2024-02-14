#!/usr/bin/node
exports.esrever = function (list) {
  if (!Array.isArray(list)) {
    throw new Error('Input is not an array');
  }
  const rev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
