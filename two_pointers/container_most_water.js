/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1891
 * Updated: 2026-06-21T21:07:51+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1891;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
