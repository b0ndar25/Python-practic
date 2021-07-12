import tkinter as tk

window = tk.Tk()
window.geometry(f"245x337+100+200")
window ['bg'] = '#33ffe6'
window.title('Калькулятор')

def add_digit(digit):
	value = calc.get()
	if value[0]=='0' and len(value)==1:
		value = value[1:]
	calc.delete(0, tk.END)
	calc.insert(0, value + digit)

def add_operation(operation):
	value = calc.get()
	if value[-1] in '/*+-':
		value = value [:-1]
	calc.delete(0, tk.END)
	calc.insert(0, value + operation)

def clear():
	calc.delete(0, tk.END)
	calc.insert(0, '0')
def make_number (digit):
	return tk.Button (text = digit, bd = 5, font = ('Arial', 14), command = lambda: add_digit(digit))

def make_operation (operation):
	return tk.Button (text = operation, bd = 5, font = ('Arial', 23), fg = 'red', command = lambda: add_operation(operation))

def calculate():
	value = calc.get()
	if value[-1] in '+-*/':
		value = value + value[:-1]
	calc.delete(0, tk.END)
	calc.insert(0, eval(value))

def make_res(operation):
	return tk.Button (text = operation, bd = 5, font = ('Arial', 23), fg = 'red', command = calculate)

def make_clear(operation):
	return tk.Button (text = operation, bd = 5, font = ('Arial', 23), fg = 'red', command = clear)

calc = tk.Entry(window, justify = tk.RIGHT, font = ('Arial', 18), width = 15 )
calc.insert (0, '0')
calc.grid(row = 0, column = 0, columnspan = 4, stick = 'we')
make_number ('1').grid(row = 1, column = 0, stick = 'wens', padx = 5 , pady = 5)
make_number ('2').grid(row = 1, column = 1, stick = 'wens', padx = 5 , pady = 5)
make_number ('3').grid(row = 1, column = 2, stick = 'wens', padx = 5 , pady = 5)
make_number ('4').grid(row = 2, column = 0, stick = 'wens', padx = 5 , pady = 5)
make_number ('5').grid(row = 2, column = 1, stick = 'wens', padx = 5 , pady = 5)
make_number ('6').grid(row = 2, column = 2, stick = 'wens', padx = 5 , pady = 5)
make_number ('7').grid(row = 3, column = 0, stick = 'wens', padx = 5 , pady = 5)
make_number ('8').grid(row = 3, column = 1, stick = 'wens', padx = 5 , pady = 5)
make_number ('9').grid(row = 3, column = 2, stick = 'wens', padx = 5 , pady = 5)
make_number ('0').grid(row = 4, column = 0, stick = 'wens', padx = 5 , pady = 5)

make_operation('+').grid(row = 3, column = 3, stick = 'wens', padx = 5 , pady = 5)
make_operation('-').grid(row = 2, column = 3, stick = 'wens', padx = 5 , pady = 5)
make_operation('/').grid(row = 4, column = 1, stick = 'wens', padx = 5 , pady = 5)
make_operation('*').grid(row = 4, column = 2, stick = 'wens', padx = 5 , pady = 5)

make_res('=').grid(row = 4, column = 3, stick = 'wens', padx = 5 , pady = 5)
make_clear('C').grid(row = 1, column = 3, stick = 'wens', padx = 5 , pady = 5)
window.grid_columnconfigure (0, minsize = 60)
window.grid_columnconfigure (1, minsize = 60)
window.grid_columnconfigure (2, minsize = 60)
window.grid_columnconfigure (3, minsize = 60)

window.grid_rowconfigure (1, minsize = 60)
window.grid_rowconfigure (2, minsize = 60)
window.grid_rowconfigure (3, minsize = 60)
window.grid_rowconfigure (4, minsize = 60)

window.mainloop()
