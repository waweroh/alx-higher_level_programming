#!/usr/bin/node
// Arguments with Javascript

const arg = process.argv[2];

if (arg) {
  console.log(arg);
} else {
  console.log('No argument');
}
