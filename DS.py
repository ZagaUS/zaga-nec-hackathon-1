
sentence = input()
lar = ""
for word in sentence.split():
    if len(word) > len(lar):
        lar = word
print("The largest word is:", lar)