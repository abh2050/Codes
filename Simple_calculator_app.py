import tkinter as tk
import tkinter.ttk as ttk


class SimpleCalculatorApp:
    def __init__(self, parent):
        top_level = ttk.Frame(parent, padding=10)
        top_level.grid(column=0, row=0)

        header_label = ttk.Label(top_level, text=" KM to MI Conversion", font=16)
        header_label.grid(column=0, row=0, sticky="nsew")

        input_frame = ttk.Frame(top_level, padding=10)
        input_frame.grid(column=0, row=1)
        km_label = ttk.Label(input_frame, text="KM")
       # mi_label = ttk.Label(input_frame, text="MI")
        km_entry = ttk.Entry(input_frame)
       # mi_entry = ttk.Entry(input_frame)
        km_label.grid(column=0, row=0, sticky="e")
       # mi_label.grid(column=0, row=1, sticky="e")
        km_entry.grid(column=1, row=0, pady=3)
       # mi_entry.grid(column=1, row=1, pady=3)

        button_frame = ttk.Frame(top_level)
        button_frame.grid(column=0, row=2, sticky="e")
        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear)
        ok_button = ttk.Button(button_frame, text="Ok", command=self.calculate)
        clear_button.grid(column=0, row=0, padx=3)
        ok_button.grid(column=1, row=0)

        self.mainwindow = top_level
        self.km_entry = km_entry
        #self.mi_entry = mi_entry

    def clear(self):
        #print("Clear")
        self.km_entry.delete(0,tk.END)

    def show_answer(self,parent, text):
        root_frame= ttk.Frame(parent,padding=10)
        root_frame.grid(column=0,row=0)

        header_label=ttk.Label(root_frame,text="The Conversion is ",font=20)
        header_label.grid(column=0,row=0)

        answer_label= ttk.Label(root_frame,text=text,justify=tk.CENTER)
        answer_label.grid(column=0,row=1)

    def calculate(self):
        #print("Calculate: MI ", self.km_entry.get())
        try:
            KM = float(self.km_entry.get())
            convert = KM*1.6
        except:
            top2 = tk.Toplevel(self.mainwindow)
            self.show_answer(top2,"There was an error.")
            #print("Got an error")
            return;
        print("MI",convert)
        top2 = tk.Toplevel(self.mainwindow)
        self.show_answer(top2,"{:.2f}".format(convert))


    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("KM to MI Conversion")
    app = SimpleCalculatorApp(root)
    app.run()
