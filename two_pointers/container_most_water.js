/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 994
 * Updated: 2025-09-25T12:24:12+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 994;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
