"use strict";

const scalarProduct = (a, b) => a.reduce((prev, curr, ind) => prev + curr * b[ind], 0);

const vectorAdd = (a, b) => a.map((v, i) => v + b[i]);

const vectorScale = (v, a) => v.map(val => val * a);

const euclideanNorm = v => Math.sqrt(v.reduce((prev, curr) => prev + curr * curr, 0));

const maxNormforSequence = S => S.reduce((prev, curr) => Math.max(prev, euclideanNorm(curr)), 1);

const euclideanDistance = (a, b) => {
    if (a.length != b.length) {
        throw "in euclideanDistance : length did not match";
    }
    let sum = 0;
    for (let i = 0; i < a.length; i++) {
        sum += (a[i] - b[i]) * (a[i] - b[i]);
    }
    return Math.pow(sum, 0.5);
};

const kMeansCluster = (k, S) => {
    const dim = S[0].length;
    const maxNorm = maxNormforSequence(S);
    let z = new Array(k)
        .fill(0)
        .map(i => new Array(dim).fill(0).map(i => Math.random()))
        .map(i => vectorScale(i, maxNorm / Math.sqrt(scalarProduct(i, i))));
    z = [[100, 100], [200, 200], [3, 8]];
    let C = new Array(k).fill([]);
    let oldC = new Array(k).fill([1]);
    console.log(z);

    while (JSON.stringify(C) !== JSON.stringify(oldC)) {
        oldC = C;
        C = new Array(k).fill([]).map(i => []);
        S.forEach(x => {
            const [_, ind] = z.map(i => euclideanDistance(i, x)).reduce((prev, curr, ind) => {
                return prev[0] > curr ? [curr, ind] : prev;
            },
            [Infinity, -1]);
            C[ind].push(x);
        });
        console.log(C);
        z = C.map(
            i =>
                i.length
                    ? vectorScale(
                          i.reduce((prev, curr) => {
                              return vectorAdd(prev, curr);
                          }, new Array(dim).fill(0)),
                          1 / i.length
                      )
                    : new Array(dim).fill(0)
        );
        console.log(z);
        console.log("======");
    }
};

const S = [[2, 12], [3, 11], [3, 8], [5, 4], [7, 5], [7, 3], [10, 8], [13, 8]];

kMeansCluster(3, S);
