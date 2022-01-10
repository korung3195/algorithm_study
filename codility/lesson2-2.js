function solution(A) {
  const set = new Set();

  for (let num of A) {
    if (set.has(num)) {
      set.delete(num);
    } else {
      set.add(num);
    }
  }

  return Array.from(set).pop();
}
