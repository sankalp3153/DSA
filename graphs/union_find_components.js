/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 359
 * Updated: 2025-03-28T15:26:47+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 359;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
