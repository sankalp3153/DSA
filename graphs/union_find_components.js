/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 658
 * Updated: 2025-06-23T19:44:42+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 658;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
