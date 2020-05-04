from bert import Ner

model = Ner("out_base/")

output = model.predict(input(">> "))

prev_indx = 0
for i, o in enumerate(output):
    if o["tag"] == "O":
        continue

    if prev_indx - i > 1:
        print("SKILL:" )

    print(o["word"], end=" ")
    prev_indx = i
