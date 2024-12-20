#!/usr/bin/node

/**
 * Prints a square of size 'size', where 'size' is the first argument.
 * If the argument is not a valid number, print "Missing size".
 */

const size = parseInt(process.argv[2]);

if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
