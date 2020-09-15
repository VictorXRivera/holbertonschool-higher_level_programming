#!/usr/bin/node
// Printing the first argument passed to script
if (process.argv[3]) {
  console.log('Arguments found');
} else if (process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
