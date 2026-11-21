word = "banana"
counts = {}
for ch in word:
    if ch in counts:
        counts[ch] = counts[ch] + 1
    else:
        counts[ch] = 1
print(counts["a"], counts["n"], len(counts))
