let data = 
[
    [[4, 4, 4], 1],
    [[4, -4, 4], 1],     
    [[4.2, 3.1, 4.9], 1],
    [[4.6, 4.8, 3.4], 1],
    [[4.6, 4.8, 2.8], -1],
    [[0, 4.2, 3.7], -1],
    [[4, -1, 4.1], -1],
    [[6.3, 5.1, 4.2], -1],
    [[5, 5, 5], 1], 
    [[4, 3, 4], 1],
    [[4.2, -3.1, 3.6], 1],
    [[2.5, 3.6, 2.5], -1], 
    [[4.1, 4.3, -1], -1],
    [[-4, -4, -4], -1],
    [[2, 2, 2.2], -1], 
    [[7, 4, 3], -1], 
    [[12, 15, 6], -1],
    [[3.6, -4.1, 5.6], -1], 
    [[3.1, -4.8, 4.9], 1], 
    [[2.8, 4.6, 3.1], -1]
]

let allItems = 
[
    [4,3,3],
    [4,-1,1],
    [-2,4,5],
    [-2,-6,-1],
    [6,0,2]
]

const euclideanDistance = (a, b) => {
    if(a.length != b.length)
        throw "in euclideanDistance : length did not match"
    let sum = 0;  
    for (i = 0; i < a.length; i++) { 
        sum += (a[i] - b[i])**2
    }
    return sum**0.5
}

const manhattanDistance = (a, b) => {
    if(a.length != b.length)
        throw "in euclideanDistance : length did not match"
    let sum = 0;  
    for (i = 0; i < a.length; i++) { 
      sum += Math.abs(a[i] - b[i])
    }
    return sum
}

const classify = (data, item, k, dFunc) => {
  //map to [distance,class]
  let distanceMap = data.map(dataItem => [dFunc(dataItem[0],item),dataItem[1]]);
  
  //sort by distance
  distanceMap.sort((a, b) => {
   if (a[0] < b[0]) return -1;
   if (a[0] > b[0]) return 1;
   return 0;
   }
  )
  
  //consider only the k nearest
  let relevantEntries = distanceMap.slice(0,k)
  
  //sum the classes of relevant items
  //assuming classes are 1 and -1
  let classSum = relevantEntries.reduce( (a,b) => {return a + b[1]} , 0);
  
  //retrun the sign (if classSum is 0, 0 is returned)
  return Math.sign(classSum);
  //use this one if a tie shall be randomly choosen to 1 or -1  
//   return Math.sign(classSum ? classSum : Math.random() - 0.5);
}

let table = {};
allItems.forEach(item => {
    table[item.toString()] = {
        euclidean2 : classify(data, item,2,euclideanDistance),        
        euclidean3 : classify(data, item,3,euclideanDistance),    
        manhattan2 : classify(data, item,2,manhattanDistance),        
        manhattan3 : classify(data, item,3,manhattanDistance),        
    }
})

//if node env use log instead of table
console.table(table);