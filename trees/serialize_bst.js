/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 402
 * Updated: 2025-04-08T13:09:07+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 402;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
