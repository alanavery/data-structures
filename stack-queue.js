const myStack = {
  values: [],
  push: function (newValue) {
    this.values.unshift(newValue);
  },
  pop: function () {
    this.values.shift();
  }
};

myStack.push('Hello!');
myStack.push('Bye.');
myStack.push('Huh?');

console.log(myStack);

myStack.pop();

console.log(myStack);

const myQueue = {
  values: [],
  push: function (newValue) {
    this.values.unshift(newValue);
  },
  pop: function () {
    this.values.pop();
  }
};

myQueue.push('Hello!');
myQueue.push('Bye.');
myQueue.push('Huh?');

console.log(myQueue);

myQueue.pop();

console.log(myQueue);
