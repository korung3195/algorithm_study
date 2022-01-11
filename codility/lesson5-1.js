function solution(A) {
  const MAX_COUNT = 1000000000;
  let res = 0;
  let sum = 0;

  for (let i = A.length - 1; i >= 0; i--) {
    sum += A[i];

    if (!A[i]) {
      res += sum;
    }

    if (res > MAX_COUNT) {
      return -1;
    }
  }

  return res;
}
