function solution(A) {
  let min_diff = Infinity;
  let left_sum = 0;
  let right_sum = A.reduce((prev, curr) => prev + curr);

  for (let i = 0; i < A.length - 1; i++) {
    left_sum += A[i];
    right_sum -= A[i];
    min_diff = Math.min(min_diff, Math.abs(left_sum - right_sum));
  }

  return min_diff;
}
