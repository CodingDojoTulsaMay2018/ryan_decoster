// 1.
function GreaterThanY(arr, Y){
    var count = 0;
    for(i = 0; i < arr.length; i++){
        if(arr[i] > Y){
            count++;
        }
    }
    return count;
}
console.log(GreaterThanY([2,6,8,9,10], 5));


// 2.
function MaxMinAvg(arr){
    var max = arr[0];
    var min = arr[0];
    var sum = arr[0];
    for(i = 1; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
        if(arr[i] < min){
            min = arr[i];
        }
        sum += arr[i];
    }
    var avg = sum/arr.length;
    var arrnew = [max, min, avg];
    return arrnew;
}
console.log(MaxMinAvg([1,2,3]));


// 3.
function replaceNegatives(arr){
    for(i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 'Dojo';
        }
    }
    return arr;
}
console.log(replaceNegatives([1,2,-3,-5,5]));


// 4.
function removeVals(arr, x, y){

    for(i = arr[arr.length-1]; i >= 0; i--){
        if(i >= x && i <= y){
            arr[i] = arr[arr.length - 1];
            arr.pop();
            console.log(arr);
        }
    }
    return arr;
}
console.log(removeVals([20,30,40,50,60,70], 2, 4));





