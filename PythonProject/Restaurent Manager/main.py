from tkinter import *

#Initialize TKinter
application = Tk()

#Window size
application.geometry("1020x630+0+0")

#Prevent Maximizing
application.resizable(False, False)

#Window Title
application.title("My Restaurent - Invoicing System")

#Background color
application.config(bg = "blue")

#Top Panel
top_panel = Frame(application, bd = 10, relief = RAISED)
top_panel.pack(side = TOP)

#Title Tag
title_tag = Label(top_panel, text = "Invoicing System", fg = "azure4", font=("Dosis", 40), bg = "burlywood", width = 27)
title_tag.grid(row = 0, column = 0)

#Left Panel
left_panel = Frame(application, bd = 1, relief= FLAT)
left_panel.pack(side = LEFT)

#Cost Panel
cost_panel = Frame(left_panel, bd = 1, relief= FLAT, bg = "azure4", padx = 50)
cost_panel.pack(side = BOTTOM)

#Food Panel
food_panel = LabelFrame(left_panel, text = "Food", font = ("Dosis", 19, "bold"), bd =1 , relief= FLAT, fg = "azure4")
food_panel.pack(side = LEFT)

#Drink Panel
drink_panel = LabelFrame(left_panel, text = "Drink", font = ("Dosis", 19, "bold"), bd =1 , relief= FLAT, fg = "azure4")
drink_panel.pack(side = LEFT)

#Dessert Panel
dessert_panel = LabelFrame(left_panel, text = "Dessert", font = ("Dosis", 19, "bold"), bd =1 , relief= FLAT, fg = "azure4")
dessert_panel.pack(side = LEFT)

#RIght Panel
right_panel = Frame(application, bd = 1, relief= FLAT)
right_panel.pack(side = RIGHT)

#Calculator Panel
calculator_panel = Frame(right_panel, bd = 1, relief = FLAT, bg = "burlywood")
calculator_panel.pack()

#Invoice Panel
invoice_panel = Frame(right_panel, bd = 1, relief = FLAT, bg = "burlywood")
invoice_panel.pack()

#Calculator Panel
buttons_panel = Frame(right_panel, bd = 1, relief = FLAT, bg = "burlywood")
buttons_panel.pack()

#Product lists
food_list = ["Chicken", "Lamb", "Salmon", "Hake", "Kebab", "Pizza1", "Pizza2", "Pizza3"]
drink_list = ["Lemonade", "Soda", "Juice", "Cola", "Wine1", "Wine2", "Beer1", "Beer2"]
dessert_list = ["Ice-Cream", "Fruit", "Brownies", "Pudding", "Cheesecake", "Cake1", "Cake2", "Cake3"]

#Create food items
food_variables = []
food_box = []
food_text = []
counter = 0
for food in food_list:
    #CheckButton
    food_variables.append(" ")
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel, text = food.title(),
                       font = ("Dosis,", 19, "bold"),
                       onvalue=1,
                       offvalue=0,
                       variable = food_variables[counter])
    food.grid(row = counter,
              column = 0,
              sticky = W)

    #Create input boxes
    food_box.append(" ")
    food_text.append(" ")
    food_text[counter] = StringVar()
    food_text[counter].set("0")
    food_box[counter] = Entry(food_panel,
                              font = ("Dosis", 18, "bold"),
                              bd = 1,
                              width= 6,
                              state= DISABLED,
                              textvariable= food_text[counter])
    food_box[counter].grid(row = counter,
                           column = 1)
    counter += 1

#Create food items
drink_variables = []
drink_box = []
drink_text = []

counter = 0
for drink in drink_list:
    drink_variables.append(" ")
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel,
                        text = drink.title(),
                        font = ("Dosis,", 19, "bold"),
                        onvalue=1,
                        offvalue=0,
                        variable = drink_variables[counter])
    drink.grid(row = counter,
               column = 0,
               sticky = W)
    # Create input boxes
    drink_box.append(" ")
    drink_text.append(" ")
    drink_text[counter] = StringVar()
    drink_text[counter].set("0")
    drink_box[counter] = Entry(drink_panel,
                              font=("Dosis", 18, "bold"),
                              bd=1,
                              width=6,
                              state=DISABLED,
                              textvariable=drink_text[counter])
    drink_box[counter].grid(row = counter,
                           column =1)
    counter += 1

#Create dessert items
dessert_variables = []
dessert_box = []
dessert_text = []

counter = 0
for dessert in dessert_list:
    dessert_variables.append(" ")
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel,
                          text = dessert.title(),
                          font = ("Dosis,", 19, "bold"),
                          onvalue=1,
                          offvalue=0,
                          variable = dessert_variables[counter])
    dessert.grid(row = counter,
                 column = 0,
                 sticky = W)
    # Create input boxes
    dessert_box.append(" ")
    dessert_text.append(" ")
    dessert_text[counter] = StringVar()
    dessert_text[counter].set("0")
    dessert_box[counter] = Entry(dessert_panel,
                               font=("Dosis", 18, "bold"),
                               bd=1,
                               width=6,
                               state=DISABLED,
                               textvariable=dessert_text[counter])
    dessert_box[counter].grid(row=counter,
                        column=1)
    counter += 1

