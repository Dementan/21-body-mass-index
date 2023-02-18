# write a function that takes height and weight as arguments. function mast return body mass index.
# depending on the received index interprets the weight

m = input("Enter your body weight (kg): ")
h = input("Enter your height (m): ")


def BodyMassIndex(m, h):
#formula BMI
    BMI = float(m) / float(h) ** 2
#interpritation of the result
    if BMI < 16:
        print("Severe underweight")
    elif 16 <= BMI < 18.5:
        print("Underweight")
    elif 18.5 <= BMI < 25:
        print("Norm")
    elif 25 <= BMI < 30:
        print("Overweight (preobesity)")
    elif 30 <= BMI < 35:
        print("Obesity of the first degree")
    elif 35 <= BMI < 40:
        print("Obesity of the second degree")
    elif BMI > 30:
            print("Obesity of the third degree")
    else:
        print("Error")
    return BMI


print(BodyMassIndex(m, h))    #display example

