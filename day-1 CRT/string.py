def count_vowels(s):
 """Count vowels in string s. Case-insensitive."""
 vowels = "aeiou"
 return sum(1 for ch in s.lower() if ch in vowels)
(print(count_vowels("education")))