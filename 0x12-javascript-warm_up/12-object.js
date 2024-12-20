#!/usr/bin/node

/**
 * Create an object `myObject` with properties `type` and `value`
 * The initial value of `value` is 12
 */
const myObject = {
  type: 'object',
  value: 12
};

/**
 * Print the object to the console before modification
 */
console.log(myObject);

/**
 * Replace the value of `myObject.value` from 12 to 89
 */
myObject.value = 89;

/**
 * Print the object to the console after modification
 */
console.log(myObject);
