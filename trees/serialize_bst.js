/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 977
 * Updated: 2025-09-21T10:42:12+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 977;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
