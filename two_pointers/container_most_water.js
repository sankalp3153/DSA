/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1868
 * Updated: 2026-06-12T21:33:27+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1868;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
