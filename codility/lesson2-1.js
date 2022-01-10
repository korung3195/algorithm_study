function solution(A, K) {
  const target = A.length - (K % A.length);
  const leftArr = A.slice(0, target);
  const rightArr = A.slice(target);
  return rightArr.concat(leftArr);
}
