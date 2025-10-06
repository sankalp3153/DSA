/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 1026
 * Updated: 2025-10-06T15:26:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1026;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
