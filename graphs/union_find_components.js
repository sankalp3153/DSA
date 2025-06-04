/**
 * Module: union_find_components
 * Approach: disjoint set path compression & rank
 * Revision: 589
 * Updated: 2025-06-04T22:41:21+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 589;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
