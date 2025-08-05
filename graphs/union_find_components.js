/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 796
 * Updated: 2025-08-05T15:20:02+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 796;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
