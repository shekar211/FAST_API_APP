//console.log("Hello world!");
//let x = 10;
//console.log(x);
//const y = 20;
//console.log(y);
//console.log(x+y);
function add(x,y) {
    return x+y;
}
console.log(add(10, 20));
const arr = [10,20,30,40,50];
console.log(arr[0]);
console.log(arr[1]);
console.log(arr[2]);
console.log(arr[3]);
console.log(arr[4]);

const dist = {"name": "gobi", "age": 30, "city": "New York"};
console.log(dist.name);
console.log(dist.age);
console.log(dist.city);

let a=[10,20];
let b=[30,40];
console.log(...a,...b);
console.log([...a,...b]);

// Template literals
const a = 10;
const b = 20;
console.log(`The sum of ${a} and ${b} is ${a+b}`);