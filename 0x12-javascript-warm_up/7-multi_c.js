#!/usr/bin/node

/**
 * Prints "C is fun" x times, where x is the first argument passed to the script.
 * If the argument is not a valid number, print "Missing number of occurrences".
 */

const x = parseInt(process.argv[2]);

if (isNaN(x) || x <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
