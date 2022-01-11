function solution(A) {
  const set = new Set(A);

  for (let i = 1; i <= 100001; i++) {
    if (!set.has(i)) {
      return i;
    }
  }
}
