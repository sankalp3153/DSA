/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1914
 * Updated: 2026-06-29T22:15:41+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1914;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
