/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 1040
 * Updated: 2025-10-09T17:06:45+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1040;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
