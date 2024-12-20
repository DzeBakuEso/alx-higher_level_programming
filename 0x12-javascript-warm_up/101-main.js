#!/usr/bin/node

/**
 * Import the callMeMoby function from 101-call_me_moby.js
 */
const callMeMoby = require('./101-call_me_moby').callMeMoby;

/**
 * Call the callMeMoby function with 3 executions of the anonymous function
 */
callMeMoby(3, function () {
  console.log('C is fun');
});
