/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 218
 * Updated: 2025-02-22T16:46:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 218;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
