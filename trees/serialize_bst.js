/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1000
 * Updated: 2025-09-27T10:02:58+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1000;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
