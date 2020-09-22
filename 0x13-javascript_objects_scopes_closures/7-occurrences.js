#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  for (let h = 0; h < list.length; h++) {
    if (list[h] === searchElement) { occur++; }
  }
  return occur;
};
