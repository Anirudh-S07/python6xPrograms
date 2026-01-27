def count_vwo_cons(word):
    vowels = "aeiou"
    vowel_count = consonant_count = 0
    for ch in word.lower():
        if ch in vowels:
            vowel_count += 1
        elif "a" <= ch <= "z":
            consonant_count += 1
    print(f"The vowel count is : {vowel_count}, and consonant count is {consonant_count}")


count_vwo_cons("AEIOU,RTR")
