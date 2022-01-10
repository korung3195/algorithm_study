function solution(N) {
  const bin = N.toString(2);
  const bin_arr = Array.from(bin);

  let max_gap = 0;
  let gap = 0;
  let flag = false;

  for (let n of bin_arr) {
    if (n === "1") {
      flag = true;
      max_gap = Math.max(max_gap, gap);
      gap = 0;
    } else if (flag) {
      gap += 1;
    }
  }

  return max_gap;
}
