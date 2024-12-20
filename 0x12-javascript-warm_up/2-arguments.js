#!/usr/bin/node
/* Exclude the first two elements (script name and node) */
const args = process.argv.length - 2;

if (args === 0) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments');
}
