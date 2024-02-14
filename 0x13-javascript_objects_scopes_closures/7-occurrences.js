#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const occ = list.reduce((count, currentElement) => {
    return currentElement === searchElement ? count + 1 : count;
  }, 0);
  return occ;
};
