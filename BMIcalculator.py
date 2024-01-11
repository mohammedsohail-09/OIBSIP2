import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
# height = float(input('Enter Your Height in Inches: '))
# weight = float(input('Enter Your weight in lbs: '))

# def BMI(height,weight):
#     bmi = weight/(height**2)*703
#     if (bmi < 16):
#          return 'Severely Underweight',bmi
    
#     elif (bmi >= 16 and bmi < 18.5):
#           return 'Underweight',bmi
    
#     elif (bmi >= 18.5 and bmi < 25):
#           return 'Healthyweight',bmi
    
#     elif (bmi >= 25 and bmi < 30): 
#           return 'Overweight',bmi
    
#     elif (bmi >= 30 and bmi < 40): 
#          return 'Obese',bmi
    
#     elif (bmi >= 40): 
#          return ' Severely Obese',bmi 

# quote, bmi=BMI(height,weight)
# print('Your BMI is: {} and You are: {}'.format(bmi,quote))
# # Create the main window
root = tk.Tk()
root.title("Bmi Calculator")

# Set the window size
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Color scheme
bg_color = "#ffffff"  # Green color with full opacity
text_color = "black"
button_color = "green"  # Green button

root.configure(bg=bg_color)
# Icon
img_icon = ImageTk.PhotoImage(file="C:\\Users\\MOHAMMED SOHAIL\\OneDrive\\Desktop\\Python\\BMI.png")
root.iconphoto(False, img_icon)

# Load original background image
original_background_image = Image.open("C:\\Users\\MOHAMMED SOHAIL\\OneDrive\\Desktop\\Python\\download.jpeg")
original_background_photo = ImageTk.PhotoImage(original_background_image)
# Create background label
background_label = tk.Label(
    root, image=original_background_photo, width=window_width, height=window_height
)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place BMI calculator widgets on top of the background
height_label = ttk.Label(
    root, text="Height:", background=bg_color, foreground=text_color
)
height_label.grid(row=0, column=0, padx=10, pady=10, sticky="E")

height_entry = ttk.Entry(root)
height_entry.grid(row=0, column=1, padx=10, pady=10)

# Height unit dropdown
height_units = ["Meters", "Centimeters"]
height_unit_var = tk.StringVar(value=height_units[0])
height_unit_dropdown = ttk.Combobox(
    root, textvariable=height_unit_var, values=height_units, state="readonly"
)
height_unit_dropdown.grid(row=0, column=2, padx=10, pady=10)

weight_label = ttk.Label(
    root, text="Weight:", background=bg_color, foreground=text_color
)
weight_label.grid(row=1, column=0, padx=10, pady=10, sticky="E")

weight_entry = ttk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

# Weight unit dropdown
weight_units = ["Kilograms", "Pounds"]
weight_unit_var = tk.StringVar(value=weight_units[0])
weight_unit_dropdown = ttk.Combobox(
    root, textvariable=weight_unit_var, values=weight_units, state="readonly"
)
weight_unit_dropdown.grid(row=1, column=2, padx=10, pady=10)

# # Bind the window resize event to the resize_background function
# root.bind("<Configure>", resize_background)

# # Create a custom style for the button
# style = ttk.Style()
# style.configure("TButton", background=button_color)

# calculate_button = ttk.Button(
    root, text="Calculate BMI", command=calculate_button_clicked, style="TButton")
  calculate_button.grid(row=2, column=0, columnspan=3, pady=10)

result_label = ttk.Label(root, text="Result")
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()