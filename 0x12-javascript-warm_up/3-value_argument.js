#!/usr/bin/node
// Printing the first argument passed to script
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
