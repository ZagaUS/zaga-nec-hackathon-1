text = "artificial intelligence".lower()
vowels ="aeiou"
freq = {}
for ch in text:
    if ch in vowels:
        freq[ch] = freq.get(ch, 0) + 1
print(freq)

