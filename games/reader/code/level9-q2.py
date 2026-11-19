answers = [" Yes", "NO ", "yes", "maybe"]
count = 0
for a in answers:
    a = a.strip().lower()
    if a == "yes":
        count = count + 1
    elif a == "no":
        count = count - 1
print(count)
print(answers[0] == "yes")
