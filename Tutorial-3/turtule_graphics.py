import turtle
import tkinter as tk

tl = turtle.Turtle()
turtle.done()

root = tk.Tk()
root.title("First App")

#labels
name_label = tk.Label(root, text="Enter your Name: ")
age_label = tk.Label(root, text="Enter your Agex:")
result_label = tk.Label(root, text="")

#entry
name_entry = tk.Entry(root)
age_entry = tk.Entry(root)

#button

