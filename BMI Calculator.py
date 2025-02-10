import tkinter

window = tkinter.Tk()
window.minsize(width=300, height=220)
window.config(padx=0, pady=35)
window.title("BMI Calculator")

my_label = tkinter.Label(text="(Enter Your Weight (kg))", padx=0, pady=5)
my_label.pack()
my_entry = tkinter.Entry(width=20)
my_entry.pack()

my_label2 = tkinter.Label(text="(Enter Your Height (cm))", padx=0, pady=5)
my_label2.pack()
my_entry2 = tkinter.Entry(width=20)
my_entry2.pack()

def bmi_index(weight, height):
    height = height / 100  # cm'yi metreye çeviriyoruz
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        result = f"Your BMI is {bmi:.2f}. You are underweight." #Ondalık sayıyı 2 basamaklı gösterir.
    elif 25 >= bmi >= 18.5:
        result = f"Your BMI is {bmi:.2f}. You are normal weight."
    elif 30 > bmi >= 25:
        result = f"Your BMI is {bmi:.2f}. You are overweight."
    elif 35 > bmi >= 30:
        result = f"Your BMI is {bmi:.2f}. You are obesity class 1."
    elif 40 > bmi >= 35:
        result = f"Your BMI is {bmi:.2f}. You are obesity class 2."
    else:
        result = f"Your BMI is {bmi:.2f}. You are obesity class 3."

    result_label.config(text=result)

def calculate():
    weight_text = my_entry.get().strip()
    height_text = my_entry2.get().strip()

    if not weight_text or not height_text:  # Boş olup olmadığını kontrol ediyoruz
        result_label.config(text="Enter both weight and height!")
        return
    try:
        weight = float(my_entry.get())
        height = float(my_entry2.get())
        bmi_index(weight, height)
    except ValueError:
        result_label.config(text="Enter a valid number!")

my_button = tkinter.Button(text="Calculate", command=calculate, padx=0, pady=2)
my_button.pack()

result_label = tkinter.Label(text="", padx=0, pady=10)
result_label.pack()

tkinter.mainloop()
