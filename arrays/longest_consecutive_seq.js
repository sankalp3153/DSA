/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1842
 * Updated: 2026-06-07T20:08:43+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1842;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
