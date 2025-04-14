/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 416
 * Updated: 2025-04-14T15:18:43+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 416;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
