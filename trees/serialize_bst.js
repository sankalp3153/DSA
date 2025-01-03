/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 11
 * Updated: 2025-01-03T16:44:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 11;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
