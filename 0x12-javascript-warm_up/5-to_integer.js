#!/usr/bin/node
// Script to check if argument is an integer
if ((isNaN(process.argv[2])) === false) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
