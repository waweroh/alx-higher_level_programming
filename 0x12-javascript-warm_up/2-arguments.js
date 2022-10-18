#!/usr/bin/node
// print arguments passed

if (process.argv.length < 3) {
    console.log('No arguments');
} else if (process.argv.length === 3) { 
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
