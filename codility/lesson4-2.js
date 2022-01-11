function solution(A) {
  const set = new Set(A);

  for (let i = 1; i <= A.length; i++) {
    if (!set.has(i)) {
      return 0;
    }
  }

  return 1;
}
