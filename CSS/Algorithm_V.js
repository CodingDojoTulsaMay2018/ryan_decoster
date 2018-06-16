// 1.
function negativeToZero(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0;
        }
    }
    return arr;
}
console.log(negativeToZero([1,2,-1,-3]));


// 2.
function moveForward(arr){
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i+1]
    }
    arr[arr.length-1] = 0;
    return arr;
}
console.log(moveForward([1,2,3]));


// 3.
function reverse(arr){
    for(var i = 0; i <= arr.length/2; i++){
        temp = arr[i];
        arr[i] = arr[arr.length-(i+1)]
        arr[arr.length-(i+1)] = temp;
    }
    return arr;
}
console.log(reverse([1,2,3,4,5]));


// 4.
function repeatTwice(arr){
    var arrnew = [];
    for(var i = 0; i < arr.length; i++){
        arrnew.push(arr[i])
        arrnew.push(arr[i])
    }
    return arrnew;
}
console.log(repeatTwice([4,"Ulysses", 42, false]));




function removeInner(arr, lowIdx, highIdx){
    if (lowIdx < 0 || highIdx > arr.length - 1 || (highIdx - lowIdx) >= arr.length - 1){
        return null;
    } 
    else {
        for (var i = lowIdx, j = highIdx + 1; j < arr.length; i++, j++) {
            arr[i] = arr[j];
        } 
        arr.length -= highIdx - lowIdx + 1;
    } 
    return arr; 
}

console.log(removeInner([20,30,40,50,60,70,80],2,4));

