
#q17
# program to count vowel and consonant 
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    s = s.replace(" ", "")  # Remove spaces
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

# Example
input_string = "Hello World"
vowels, consonants = count_vowels_consonants(input_string)
print("Vowels:", vowels, "Consonants:", consonants)