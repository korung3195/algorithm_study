function solution(N, A) {
  const MAX_COUNTER = N + 1;
  const map = new Map();
  let max = 0;
  let temp_max = 0;

  A.forEach((counter) => {
    if (counter == MAX_COUNTER) {
      map.clear();
      max += temp_max;
      temp_max = 0;
    } else {
      const count = map.get(counter) || 0;
      temp_max = Math.max(count + 1, temp_max);
      map.set(counter, count + 1);
    }
  });

  const arr = new Array(N).fill(max);
  [...map].forEach(([index, count]) => {
    arr[index - 1] += count;
  });

  return arr;
}
