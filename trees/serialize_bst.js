/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 586
 * Updated: 2025-06-04T19:32:48+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 586;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
