function solution(S, P, Q) {
  const arrA = new Array(S.length).fill(-1);
  const arrC = new Array(S.length).fill(-1);
  const arrG = new Array(S.length).fill(-1);

  const res = [];

  for (let i = 0; i < S.length; i++) {
    if (i > 0) {
      arrA[i] = arrA[i - 1];
      arrC[i] = arrC[i - 1];
      arrG[i] = arrG[i - 1];
    }

    if (S[i] === "A") {
      arrA[i] = i;
    } else if (S[i] === "C") {
      arrC[i] = i;
    } else if (S[i] === "G") {
      arrG[i] = i;
    }
  }

  for (let i = 0; i < P.length; i++) {
    const start = P[i];
    const end = Q[i];

    if (arrA[end] >= start) {
      res.push(1);
    } else if (arrC[end] >= start) {
      res.push(2);
    } else if (arrG[end] >= start) {
      res.push(3);
    } else {
      res.push(4);
    }
  }

  return res;
}
