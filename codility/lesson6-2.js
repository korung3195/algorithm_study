function solution(A) {
  const arr = Array.from(A).sort((a, b) => a - b);

  if (arr[arr.length - 1] < 0) {
    return arr[arr.length - 3] * arr[arr.length - 2] * arr[arr.length - 1];
  }

  return (
    arr[arr.length - 1] *
    Math.max(arr[arr.length - 2] * arr[arr.length - 3], arr[0] * arr[1])
  );
}
