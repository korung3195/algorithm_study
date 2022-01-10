function solution(A) {
  const set = new Set(A);
  for (let x = 1; x <= A.length + 1; x++) {
    if (!set.has(x)) {
      return x;
    }
  }
}
