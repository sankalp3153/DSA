/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1736
 * Updated: 2026-05-04T22:04:41+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1736;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
