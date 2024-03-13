#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  let i;
  let j = 0;

  for (i = list.length - 1; i >= 0; i--, j++) {
    rev[j] = list[i];
  }
  return (rev);
};
