#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint(); // Print the square using default character 'X'

s1.charPrint('C'); // Print the square using the character 'C'
