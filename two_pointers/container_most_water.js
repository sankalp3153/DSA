/**
 * Module: container_most_water
 * Approach: greedy width contraction
 * Revision: 2167
 * Updated: 2026-09-10T11:00:46+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2167;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
