"use strict";

const scalarProduct = (a, b) => a.reduce((prev, curr, ind) => prev + curr * b[ind], 0);

const vectorAdd = (a, b) => a.map((v, i) => v + b[i]);

const vectorScale = (v, a) => v.map(val => val * a);

const euclideanNorm = v => Math.sqrt(v.reduce((prev, curr) => prev + curr * curr, 0));

const homogenizeSequence = S => S.map(entry => [[...entry[0], 1], entry[1]]);

const maxNormforSequence = S => S.reduce((prev, curr) => Math.max(prev, euclideanNorm(curr[0])), 1);

const normalizeSequence = S => S.map(item => [item[0].map(val => val / maxNormforSequence(S)), item[1]]);

const shuffle = a => {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
};

let done = false;
let steps = 0;
let w = [0, 0, 0, 0];
const S = [[[4, 2, 1], -1], [[-1, 2, -4], 1], [[8, -2, -3], 1], [[1, -1, 1], -1], [[2, -2, 5], -1], [[-6, 2, 7], -1]];
shuffle(S);
console.log(S.join("\n"));
console.log(JSON.stringify(S));
const homogeneousS = homogenizeSequence(S);
const normalizedS = normalizeSequence(homogeneousS);

while (!done) {
    done = true;
    normalizedS.forEach(entry => {
        if (Math.sign(scalarProduct(w, entry[0])) * entry[1] - 1) {
            w = vectorAdd(w, vectorScale(entry[0], entry[1]));
            console.log(w.join("\\\\"));
            steps = steps + 1;
            done = false;
        }
    });
}

//console.log(w.join("\t"));
console.log("in", steps, "steps");
