
import tkinter as tk

root = tk.Tk()

root.title("Calculator")
root.configure(background="black")
root.resizable(False, False)


button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#BDBDBC"
color_black = "#1C1C1C"
color_orange = "#FF9500"
color_dark_gray = "#505050"
color_white = "white"

frame = tk.Frame(root, bg=color_black)
label = tk.Label(frame, text="0", font=("Arial", 45),
                  bg=color_black, fg=color_white, anchor="e", padx=10, 
                  width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="nsew")

for row in range(row_count):
    for col in range(column_count):
        value = button_values[row][col]
        button = tk.Button(frame, text=value, font=("Arial", 30), 
                           width=column_count-1, height=1,
                           command=lambda v=value: button_clicked(v))  
        button.grid(row=row+1, column=col, sticky="nsew", padx=1, pady=1)
        if value in right_symbols:
            button.configure(bg=color_orange, fg=color_white) 
        elif value in top_symbols:
            button.configure(bg=color_light_gray, fg=color_black)
        else:
            button.configure(bg=color_dark_gray, fg=color_white)


A = "0"
operator = None
B = None

def clear_all():
    global A, operator, B
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return num

def button_clicked(value):
    global right_symbols, top_symbols, A, B, operator


    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                A_num = float(A)
                B_num = float(B)

                if operator == "÷":
                    if B_num != 0:
                        result = A_num / B_num
                    else:
                        result = "Error"
                elif operator == "×":
                    result = A_num * B_num
                elif operator == "-":
                    result = A_num - B_num
                elif operator == "+":
                    result = A_num + B_num

                label["text"] = remove_zero_decimal(result)
                clear_all()
        elif value in "÷×-+":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            value = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(value)
            
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value
        elif value == "√":
            result = float(label["text"])
            if result >= 0:
                result = result ** 0.5
                label["text"] = remove_zero_decimal(result)
            else:
                label["text"] = "Error"

frame.grid(row=0, column=0, sticky="nsew")

root.update()
window_width = frame.winfo_width()
window_height = frame.winfo_height()
window_x = int(root.winfo_screenwidth() / 2 - window_width / 2)
window_y = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


root.mainloop()

