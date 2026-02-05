/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1431
 * Updated: 2026-02-05T10:26:51+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1431;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
