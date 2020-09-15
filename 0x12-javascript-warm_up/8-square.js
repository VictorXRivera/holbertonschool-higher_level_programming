#!/usr/bin/node
// Print square
if ((isNaN(process.argv[2])) === false) {
  let row = '';
  for (let h = 0; h < parseInt(process.argv[2]); h++) {
    row += 'X';
  }
  for (let h = 0; h < parseInt(process.argv[2]); h++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
