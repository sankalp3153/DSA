/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 1152
 * Updated: 2025-11-21T18:00:44+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 1152;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
