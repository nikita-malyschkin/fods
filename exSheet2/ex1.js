"use strict";

const scalarProduct = (a, b) => a.reduce((prev, curr, ind) => prev + curr * b[ind], 0);

const vectorAdd = (a, b) => a.map((v, i) => v + b[i]);

const vectorScale = (v, a) => v.map(val => val * a);

const euclideanNorm = v => Math.sqrt(v.reduce((prev, curr) => prev + curr * curr, 0));

const maxNormforSequence = S => S.reduce((prev, curr) => Math.max(prev, euclideanNorm(curr[0])), 1);

const normalizeSequence = S => S.map(item => [item[0].map(val => val / maxNormforSequence(S)), item[1]]);

let done = false;
let steps = 0;
let w = [0, 0, 0];
const S = [[[4, 2, 1], -1], [[-1, 2, -4], 1], [[8, -2, -3], 1], [[1, -1, 1], -1], [[2, -2, 5], -1], [[-6, 2, 7], -1]];
const normalizedS = normalizeSequence(S);

while (!done) {
    done = true;
    steps = steps + 1;
    console.log("new round");
    console.log(w);
    normalizedS.forEach(entry => {
        console.log(entry);
        if (Math.sign(scalarProduct(w, entry[0])) * entry[1] - 1) {
            w = vectorAdd(w, vectorScale(entry[0], entry[1]));
            done = false;
        }
    });
}

console.log(w, steps);
// y=np.array([-1,1,1,-1,-1,-1])
// finished=False

// while (finished==False):
//     finished=True
//     steps=0
//     for t in range(0,6):
//         if (np.sign(np.dot(w,x[t]))!=y[t]):
//             w=w+y[t]*x[t]
//             steps+=1
//             print(w)
//             finished=False
// print("Finished in "+str(steps)+" steps")
