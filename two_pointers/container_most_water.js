/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1362
 * Updated: 2026-01-16T10:14:37+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1362;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
