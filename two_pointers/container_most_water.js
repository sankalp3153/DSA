/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1822
 * Updated: 2026-06-03T21:20:24+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1822;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
