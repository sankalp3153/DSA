/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 379
 * Updated: 2025-04-01T22:28:18+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 379;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
