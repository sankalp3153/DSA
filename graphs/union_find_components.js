/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 152
 * Updated: 2025-02-04T10:16:42+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 152;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
