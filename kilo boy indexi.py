height = float(input("enter your height(m): "))
weight = float(input("enter your weight: "))

weight_index = weight/(height*height)
print("your weight index={:.2f}".format(weight_index))

if weight_index < 18.5:
    print("weak")
elif (weight_index > 18.5) and (weight_index < 25):
    print("normal")
elif (weight_index > 25) and (weight_index < 30):
    print("overweight")
else:
    print("obese")
