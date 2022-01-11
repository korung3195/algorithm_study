function solution(A) {
  const avg = [];
  let minAvg = Infinity;
  let index = -1;

  for (let i = 1; i < A.length; i++) {
    avg[i] = (A[i - 1] + A[i]) / 2;
    if (avg[i] < minAvg) {
      minAvg = avg[i];
      index = i - 1;
    }

    if (i == 1) {
      continue;
    }

    const temp_avg = (avg[i - 1] * 2 + A[i]) / 3;
    if (temp_avg < minAvg) {
      minAvg = temp_avg;
      index = i - 2;
    }
  }

  return index;
}
