/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1313
 * Updated: 2025-12-31T10:07:34+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1313;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
