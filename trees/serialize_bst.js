/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1621
 * Updated: 2026-03-27T10:07:00+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1621;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
