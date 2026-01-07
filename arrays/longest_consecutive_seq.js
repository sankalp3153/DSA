/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1336
 * Updated: 2026-01-07T11:34:36+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1336;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
