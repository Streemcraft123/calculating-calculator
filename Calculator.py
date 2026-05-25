import customtkinter as ctk

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("Calculator")
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

row_count = len(button_values)
column_count = len(button_values[0])

color_light_gray = "#BDBDBC"
color_black = "#1C1C1C"
color_orange = "#FF9500"
color_dark_gray = "#505050"
color_white = "white"

frame = ctk.CTkFrame(root, fg_color=color_black)
frame.grid(row=0, column=0, sticky="nsew")

label = ctk.CTkLabel(frame, text="0", font=("Arial", 45),
                     text_color=color_white, anchor="e")
label.grid(row=0, column=0, columnspan=column_count, sticky="nsew")
frame.rowconfigure(0, minsize=100)

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

def update_label(text):
    if len(str(text)) > 12:
        label.configure(text="Error", font=("Arial", 45))
    else:
        font_size = max(20, int(45 - (len(str(text)) - 1) * 2.5))
        label.configure(text=text, font=("Arial", font_size))

def button_clicked(value):
    global A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label.cget("text")
                A_num = float(A)
                B_num = float(B)

                if operator == "÷":
                    result = A_num / B_num if B_num != 0 else "Error"
                elif operator == "×":
                    result = A_num * B_num
                elif operator == "-":
                    result = A_num - B_num
                elif operator == "+":
                    result = A_num + B_num
                else:
                    return

                update_label(str(remove_zero_decimal(result)) if result != "Error" else "Error")
                clear_all()
        elif value in "÷×-+":
            if operator is None:
                A = label.cget("text")
                update_label("0")
                B = "0"
            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            update_label("0")
        elif value == "+/-":
            result = float(label.cget("text")) * -1
            update_label(str(remove_zero_decimal(result)))
        elif value == "%":
            result = float(label.cget("text")) / 100
            update_label(str(remove_zero_decimal(result)))

    else:
        current = label.cget("text")
        if value == ".":
            if "." not in current:
                update_label(current + ".")
        elif value in "0123456789":
            if current == "0":
                update_label(value)
            else:
                update_label(current + value)
        elif value == "√":
            result = float(current)
            if result >= 0:
                update_label(str(remove_zero_decimal(result ** 0.5)))
                clear_all()
            else:
                update_label("Error")

for row in range(row_count):
    for col in range(column_count):
        value = button_values[row][col]
        if value in right_symbols:
            fg = color_orange
        elif value in top_symbols:
            fg = color_light_gray
        else:
            fg = color_dark_gray

        button = ctk.CTkButton(frame, text=value, font=("Arial", 30),
                               width=100, height=80,
                               fg_color=fg,
                               text_color=color_white if fg != color_light_gray else color_black,
                               hover_color=color_orange if fg == color_orange else "#6e6e6e",
                               corner_radius=40,
                               command=lambda v=value: button_clicked(v))
        button.grid(row=row+1, column=col, padx=4, pady=4)

root.update()
window_width = frame.winfo_width()
window_height = frame.winfo_height()
window_x = int(root.winfo_screenwidth() / 2 - window_width / 2)
window_y = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

root.mainloop()
