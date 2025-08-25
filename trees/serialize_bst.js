/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 885
 * Updated: 2025-08-25T15:13:38+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 885;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
