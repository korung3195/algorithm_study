function solution(A) {
  const arr = Array.from(A).sort((a, b) => a - b);

  for (let i = 2; i < arr.length; i++) {
    if (arr[i - 2] + arr[i - 1] > arr[i]) {
      return 1;
    }
  }
  return 0;
}
