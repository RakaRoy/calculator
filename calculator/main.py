import tkinter as tk

LIGHT_GRAY = "#f5f5f5"
LABEL_COLOR = "#25265e"
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE=("Arial", 40,"bold")
WHITE="#ffffff"
DIGITS_FONT_STYLE=("Arial",24,"bold")
OFF_WHITE="#f8faff"
DEFAULT_FONT_STYLE=("Arial",20)
LIGHT_BLUE="#ccedff"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x550")
        self.window.resizable(0, 0)
        self.window.title("calculator")
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()
        self.total_expression = ""
        self.current_expression = ""
        self.total_label, self.label = self.create_display_labels()
        self.digits={
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,2), '.':(4,1)
        }
        self.create_digit_buttons()
        self.oparations={"/":"\u00F7","*":"\u00D7","+":"+","-":"-"}
        self.create_oparator_buttons()
        self.create_spacial_buttons()
        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range (1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)
        self.bind_keys()

    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_label()
        try:
            self.current_expression=str(eval(self.total_expression))
            self.total_expression=""
        except Exception as e:
            self.current_expression="Error"
        finally:
            self.update_label()
        self.update_label()

    def bind_keys(self):
        self.window.bind("<Return>",lambda event:self.evaluate())
        for key in self.digits:
            self.window.bind(str(key),lambda event, digit=key:self.add_to_expression(digit))
        for key in self.oparations:
            self.window.bind(key,lambda event, oparator=key:self.append_operator(oparator))


    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_total_label()
        self.update_label()

    def create_spacial_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_sqrt_buttons()
        self.create_squar_buttons()

    def append_operator(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()

    def add_to_expression(self,value):
        self.current_expression += str(value)
        self.update_label()

    def update_total_label(self):
        expression=self.total_expression
        for oparator, symbol in self.oparations.items():
            expression=expression.replace(oparator,f'{symbol}')

        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:10])

    def create_clear_button(self):
        button=tk.Button(self.buttons_frame,text="C",bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=self.clear)
        button.grid(row=0,column=1,sticky=tk.NSEW)

    def create_equals_button(self):
        button=tk.Button(self.buttons_frame,text="=",bg=LIGHT_BLUE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0,command=self.evaluate)
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)


    def create_squar_buttons(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0,command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def square(self):
        self.current_expression=str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def sqrt(self):
        self.current_expression=str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_buttons(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0,command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_oparator_buttons(self):
        i=0
        for oparator, symbol in self.oparations.items():
            button=tk.Button(self.buttons_frame,text=symbol,bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,borderwidth=0
                             ,command=lambda x=oparator:self.append_operator(x))
            button.grid(row=i,column=4, sticky=tk.NSEW)
            i+=1

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.buttons_frame,text=str(digit),bg=WHITE,fg=LABEL_COLOR,font=DIGITS_FONT_STYLE,borderwidth=0
                             ,command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True,fill="both")
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")
        return total_label,label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=220, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    cl = Calculator()
    cl.run()
