function solution(X, A) {
  const set = new Set(Array.from({ length: X }, (_, i) => i + 1));

  for (let i = 0; i < A.length; i++) {
    set.delete(A[i]);
    if (!set.size) {
      return i;
    }
  }

  return -1;
}
