/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 681
 * Updated: 2025-06-27T18:12:01+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 681;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
