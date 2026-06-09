/**
 * Module: serialize_bst
 * Approach: preorder bound reconstruction
 * Revision: 1851
 * Updated: 2026-06-09T22:15:06+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1851;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
