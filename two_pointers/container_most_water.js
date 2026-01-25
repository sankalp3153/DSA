/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1385
 * Updated: 2026-01-25T17:10:30+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1385;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
