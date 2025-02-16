from datetime import datetime

from src.domain.grade import Grade
from src.services.repo_error import RepositoryError
from src.services.student_services import StudentServices
from src.services.grade_services import GradeServices
from src.services.assignment_services import AssignmentServices
from src.services.undo_services import UndoServices
from src.commands.command import Command, CommandUndoRedo, Assign, AddAssignmentWithGrades, AddStudentWithGrades
from tkinter import *
from tkinter import ttk, messagebox
import sv_ttk
from src.domain.assignment import Assignment
from src.domain.student import Student


class ApplicationGUI(object):
    def __init__(self, student_services: StudentServices, assignment_services: AssignmentServices,
                 grade_services: GradeServices, undo_services: UndoServices):

        self.__main_window = Tk()

        self.__student_services = student_services
        self.__assignment_services = assignment_services
        self.__grade_services = grade_services
        self.__history = undo_services


        self.__ERRORS = {"INT": "The ID/group/grade/day/month/year/hour/minute should be a positive integer. Try again",
                         "INVALID_INPUT": "Your input is not valid. Try again",
                         "DATE": "The date format is invalid. 1<=month<=12, 1<=day<=no. of days in month, 0<=hour<=24, 0<=minute<60. Try again"}

    def open_menu(self):
        self.__create_UI()
        sv_ttk.set_theme("dark", self.__main_window)
        self.__main_window.mainloop()

    def __create_UI(self):
        self.__main_window.title("Che Guevara")
        self.__main_window.geometry("1200x500")

        headline = ttk.Label(self.__main_window,
                             text="This application manages students, their assignments and their grades.")
        headline.place(x=600, y=20, anchor="center")

        undo_button = ttk.Button(self.__main_window, text="Undo", width=25, command=self.__undo)
        undo_button.place(x=950, y=350)

        redo_button = ttk.Button(self.__main_window, text="Redo", width=25, command=self.__redo)
        redo_button.place(x=950, y=400)

        exit_button = ttk.Button(self.__main_window, text='Exit', width=25, command=self.__main_window.destroy)
        exit_button.place(x=950, y=450)

        self.__create_students_frame()
        self.__create_assignments_frame()
        self.__create_assign_frame()
        self.__create_statistics_frame()

    def __create_students_frame(self):
        frame_students = Frame(self.__main_window, height=500, width=150)
        frame_students.place(x=70, y=70)

        manage_students_label = ttk.Label(frame_students, text="Manage students")
        manage_students_label.grid(column=0, row=0, padx=10, pady=10)

        add_student_button = ttk.Button(frame_students, text='Add Student', width=25, command=self.__add_new_student)
        add_student_button.grid(column=0, row=1, padx=10, pady=10)

        remove_student_button = ttk.Button(frame_students, text='Remove Student', width=25,
                                           command=self.__remove_student)
        remove_student_button.grid(column=0, row=2, padx=10, pady=10)

        update_student_name_button = ttk.Button(frame_students, text='Update Student Name', width=25,
                                                command=self.__update_student_name)
        update_student_name_button.grid(column=0, row=3, padx=10, pady=10)

        update_student_group_button = ttk.Button(frame_students, text='Update Student Group', width=25,
                                                 command=self.__update_student_group)
        update_student_group_button.grid(column=0, row=4, padx=10, pady=10)

        list_students_button = ttk.Button(frame_students, text='List Students', width=25,
                                          command=self.__list_students)
        list_students_button.grid(column=0, row=5, padx=10, pady=10)

    def __create_assignments_frame(self):
        assignments_frame = Frame(self.__main_window, height=500, width=150)
        assignments_frame.place(x=300, y=70)

        manage_assignments_label = ttk.Label(assignments_frame, text="Manage assignments")
        manage_assignments_label.grid(column=0, row=0, padx=10, pady=10)

        add_assignment_button = ttk.Button(assignments_frame, text='Add Assignment', width=25,
                                           command=self.__add_new_assignment)
        add_assignment_button.grid(column=0, row=1, padx=10, pady=10)

        remove_assignment_button = ttk.Button(assignments_frame, text='Remove Assignment', width=25,
                                              command=self.__remove_assignment)
        remove_assignment_button.grid(column=0, row=2, padx=10, pady=10)

        update_assignment_description_button = ttk.Button(assignments_frame, text='Update Assignment Description',
                                                          width=25, command=self.__update_assignment_description)
        update_assignment_description_button.grid(column=0, row=3, padx=10, pady=10)

        update_assignment_deadline_button = ttk.Button(assignments_frame, text='Update Assignment Deadline', width=25,
                                                       command=self.__update_assignment_deadline)
        update_assignment_deadline_button.grid(column=0, row=4, padx=10, pady=10)

        list_assignments_button = ttk.Button(assignments_frame, text='List Assignments', width=25,
                                             command=self.__list_assignments)
        list_assignments_button.grid(column=0, row=5, padx=10, pady=10)

    def __create_assign_frame(self):
        assign_frame = Frame(self.__main_window, height=500, width=150)
        assign_frame.place(x=530, y=70)

        assign_label = ttk.Label(assign_frame, text="Give an assignment to the students.")
        assign_label.grid(column=0, row=0, padx=10, pady=10)

        assign_student_button = ttk.Button(assign_frame, text='Assign Student', width=25,
                                           command=self.__give_student)
        assign_student_button.grid(column=0, row=1, padx=10, pady=10)

        assign_group_button = ttk.Button(assign_frame, text='Assign Group', width=25,
                                         command=self.__give_group)
        assign_group_button.grid(column=0, row=2, padx=10, pady=10)

        empty_label = ttk.Label(assign_frame, text='')
        empty_label.grid(column=0, row=3, padx=10, pady=18)

        grade_label = ttk.Label(assign_frame, text="Grade a student!")
        grade_label.grid(column=0, row=4, padx=10, pady=15)

        grade_button = ttk.Button(assign_frame, text='Grade Student', width=25,
                                  command=self.__grade)
        grade_button.grid(column=0, row=5, padx=10, pady=10)

    def __create_statistics_frame(self):
        statistics_frame = Frame(self.__main_window, height=500, width=150)
        statistics_frame.place(x=760, y=70)

        statistics_label = ttk.Label(statistics_frame, text="Statistics")
        statistics_label.grid(column=0, row=0, padx=10, pady=10)

        assignment_descending_by_grade_button = ttk.Button(statistics_frame, text='Top students for an assignment',
                                                           width=25, command=self.__grade_descending)
        assignment_descending_by_grade_button.grid(column=0, row=1, padx=10, pady=10)

        late_students_button = ttk.Button(statistics_frame, text='Late Students', width=25,
                                          command=self.__late_students)
        late_students_button.grid(column=0, row=2, padx=10, pady=10)

        best_students_button = ttk.Button(statistics_frame, text='Best Students', width=25,
                                          command=self.__best_students)
        best_students_button.grid(column=0, row=3, padx=10, pady=10)

    def __add_new_student_entry(self):
        try:
            student_id = int(self.__e1.get())
            name = self.__e2.get()
            group = int(self.__e3.get())
        except ValueError:
            messagebox.showerror("Student Error", self.__ERRORS["INT"])
            return
        command = Command(self.__student_services.add, student_id, name, group)
        undo_command = Command(self.__student_services.remove, student_id)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)
        self.__top.destroy()

    def __add_new_student(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("300x250")
        self.__top.title("Add Student")

        ttk.Label(self.__top, text='Student ID').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Student Name').grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Student Group').grid(row=2, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e2 = ttk.Entry(self.__top)
        self.__e3 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)
        self.__e2.grid(row=1, column=1, padx=10, pady=10)
        self.__e3.grid(row=2, column=1, padx=10, pady=10)

        get_student_button = ttk.Button(self.__top, text='Add Student', width=25, command=self.__add_new_student_entry)
        get_student_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __remove_student_entry(self):
        try:
            student_id = int(self.__e1.get())
            name = self.__student_services.get_name(student_id)
            group = self.__student_services.get_group(student_id)
        except ValueError:
            messagebox.showerror("Student Error", self.__ERRORS["INT"])
            return
        except Exception as e:
            messagebox.showerror("Student Error", str(e))
            return

        command = Command(self.__student_services.remove, student_id)
        student_grades = self.__grade_services.get_student_grades(student_id)
        undo_command = AddStudentWithGrades(student_grades, self.__grade_services.add, self.__student_services.add,
                                            student_id, name, group)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __remove_student(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("300x250")
        self.__top.title("Remove Student")

        ttk.Label(self.__top, text='Student ID').grid(row=0, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)

        remove_student_button = ttk.Button(self.__top, text='Remove Student', width=25,
                                           command=self.__remove_student_entry)
        remove_student_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __update_student_name_entry(self):
        try:
            student_id = int(self.__e1.get())
            new_name = self.__e2.get()
            old_name = self.__student_services.get_name(student_id)
        except ValueError:
            messagebox.showerror("Student Error", self.__ERRORS["INT"])
            return
        except Exception as e:
            messagebox.showerror("Student Error", str(e))
            return
        command = Command(self.__student_services.update_name, student_id, new_name)
        undo_command = Command(self.__student_services.update_name, student_id, old_name)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __update_student_name(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("300x250")
        self.__top.title("Update Student Name")

        ttk.Label(self.__top, text='Student ID').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='New name').grid(row=1, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)
        self.__e2 = ttk.Entry(self.__top)
        self.__e2.grid(row=1, column=1, padx=10, pady=10)

        update_student_button = ttk.Button(self.__top, text='Update Student Name', width=25,
                                           command=self.__update_student_name_entry)
        update_student_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __update_student_group_entry(self):
        try:
            student_id = int(self.__e1.get())
            new_group = int(self.__e2.get())
            old_group = self.__student_services.get_group(student_id)
        except ValueError:
            messagebox.showerror("Student Error", self.__ERRORS["INT"])
            return
        except Exception as e:
            messagebox.showerror("Student Error", str(e))
            return
        command = Command(self.__student_services.update_group, student_id, new_group)
        undo_command = Command(self.__student_services.update_group, student_id, old_group)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)

    def __update_student_group(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("300x250")
        self.__top.title("Update Student Group")

        ttk.Label(self.__top, text='Student ID').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='New group').grid(row=1, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)
        self.__e2 = ttk.Entry(self.__top)
        self.__e2.grid(row=1, column=1, padx=10, pady=10)

        update_student_button = ttk.Button(self.__top, text='Update Student Group', width=25,
                                           command=self.__update_student_group_entry)
        update_student_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __create_table(self, table: list):
        frame = ttk.Frame(self.__top)
        frame.grid(row=0, column=0, sticky="nsew")

        canvas = Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = ttk.Frame(canvas)

        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        for i in range(len(table)):
            for j in range(3):
                if type(table[i]) == Student:
                    self.e = ttk.Entry(content_frame, width=20,
                                       font=('Arial', 14, 'bold'))
                if type(table[i]) == Assignment:
                    self.e = ttk.Entry(content_frame, width=35,
                                       font=('Arial', 14, 'bold'))
                if type(table[i]) == Grade:
                    self.e = ttk.Entry(content_frame, width=20,
                                       font=('Arial', 14, 'bold'))

                self.e.grid(row=i, column=j)

                if type(table[i]) == Student:
                    if j == 0:
                        self.e.insert(END, table[i].id)
                    if j == 1:
                        self.e.insert(END, table[i].name)
                    if j == 2:
                        self.e.insert(END, table[i].group)
                if type(table[i]) == Assignment:
                    if j == 0:
                        self.e.insert(END, table[i].id)
                    if j == 1:
                        self.e.insert(END, table[i].description)
                    if j == 2:
                        self.e.insert(END, table[i].deadline)

                if type(table[i]) == Grade:
                    if j == 0:
                        self.e.insert(END, table[i].student_id)
                    if j == 1:
                        self.e.insert(END, table[i].assignment_id)
                    if j == 2:
                        self.e.insert(END, table[i].grade_value)

        self.__top.columnconfigure(0, weight=1)
        self.__top.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        exit_button = ttk.Button(content_frame, text='Exit', width=25, command=self.__top.destroy)
        exit_button.grid(row=len(table), column=1, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __list_students(self):
        students = self.__student_services.get_students()

        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("700x400")
        self.__top.title("Students")

        self.__create_table(students)

    def __add_new_assignment_entry(self):
        try:
            assignment_id = int(self.__e1.get())
            description = self.__e2.get()
            year = int(self.__e3.get())
            month = int(self.__e4.get())
            day = int(self.__e5.get())
            hour = int(self.__e6.get())
            minute = int(self.__e7.get())
            try:
                deadline = datetime(year, month, day, hour, minute)
            except ValueError:
                messagebox.showerror("Datetime error", self.__ERRORS["DATE"])
                return
        except ValueError:
            messagebox.showerror("Add Assignment Error", self.__ERRORS["INT"])
            return
        command = Command(self.__assignment_services.add, assignment_id, description, deadline)
        undo_command = Command(self.__assignment_services.remove, assignment_id)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)
        self.__top.destroy()

    def __add_new_assignment(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("380x500")
        self.__top.title("Add Assignment")

        ttk.Label(self.__top, text='Assignment ID').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Description').grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Deadline').grid(row=2, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Year').grid(row=3, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Month').grid(row=4, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Day').grid(row=5, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Hour').grid(row=6, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Minute').grid(row=7, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e2 = ttk.Entry(self.__top)
        self.__e3 = ttk.Entry(self.__top)
        self.__e4 = ttk.Entry(self.__top)
        self.__e5 = ttk.Entry(self.__top)
        self.__e6 = ttk.Entry(self.__top)
        self.__e7 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)
        self.__e2.grid(row=1, column=1, padx=10, pady=10)
        self.__e3.grid(row=3, column=1, padx=10, pady=10)
        self.__e4.grid(row=4, column=1, padx=10, pady=10)
        self.__e5.grid(row=5, column=1, padx=10, pady=10)
        self.__e6.grid(row=6, column=1, padx=10, pady=10)
        self.__e7.grid(row=7, column=1, padx=10, pady=10)

        get_assignment_button = ttk.Button(self.__top, text='Add Assignment', width=25, command=self.__add_new_assignment_entry)
        get_assignment_button.grid(row=8, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __remove_assignment_entry(self):
        try:
            assignment_id = int(self.__e1.get())
            description = self.__assignment_services.get_description(assignment_id)
            deadline = self.__assignment_services.get_deadline(assignment_id)
        except Exception as e:
            messagebox.showerror("Remove Assignment Error", str(e))
            return

        command = Command(self.__assignment_services.remove, assignment_id)
        assignment_grades = self.__grade_services.get_assignment_grades(assignment_id)
        undo_command = AddAssignmentWithGrades(assignment_grades, self.__grade_services.add,
                                               self.__assignment_services.add, assignment_id, description, deadline)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)
        self.__top.destroy()

    def __remove_assignment(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("300x250")
        self.__top.title("Remove Assignment")

        ttk.Label(self.__top, text='Assignment ID').grid(row=0, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)

        remove_student_button = ttk.Button(self.__top, text='Remove Assignment', width=25,
                                           command=self.__remove_assignment_entry)
        remove_student_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __update_assignment_description_entry(self):
        try:
            assignment_id = int(self.__e1.get())
            new_description = self.__e2.get()
            old_description = self.__assignment_services.get_description(assignment_id)
        except Exception as e:
            messagebox.showerror("Update Assignment Description Error", str(e))
            return
        command = Command(self.__assignment_services.update_description, assignment_id, new_description)
        undo_command = Command(self.__assignment_services.update_description, assignment_id, old_description)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)
        self.__top.destroy()

    def __update_assignment_description(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("500x250")
        self.__top.title("Update Assignment Description")

        ttk.Label(self.__top, text='Assignment ID').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='New description').grid(row=1, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)
        self.__e2 = ttk.Entry(self.__top)
        self.__e2.grid(row=1, column=1, padx=10, pady=10, width=80)

        update_assignment_button = ttk.Button(self.__top, text='Update Assignment Description', width=35,
                                           command=self.__update_assignment_description_entry)
        update_assignment_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __update_assignment_deadline_entry(self):
        try:
            assignment_id = int(self.__e1.get())
            year = int(self.__e2.get())
            month = int(self.__e3.get())
            day = int(self.__e4.get())
            hour = int(self.__e5.get())
            minute = int(self.__e6.get())
            try:
                new_deadline = datetime(year, month, day, hour, minute)
            except ValueError:
                messagebox.showerror("Datetime error", self.__ERRORS["DATE"])
                return
            old_deadline = self.__assignment_services.get_deadline(assignment_id)
        except Exception as e:
            messagebox.showerror("Update Assignment Deadline Error", str(e))
            return
        command = Command(self.__assignment_services.update_description, assignment_id, new_deadline)
        undo_command = Command(self.__assignment_services.update_description, assignment_id, old_deadline)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)
        self.__top.destroy()

    def __update_assignment_deadline(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("500x400")
        self.__top.title("Update Assignment Description")

        ttk.Label(self.__top, text='Assignment ID').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='New Assignment Deadline').grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Year').grid(row=2, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Month').grid(row=3, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Day').grid(row=4, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Hour').grid(row=5, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment Minute').grid(row=6, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e2 = ttk.Entry(self.__top)
        self.__e3 = ttk.Entry(self.__top)
        self.__e4 = ttk.Entry(self.__top)
        self.__e5 = ttk.Entry(self.__top)
        self.__e6 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)
        self.__e2.grid(row=2, column=1, padx=10, pady=10)
        self.__e3.grid(row=3, column=1, padx=10, pady=10)
        self.__e4.grid(row=4, column=1, padx=10, pady=10)
        self.__e5.grid(row=5, column=1, padx=10, pady=10)
        self.__e6.grid(row=6, column=1, padx=10, pady=10)

        update_assignment_button = ttk.Button(self.__top, text='Update Assignment Deadline', width=25,
                                           command=self.__update_assignment_deadline_entry)
        update_assignment_button.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __list_assignments(self):
        assignments = self.__assignment_services.get_assignments()

        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("1400x800")
        self.__top.title("Students")

        self.__create_table(assignments)


    def __give_student_entry(self):
        try:
            student_id = int(self.__e1.get())
            assignment_id = int(self.__e2.get())
        except ValueError:
            messagebox.showerror("Student/Assignment ID error", self.__ERRORS["INT"])
            return

        command = Command(self.__grade_services.assign, student_id, assignment_id)
        undo_command = Command(self.__grade_services.remove, student_id, assignment_id)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)
        self.__top.destroy()

    def __give_student(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("350x250")
        self.__top.title("Assign Student")

        ttk.Label(self.__top, text='Student ID').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment ID').grid(row=1, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e2 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)
        self.__e2.grid(row=1, column=1, padx=10, pady=10)

        give_student_button = ttk.Button(self.__top, text='Give Assignment', width=35,
                                              command=self.__give_student_entry)
        give_student_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __give_group_entry(self):
        try:
            group = int(self.__e1.get())
            assignment_id = int(self.__e2.get())  # Assignment to be assigned to the group
        except ValueError:
            messagebox.showerror("Assignment/Group ID error", self.__ERRORS["INT"])
            return

        command = Assign(self.__grade_services.assign_group, group, assignment_id)
        undo_command = Command(self.__grade_services.remove_group_assignment, group, assignment_id)
        full_command = CommandUndoRedo(command, undo_command)
        self.__execute_command(full_command)
        self.__top.destroy()

    def __give_group(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("350x250")
        self.__top.title("Assign Group")

        ttk.Label(self.__top, text='Group ID').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment ID').grid(row=1, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e2 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)
        self.__e2.grid(row=1, column=1, padx=10, pady=10)

        give_student_button = ttk.Button(self.__top, text='Give Assignment', width=35,
                                         command=self.__give_group_entry)
        give_student_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __grade_entry_assignment(self):
        try:
            student_id =  self.__save_e
            assignment_id = int(self.__e1.get())
            grade = int(self.__e2.get())
        except ValueError:
            messagebox.showerror("Assignment ID/Grade error", self.__ERRORS["INT"])
            return

        try:
            old_grade = self.__grade_services.get_grade(student_id, assignment_id)
            command = Command(self.__grade_services.grade_assignment, student_id, assignment_id, grade)
            undo_command = Command(self.__grade_services.grade_assignment, student_id, assignment_id, old_grade)
            full_command = CommandUndoRedo(command, undo_command)  # A command equipped with undo and redo!
            self.__execute_command(full_command)  # execute the doing part of the command
            self.__top.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

    def __grade_get_assignment(self):
        self.__top.destroy()
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("300x250")
        self.__top.title("Grade Assignment")

        ttk.Label(self.__top, text='Assignment ID').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Grade Value').grid(row=1, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e2 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)
        self.__e2.grid(row=1, column=1, padx=10, pady=10)

        grade_assignment_button = ttk.Button(self.__top, text='Choose assignment', width=25,
                                             command=self.__grade_entry_assignment)
        grade_assignment_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __grade_entry(self):
        try:
            student_id = int(self.__e1.get())
        except ValueError:
            messagebox.showerror("Student ID error", self.__ERRORS["INT"])
            return

        self.__save_e = student_id
        grades = self.__grade_services.get_student_grades(student_id)

        there_is_ungraded = False
        for grade in grades:
            if grade.grade_value == 0:
                there_is_ungraded = True

        if there_is_ungraded is False:
            messagebox.showinfo("Grade info", "This student doesn't have any ungraded assignments!")
            self.__top.destroy()
            return
        self.__top.destroy()
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("1400x800")
        self.__top.title("Students")

        table = grades
        frame = ttk.Frame(self.__top)
        frame.grid(row=0, column=0, sticky="nsew")

        canvas = Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = ttk.Frame(canvas)

        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        for i in range(len(table)):
            for j in range(3):
                if type(table[i]) == Student:
                    self.e = ttk.Entry(content_frame, width=20,
                                       font=('Arial', 14, 'bold'))
                if type(table[i]) == Assignment:
                    self.e = ttk.Entry(content_frame, width=35,
                                       font=('Arial', 14, 'bold'))
                if type(table[i]) == Grade:
                    self.e = ttk.Entry(content_frame, width=20,
                                       font=('Arial', 14, 'bold'))

                self.e.grid(row=i, column=j)

                if type(table[i]) == Student:
                    if j == 0:
                        self.e.insert(END, table[i].id)
                    if j == 1:
                        self.e.insert(END, table[i].name)
                    if j == 2:
                        self.e.insert(END, table[i].group)
                if type(table[i]) == Assignment:
                    if j == 0:
                        self.e.insert(END, table[i].id)
                    if j == 1:
                        self.e.insert(END, table[i].description)
                    if j == 2:
                        self.e.insert(END, table[i].deadline)

                if type(table[i]) == Grade:
                    if j == 0:
                        self.e.insert(END, table[i].student_id)
                    if j == 1:
                        self.e.insert(END, table[i].assignment_id)
                    if j == 2:
                        self.e.insert(END, table[i].grade_value)

        self.__top.columnconfigure(0, weight=1)
        self.__top.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        exit_button = ttk.Button(content_frame, text='Exit', width=25, command=self.__grade_get_assignment)
        exit_button.grid(row=len(table), column=1, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __grade(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("300x250")
        self.__top.title("Choose Assignment")

        ttk.Label(self.__top, text='Student ID').grid(row=0, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e1.grid(row=0, column=1, padx=10, pady=10)

        grade_assignment_button = ttk.Button(self.__top, text='Choose assignment', width=25,
                                           command=self.__grade_entry)
        grade_assignment_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()


    def __execute_command(self, command: CommandUndoRedo):
        try:
            command.redo()  # basically the base command, that's what we do, then store the whole operation also containing the undo
            self.__history.record(command)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def __undo(self):
        try:
            self.__history.undo()
            messagebox.showinfo("Undo", "Undone successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def __redo(self):
        try:
            self.__history.redo()
            messagebox.showinfo("Redo", "Redone successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def __grade_descending_UI(self):
        try:
            assignment_id = int(self.__e1.get())
        except ValueError:
            messagebox.showerror("Assignment ID Error", self.__ERRORS["INT"])
            return

        grades = self.__grade_services.grade_descending(assignment_id)

        self.__top.destroy()

        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("1000x400")
        self.__top.title("Students")

        frame = ttk.Frame(self.__top)
        frame.grid(row=0, column=0, sticky="nsew")

        canvas = Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = ttk.Frame(canvas)

        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        for i in range(len(grades)):
            for j in range(4):
                self.e = ttk.Entry(content_frame, width=20,
                                       font=('Arial', 14, 'bold'))

                self.e.grid(row=i, column=j)
                student = self.__student_services.get_student(grades[i].student_id)

                if j==0:
                    self.e.insert(END, student.id)
                if j==1:
                    self.e.insert(END, student.name)
                if j==2:
                    self.e.insert(END, student.group)
                if j==3:
                    self.e.insert(END, grades[i].grade_value)

        self.__top.columnconfigure(0, weight=1)
        self.__top.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.__top.mainloop()

    def __grade_descending(self):
        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("500x250")
        self.__top.title("Choose Assignment")

        ttk.Label(self.__top, text='Show best students for assignment').grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.__top, text='Assignment ID').grid(row=1, column=0, padx=10, pady=10)
        self.__e1 = ttk.Entry(self.__top)
        self.__e1.grid(row=1, column=1, padx=10, pady=10)

        grade_assignment_button = ttk.Button(self.__top, text='Show statistics', width=30,
                                             command=self.__grade_descending_UI)
        grade_assignment_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

        self.__top.mainloop()

    def __late_students(self):
        late_students = self.__grade_services.get_late_student_grades()
        students = []
        for student_ungraded_grades in late_students:  # student_ungraded_grades is a list of their ungraded grades that are past due!
            # Just get the first grade to get the student first
            students.append(self.__student_services.get_student(student_ungraded_grades[0].student_id))

        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("1000x400")
        self.__top.title("Students")

        self.__create_table(students)

    def __best_students(self):
        best_students_grades = self.__grade_services.get_best_students_grades()
        students = []
        for student_id in best_students_grades:
            students.append(self.__student_services.get_student(student_id))

        self.__top = Toplevel(self.__main_window)
        self.__top.geometry("1000x400")
        self.__top.title("Students")

        frame = ttk.Frame(self.__top)
        frame.grid(row=0, column=0, sticky="nsew")

        canvas = Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = ttk.Frame(canvas)

        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        for i in range(len(students)):
            for j in range(4):
                self.e = ttk.Entry(content_frame, width=25,
                                   font=('Arial', 14, 'bold'))

                self.e.grid(row=i, column=j)
                student = students[i]

                if j == 0:
                    self.e.insert(END, student.id)
                if j == 1:
                    self.e.insert(END, student.name)
                if j == 2:
                    self.e.insert(END, student.group)
                if j == 3:
                    self.e.insert(END, best_students_grades[student.id])

        self.__top.columnconfigure(0, weight=1)
        self.__top.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

        self.__top.mainloop()