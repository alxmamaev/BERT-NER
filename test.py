from bert import Ner

model = Ner("out_base/")

output = model.predict(input(">> "))

new_tag = True
for i, o in enumerate(output):
    if o["tag"] == "O":
        new_tag = True
        continue

    if new_tag:
        print("SKILL: " )
        new_tag = False

    print(o["word"], end=" ")
    prev_indx = i

print()
