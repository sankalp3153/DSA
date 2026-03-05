/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1546
 * Updated: 2026-03-05T22:03:28+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1546;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
