/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 356
 * Updated: 2025-03-25T23:11:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 356;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
