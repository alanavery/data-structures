const nodeThree = {
  next: null,
  value: 3
};

const nodeTwo = {
  next: nodeThree,
  value: 2
};

const nodeOne = {
  next: nodeTwo,
  value: 1
};

const reverseLinkedList = (head) => {
  let nodesArray = [];
  let nextNode = head;
  while (nextNode.next) {
    nodesArray.push(nextNode);
    nextNode = nextNode.next;
  }
  nodesArray.push(nextNode);

  nodesArray = nodesArray.reverse();

  for (let i = 0; i < nodesArray.length; i++) {
    nodesArray[i].next = nodesArray[i + 1];
  }

  return nodesArray;
};

console.log(reverseLinkedList(nodeOne));
