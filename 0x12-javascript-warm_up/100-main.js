#!/usr/bin/node

/** 
 * Initial value of myVar
 */
myVar = 89;

/** 
 * Require the script that modifies myVar
 */
require('./100-let_me_const');

/** 
 * Print the modified value of myVar
 */
console.log(myVar);  /* Should print 333 */ 
