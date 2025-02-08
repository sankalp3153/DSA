/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 172
 * Updated: 2025-02-08T19:46:59+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 172;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
