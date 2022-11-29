#!/usr/bin/node

function secondBiggest (myList) {
  const myListSet = new Set(myList);
  myList = Array.from(myListSet);
  const myListLength = myList.length;
  if (myListLength === 0 || myListLength === 1) {
    console.log('0');
  } else {
    const sndLastIndex = myListLength - 2;
    myList.sort(function(a, b) {
      return a - b;
    });
    console.log(myList[sndLastIndex]);
  }
}

secondBiggest(process.argv.slice(2));
