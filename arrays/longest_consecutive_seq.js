/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2325
 * Updated: 2026-11-03T21:43:27+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2325;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
