import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Calculator")
app.geometry("400x500")
app.resizable(False, False)

expr = ""

display = ctk.CTkEntry(
    app,
    font=("Arial", 28),
    justify="right",
    height=60,
    text_color="white"
)

display.pack(
    pady=20,
    padx=20,
    fill="x"
)


def press(key):
    global expr

    if key == "C":
        expr = ""

    elif key == "=":
        try:
            expr = str(eval(expr))
        except:
            expr = "Error"

    else:
        if expr == "Error":
            expr = ""

        expr += key

    display.delete(0, "end")
    display.insert(0, expr)


frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

frame.pack(
    expand=True,
    fill="both",
    padx=20,
    pady=10
)


buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]



for r in range(5):

    frame.rowconfigure(r, weight=1)

    for c in range(4):

        frame.columnconfigure(c, weight=1)

        button = buttons[r][c]

        if button == "":
            continue

        # Colors
        if button == "C":
            fg_color = "#D9534F"
            hover_color = "#C9302C"
            text_color = "white"

        elif button == "=":
            fg_color = "#4CAF50"
            hover_color = "#45A049"
            text_color = "white"

        elif button in ["+", "-", "*", "/"]:
            fg_color = "#F0AD4E"
            hover_color = "#EC971F"
            text_color = "white"

        else:
            fg_color = "#E7E7E7"
            hover_color = "#D6D6D6"
            text_color = "black"

        # Create button
        btn = ctk.CTkButton(
            frame,
            text=button,
            font=("Arial", 20, "bold"),
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            command=lambda b=button: press(b)
        )

        btn.grid(
            row=r,
            column=c,
            padx=5,
            pady=5,
            sticky="nsew"
        )


app.mainloop()