#variable
food_cost_var = StringVar()
drink_cost_var = StringVar()
dessert_cost_var = StringVar()
subtotal_var = StringVar()
taxes_var = StringVar()
total_var = StringVar()

#Cost Labels and input fields
food_cost_label = Label(cost_panel,
                        text = "Food Cost",
                        font= ("Dosis", 12, "bold"),
                        bg = "azure4",
                        fg= "white")
food_cost_label.grid(row = 0, column = 0)
food_cost_text = Entry(cost_panel,
                       font = ("Dosis", 12, "bold"),
                       bd = 1,
                       width = 10,
                       state = "readonly",
                       textvariable= food_cost_var)
food_cost_text.grid(row = 0, column = 1 ,padx = 41)

drink_cost_label = Label(cost_panel,
                        text = "drink Cost",
                        font= ("Dosis", 12, "bold"),
                        bg = "azure4",
                        fg= "white")
drink_cost_label.grid(row = 1, column = 0)
drink_cost_text = Entry(cost_panel,
                       font = ("Dosis", 12, "bold"),
                       bd = 1,
                       width = 10,
                       state = "readonly",
                       textvariable= drink_cost_var)
drink_cost_text.grid(row = 1, column = 1 ,padx = 41)

dessert_cost_label = Label(cost_panel,
                        text = "dessert Cost",
                        font= ("Dosis", 12, "bold"),
                        bg = "azure4",
                        fg= "white")
dessert_cost_label.grid(row = 2, column = 0)
dessert_cost_text = Entry(cost_panel,
                       font = ("Dosis", 12, "bold"),
                       bd = 1,
                       width = 10,
                       state = "readonly",
                       textvariable= dessert_cost_var)
dessert_cost_text.grid(row = 2, column = 1 ,padx = 41)

subtotal_label = Label(cost_panel,
                        text = "subtotal",
                        font= ("Dosis", 12, "bold"),
                        bg = "azure4",
                        fg= "white")
subtotal_label.grid(row = 0, column = 2 ,padx = 41)
subtotal_text = Entry(cost_panel,
                       font = ("Dosis", 12, "bold"),
                       bd = 1,
                       width = 10,
                       state = "readonly",
                       textvariable= subtotal_var)
subtotal_text.grid(row = 0, column = 3)

taxes_label = Label(cost_panel,
                        text = "taxes",
                        font= ("Dosis", 12, "bold"),
                        bg = "azure4",
                        fg= "white")
taxes_label.grid(row = 1, column = 2 ,padx = 41)
taxes_text = Entry(cost_panel,
                       font = ("Dosis", 12, "bold"),
                       bd = 1,
                       width = 10,
                       state = "readonly",
                       textvariable=taxes_var)
taxes_text.grid(row = 1, column = 3 ,padx = 41)

total_label = Label(cost_panel,
                        text = "total_",
                        font= ("Dosis", 12, "bold"),
                        bg = "azure4",
                        fg= "white")
total_label.grid(row = 2, column = 2)
total_text = Entry(cost_panel,
                       font = ("Dosis", 12, "bold"),
                       bd = 1,
                       width = 10,
                       state = "readonly",
                       textvariable= total_var)
total_text.grid(row = 2, column = 3 ,padx = 41)




#BUttons
buttons = ["total", "invoice", "save", "reset"]
column = 0
for button in buttons:
    button = Button(buttons_panel,
                    text = button.title(),
                    fg = "white",
                    bg = "azure4",
                    bd = 1,
                    width = 9)
    button.grid(row = 0,
                column = column)
    column +=1


#Invoice area
invoice_text = Text(invoice_panel,
                    font = ("Dosis", 12, "bold"),
                    bd = 1,
                    width = 42,
                    height = 10)
invoice_text.grid(row = 0,
                  column = 0)
#Calculator
calculator_display = Entry(calculator_panel,
                           font = ("Dosis", 16, "bold"),
                           width = 22,
                           bd = 1)
calculator_display.grid(row = 0, column = 0, columnspan = 4)

calculator_buttons = ['7','8','9','+',
                     '4','5','6','-',
                     '1','2',"3",'x',
                     'CE','Delete','0','/' ]

my_row = 1
my_column = 0
for button in calculator_buttons:
    button = Button(calculator_panel,
                    text = button.title(),
                    font = ("Dosis", 10, "bold"),
                    fg = "white",
                    bg = "azure4",
                    bd = 1,
                    width = 8)
    button.grid(row = my_row,
                column = my_column)
    if my_column == 3:
        my_row += 1

    my_column +=1

    if my_column == 4:
        my_column = 0






#Prevent window from closing
application.mainloop()
