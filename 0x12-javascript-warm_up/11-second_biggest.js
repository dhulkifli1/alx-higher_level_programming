#!/usr/bin/node

function secondBiggest (myList) {
  let myListLength = myList.length;
  if (myListLength === 0 || myListLength === 1) {
    console.log('0');
  } else {
    const myListSet = new Set(myList);
    myList = Array.from(myListSet);
    myListLength = myList.length;
    const sndLastIndex = myListLength - 2;
    myList = myList.sort();
    console.log(myList[sndLastIndex]);
  }
}

secondBiggest(process.argv.slice(2));
