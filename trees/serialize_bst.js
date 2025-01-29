/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 126
 * Updated: 2025-01-29T22:23:36+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 126;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
