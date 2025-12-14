/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1253
 * Updated: 2025-12-14T22:24:30+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1253;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
