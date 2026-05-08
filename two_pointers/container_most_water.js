/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1753
 * Updated: 2026-05-08T21:06:09+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1753;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
