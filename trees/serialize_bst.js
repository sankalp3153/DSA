/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1115
 * Updated: 2025-11-03T23:09:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1115;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
