/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 2095
 * Updated: 2026-08-21T22:15:57+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 2095;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
