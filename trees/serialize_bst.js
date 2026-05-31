/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1805
 * Updated: 2026-05-31T18:03:10+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1805;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
