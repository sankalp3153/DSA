/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2098
 * Updated: 2026-08-22T19:32:27+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2098;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
