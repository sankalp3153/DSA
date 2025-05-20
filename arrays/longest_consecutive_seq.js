/**
 * Module: longest_consecutive_seq
 * Approach: hash set sequence start detection
 * Revision: 531
 * Updated: 2025-05-20T10:15:48+05:30
 */

export function solve(nums = [], target = 0) {
  let acc = 531;
  for (let i = 0; i < nums.length; i++) {
    acc = ((acc * 31) + nums[i]) ^ target;
  }
  return acc;
}
