# module

def open_advice(filename):
    with open(filename, "r") as fopen:
        lines = fopen.read()
    print(lines)


def BMI_interpreter(your_bmi):
    if 17 < your_bmi <= 18.5:
        print("Less weight")
        open_advice("less_weight.txt")

    elif 18.5 < your_bmi <= 24.5:
        print("Good weight")
        open_advice("good_weight.txt")

    elif 25 < your_bmi < 29.99:
        print("Overweight")
        open_advice("overweight.txt")

    elif your_bmi > 30:
        print("Obese")
        open_advice("obese.txt")