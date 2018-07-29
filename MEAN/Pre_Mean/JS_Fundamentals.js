// Max Min Average
// function maxMinAvg(arr) {
//     max = arr[0];
//     min = arr[0];
//     sum = 0;
//     for (var i = 0; i < arr.length; i++) {
//         if (arr[i] > max) {
//             max = arr[i];
//         }
//         if (arr[i] < min) {
//             min = arr[i];
//         }
//         sum += arr[i];
//     }
//     var avg = sum/arr.length;
//     var newArr = [max, min, avg];
//     return newArr;
// }
// console.log(maxMinAvg([1, -2, 9, 4]));

// Fizz Buzz
// function fizzBuzz(n) {
//     for (var i = 1; i <= n; i++) {
//         if (i % 15 === 0) {
//             console.log("FizzBuzz");
//         }
//         else if (i % 3 === 0) {
//             console.log("Fizz");
//         }
//         else if (i % 5 === 0) {
//             console.log("Buzz");
//         }
//         else {
//           console.log(i);
//         }
//     }
// }
// console.log(fizzBuzz(15));

// Braces Valid
// function bracesValid(str){
//     var braces = {
//         ')' : '(',
//         ']' : '[',
//         '}' : '{'
//     };

//     var open = [];

//     for (var i = 0; i < str.length; ++i)
//         if (str[i] === '(' || str[i] === '[' || str[i] === '{')
//             open.push(str[i]);
//         else if (open[open.length-1] === braces[str[i]])
//             open.pop();
//         else
//             return false;

//     return open.length === 0;
// }
// console.log(bracesValid("[]([])"));

// Bubble Sort
// function bubbleSort(arr) {
//     for (var i = 0; i < arr.length; i++) {
//         for (var j = 0; j < (arr.length - i - 1); j++) {
//             if(arr[j] > arr[j+1]) {
//             var temp = arr[j];
//             arr[j] = arr[j+1];
//             arr[j+1] = temp;
//             }
//           console.log(arr);
//         }
//         console.log(arr);
//     }
//     return arr;
// }
// console.log(bubbleSort([5,7,1,3,6]));

// Coin Change
// function coinChange(n) {
//     var change = {
//         Dollars: 0,
//         Quarters : 0,
//         Nickels : 0,
//         Dimes : 0,
//         Pennies : 0
//     };
//     if (n >= 100) {
//         change.Dollars = Math.floor(n/100);
//         n -= change.Dollars * 100;
//     }
//     if (n >= 25) {
//         change.Q = Math.floor(n/25);
//         n -= change.Q * 25;
//     }
//     if (n >= 10) {
//         change.D = Math.floor(n/10);
//         n -= change.D * 10;
//     }
//     if (n >= 5) {
//         change.N = Math.floor(n/5);
//         n -= change.N * 5;
//     }
//     change.P = n;
//     return change;
// }
// console.log(coinChange(286));

// Users
// users = [
//     {
//       fname: "Kermit",
//       lname: "the Frog",
//       languages: ["Python", "JavaScript", "C#", "HTML", "CSS", "SQL"],
//       interests: {
//         music: ["guitar", "flute"],
//         dance: ["tap", "salsa"],
//         television: ["Black Mirror", "Stranger Things"]
//       }
//     },
//     {
//       fname: "Winnie",
//       lname: "the Pooh",
//       languages: ["Python", "Swift", "Java"],
//       interests: {
//         food: ["honey", "honeycomb"],
//         flowers: ["honeysuckle"],
//         mysteries: ["Heffalumps"]
//       }
//     },
//     {
//       fname: "Arthur",
//       lname: "Dent",
//       languages: ["JavaScript", "HTML", "Go"],
//       interests: {
//         space: ["stars", "planets", "improbability"],
//         home: ["tea", "yellow bulldozers"]
//       }
//     }
//   ];
//   function userLanguages(userlist)
//     {
//       var langlist = ""
//       for(i=0;i<userlist.length;i++)
//           {
//               langlist+= userlist[i].fname+" "+userlist[i].lname+" knows "
//               for(j=0;j<userlist[i].languages.length;j++)
//               {
//                   if(j < userlist[i].languages.length-1)
//                   {
//                       langlist += userlist[i].languages[j]
//                       langlist += ", "
//                   }
//                   else
//                   {
//                       langlist += "and "
//                       langlist += userlist[i].languages[j]
//                       langlist += "." + "\n"
//                   }
  
//               }
  
//         }
//         return langlist
//     }
//   console.log(userLanguages(users));

// Binary Search
function binarySearch (arr, val){
    var low = 0;
    var high = arr.length -1;
    var mid;      
    while (low <= high){
        mid = Math.floor(low+high/2);     
        if(arr[mid] == val) {
          return mid;
        }
        else if (arr[mid] < val) {
          low = mid+1;
        }
        else {
          high = mid-1;
        }
    }
    return -1;
}
console.log(binarySearch([1,4,5,7,9,10,15,20,26,30,31,35], 35));