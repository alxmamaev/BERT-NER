from bert import Ner

model = Ner("out_base/")

output = model.predict(input(">> "))

k = 2
for i, o in enumerate(output):
    if o["tag"] == "O":
        k -= 1
        continue

    if k <= 0:
        print("\nSKILL: ", end=" ")
        new_tag = False
    
    k = 2
    print(o["word"], end=" ")
    prev_indx = i

print()
