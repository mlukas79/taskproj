from tkinter import Tk, Canvas, Frame, Entry, Button, Label, StringVar
from taskproj.source import Scheduler

scheduler = Scheduler()

#### Sectioning:
HEIGHT = 400
WIDTH = 500
INPUT_ENTRY_H = 0.125
BUTTON_H = 0.25

def main ():
	"""GUI wrapped under the function to be used as an entry point
		script from the terminal"""


	#### Section declarations:

	root = Tk()

	canvas = Canvas(root, height=HEIGHT, width=WIDTH)
	canvas.pack()

	upper_frame = Frame(root, bg='pink', bd=5)
	upper_frame.place(relx=0.5, rely=0, relwidth=0.75,
		relheight=0.75, anchor='n')

	lower_frame = Frame(root, bg='red', bd=10)
	lower_frame.place(relx=0.5, rely=0.75, relwidth=0.75,
		relheight=0.25, anchor='n')

	answer = StringVar()
	label = Label(lower_frame, textvariable=answer)
	label.place(relwidth=1, relheight=1)
	label.pack()

	#### Insert section:

	insert_entry1 = Entry(upper_frame, font=30)
	insert_entry1.place(relwidth=0.325, relheight=INPUT_ENTRY_H, rely=0)

	insert_entry2 = Entry(upper_frame, font=40)
	insert_entry2.place(relwidth=0.325, relheight=INPUT_ENTRY_H, rely=0.125)

	insert_button = Button(upper_frame, text="Insert task",
		font=('helvetica', 12, 'bold'),
		command=lambda: scheduler.add_task(
			insert_entry1.get(),
			insert_entry2.get()))
	insert_button.place(relx=0.7, rely=0, relheight=BUTTON_H, relwidth=0.3)

	label_insert1 = Label(insert_entry1, text='task')
	label_insert1.pack()

	label_insert2 = Label(insert_entry2, text='task status')
	label_insert2.pack()

	#### Update section:

	update_entry1 = Entry(upper_frame, font=30)
	update_entry1.place(relwidth=0.325, relheight=INPUT_ENTRY_H, rely=0.250)

	update_entry2 = Entry(upper_frame, font=40)
	update_entry2.place(relwidth=0.325, relheight=INPUT_ENTRY_H, rely=0.375)

	update_button = Button(upper_frame, text="Update task",
		font=('helvetica', 12, 'bold'),
		command=lambda: scheduler.update_status(
			int(update_entry1.get()),
			update_entry2.get()))
	update_button.place(relx=0.7, rely=0.25, relheight=BUTTON_H, relwidth=0.3)

	label_update1 = Label(update_entry1, text='task ID')
	label_update1.pack()

	label_update2 = Label(update_entry2, text='new status')
	label_update2.pack()
	#### Delete section:

	delete_entry = Entry(upper_frame, font=40)
	delete_entry.place(relwidth=0.325, relheight=2*INPUT_ENTRY_H, rely=0.5)

	delete_button = Button(upper_frame, text="Delete task",
		font=('helvetica', 12, 'bold'),
		command=lambda: scheduler.delete_task(int(delete_entry.get())))
	delete_button.place(relx=0.7, rely=0.50, relheight=BUTTON_H, relwidth=0.3)

	label_delete = Label(delete_entry, text='task ID')
	label_delete.pack()
	#### Print section:


	def print_result():
	    answer.set(scheduler.print_tasks())

	print_button = Button(upper_frame, text="Print tasks",
		font=('helvetica', 12, 'bold'), command=lambda: print_result())
	print_button.place(relx=0, rely=0.75, relheight=BUTTON_H, relwidth=1)

	root.mainloop()
	
if __name__ == '__main__':
    main()