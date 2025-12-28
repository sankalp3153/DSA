/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1299
 * Updated: 2025-12-28T10:20:02+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1299;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
