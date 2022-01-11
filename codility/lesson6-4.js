function solution(A) {
  const arr = A.map((r, i) => [i - r, i + r]).sort((a, b) => a[0] - b[0]);
  const LIMIT = 10000000;

  let res = 0;

  for (let i = 0; i < A.length; i++) {
    let cross = 0;

    for (let j = i + 1; j < A.length; j++) {
      if (arr[j][0] > arr[i][1]) {
        break;
      }

      cross += 1;
    }

    res += cross;

    if (res > LIMIT) {
      return -1;
    }
  }

  return res;
}
