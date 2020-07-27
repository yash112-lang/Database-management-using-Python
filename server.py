from tkinter import *
import tkinter.messagebox as msgtk
from PIL import ImageTk, Image
import os
import subprocess


signup_window = Tk()
signup_window.geometry("600x600")

def register():
    print(username_store.get())
    print(password_store.get())
    print(cpassword_store.get())
    if(cpassword_store.get() == ""):
        msgtk.showwarning("Warning", "Confirm password should not be Empty")
    elif(password_store.get() != cpassword_store.get()):
        msgtk.showwarning("Warning", "Password & confirm password are not matched!")
    else:
        dict={username_store.get(): password_store.get()}
        print(dict)
        f=open('a.txt','a')
        for key,value in dict.items():
            a=key+': '+value
            f.write(a)
            f.write('\n')
        f.close()
        msgtk.showinfo("Success", "Your registration has been done successfully.")
def login():

    def login_creadentials():
        f=open('a.txt','r')
        k=login_username_store.get()
        v=login_password_store.get()
        b=k+': '+v
        while True:
            print(b)
            data=f.read()
            if(data==""):break
            if(b in data):
                # print('matched')
                # msgtk.showinfo("Success", "Your details has been found")
                
                def start():
                    print("Server opened successfully")
                    subprocess.Popen(['C:\\Xampp\\xampp_start.exe'])
                def stop():
                    print("Server Closed successfully")
                    subprocess.Popen(['C:\\Xampp\\xampp_stop.exe'])
                def login():
                    import tkinter.messagebox as msgtk
                    if(server_name_input.get() == ""):
                        msgtk.showwarning("Warning", "Please Enter the Valid Servername")
                    else:
                        pass
                    if(user_name_input.get() == ""):
                        msgtk.showerror("Warning", "Please Enter a Valid Username")
                    else:
                        pass
                    # if(password_input.get() == ""):
                    #     msgtk.showerror("Warning", "Please Enter a Valid Password")
                    # else:
                    #     pass
                    # second_window = Tk()
                    # second_window.mainloop()
                    host = server_name_input.get().lower()
                    user = user_name_input.get().lower()
                    if(host == "localhost") and (user == "root"):
                        running = True
                        # second_window = Tk()
                        # second_window.geometry("800x700")
                        # main_heading_label_frame = Label(second_window, text = "Welcome to iServer Manager", font = ("comicsansms 22 bold"))
                        # main_heading_label_frame.grid(padx = 200)
                        # # conn = mysql.connect(host=f"{host}", port=3306,user=f"{username}", password="")
                        # # cmd = conn.cursor()
                            



                        # second_window.mainloop()
                        # from tkinter import *
                        import tkinter.messagebox as msgtk
                        import pymysql as mysql

                        show_database_list = []
                        total_database = 0
                        def db_list():
                            global total_database
                            total_database = 0
                            conn = mysql.connect(host="localhost", port=3306, user="root", password="")
                            cmd = conn.cursor()
                            sq = "Show DATABASES"
                            cmd.execute(sq)
                            l = cmd.fetchall()
                            for i in l:
                                # global total_database
                                for k in i:
                                    show_database_list.append(k)
                                    total_database+=1
                            total_database_label.config(text = f"Total Database present : {total_database}")
                            total_database_label.update()
                            conn.commit()


                        def cd(dbn):
                            try:
                                # dbn = input("Enter Database name which you want to create
                                conn = mysql.connect(host="localhost", port=3306,user="root", password="")
                                cmd = conn.cursor()
                                q = f"create database {dbn}"
                                cmd.execute(q)
                                d = conn.commit()
                                print(d)
                                # print("Your Database is successfully created")
                                conn.close()
                                msgtk.showinfo("Success", "You database is successfully created.")
                            except Exception as e:
                                # print('Database Already exist...')
                                msgtk.showerror("Already exists", "Database Could not be created beacuse it is already exists.")
                                c = print('Error:',e)
                                # print(c)


                        def Create_New_Database():
                            dbname = dbname_original.get().lower()
                            cd(dbname)

                        def clear():
                            list_box_show_database.delete(0, END)
                            show_database_list.clear()
                        def showall():
                            clear()
                            db_list()
                            for i in range(len(show_database_list)):
                                list_box_show_database.insert(END, show_database_list[i])

                        def delete_db(dbname):
                            try:
                                conn = mysql.connect(host="localhost", port=3306, user="root", password="")
                                cmd = conn.cursor()
                                dq = f"DROP DATABASE {dbname}"
                                print("Database deleted successfully.")
                                cmd.execute(dq)
                                conn.commit()
                                conn.close()
                                msgtk.showinfo("Success", "Database was deleted successfully.")
                            except Exception:
                                msgtk.showerror("Error", "Database could not be deleted.")









                        def delete():
                            delete_db(db_delete_name.get().lower())

                            




                        def delete_selected_item():
                            if (len(delete_item_name) == 0):
                                print("Ddssd")
                            delete_db(delete_item_name.lower())

                        def exit_main_window():
                            message = msgtk.askyesno("Quit", "Do you really want to exit")
                            if(message):
                                second_window.destroy()
                                running = False
                            else:
                                pass






                        def refresh():
                            clear()
                            second_window.update()
                            db_list()
                            second_window.update()
                            for i in range(len(show_database_list)):
                                list_box_show_database.insert(END, show_database_list[i])
                            second_window.update()
                            msgtk.showinfo("Refresh", "Database is refreshed successfully.")


                        delete_item_name = []
                        def delete_selected():
                            # print(len(delete_item_name))
                            delete_item_name.clear()
                            list_of_selected = list_box_show_database.curselection()
                            print(list_of_selected)
                            if(len(list_of_selected) == 0):
                                msgtk.showwarning("Warning", "Please select a Database first !")
                            for item in list_of_selected:
                                print(item)
                                delete_item_name.append(list_box_show_database.get(item))
                            for i in range(len(delete_item_name)):
                                print(delete_item_name[i])
                                yes_no = msgtk.askyesno("Confirm Delete", "Do you want to permanently delete the selected database ?")
                                if(yes_no):
                                    delete_db(delete_item_name[i].lower())
                                else:
                                    pass
                            

                        def tables():
                            import tkinter.messagebox as msgtk
                            import pymysql as mysql


                            # third_window = Tk()
                            third_window = Toplevel(second_window)
                            third_window.geometry("1000x700")









                            ###############################################################Functions#################################################################
                            #############clear function###############
                            def database_clear():
                                third_window_show_list_box_show_database.delete(0, END)
                                show_database_list.clear()
                                third_window_show_list_box_show_table.delete(0, END)
                                show_table_list.clear()

                            def table_clear():
                                third_window_show_list_box_show_table.delete(0, END)
                                show_table_list.clear()




                            ###############show database function##################
                            show_database_list = []
                            total_database = 0
                            def db_list():
                                global total_database
                                total_database = 0
                                conn = mysql.connect(host="localhost", port=3306, user="root", password="")
                                cmd = conn.cursor()
                                sq = "Show DATABASES"
                                cmd.execute(sq)
                                l = cmd.fetchall()
                                for i in l:
                                    # global total_database
                                    for k in i:
                                        show_database_list.append(k)
                                        total_database+=1
                                # total_database_label.config(text = f"Total Database present : {total_database}")
                                # total_database_label.update()
                                conn.commit()




                            #########################Show Table Function############################
                            show_table_list = []
                            def show_table(dbname):
                                show_table_list.clear()
                                table_clear()
                                conn = mysql.connect(host = "localhost", port = 3306, user = "root", password = "", db = f"{dbname}")
                                cmd = conn.cursor()
                                sq = "SHOW TABLES"
                                cmd.execute(sq)
                                l = cmd.fetchall()
                                for i in l:
                                    for k in i:
                                        show_table_list.append(k)
                                        # print(k)
                                conn.commit()
                            #####################Database function start here##########
                            def showalldatabase():
                                database_clear()
                                db_list()
                                for i in range(len(show_database_list)):
                                    third_window_show_list_box_show_database.insert(END, show_database_list[i])



                            def refreshdatabase():
                                database_clear()
                                third_window.update()
                                showalldatabase()
                                third_window.update()
                                for i in range(len(show_database_list)):
                                    third_window_show_list_box_show_database.insert(END, show_database_list[i])
                                third_window.update()
                                msgtk.showinfo("Refresh", "Database is refreshed successfully.")


                            ##############Table Function start here########################
                            connections_name = []
                            show_table_name = []
                            def showalltable():
                                show_table_name.clear()
                                # connections_name.clear()
                                list_of_selected = third_window_show_list_box_show_database.curselection()
                                # print(list_of_selected)
                                if(len(list_of_selected) == 0):
                                    msgtk.showwarning("Warning", "Please select a Database first !")
                                else:
                                    for item in list_of_selected:
                                        pass
                                    show_table_name.append(third_window_show_list_box_show_database.get(item))
                                    for i in range(len(show_table_name)):
                                        # print(show_table_name[i])
                                        database_table_name = show_table_name[i]
                                        connections_name.append(database_table_name)
                                        # print(database_table_name)
                                        # clear()
                                        show_table(database_table_name)
                                        for i in range(len(show_table_list)):
                                            third_window_show_list_box_show_table.insert(END, show_table_list[i])



                            def refreshtable():
                                show_table_name.clear()
                                list_of_selected = third_window_show_list_box_show_database.curselection()
                                # print(list_of_selected)
                                if(len(list_of_selected) == 0):
                                    msgtk.showwarning("Warning", "Please select a Database first !")
                                else:
                                    for item in list_of_selected:
                                        pass
                                    show_table_name.append(third_window_show_list_box_show_database.get(item))
                                    for i in range(len(show_table_name)):
                                        # print(show_table_name[i])
                                        database_table_name = show_table_name[i]
                                        # clear()
                                        show_table(database_table_name)
                                        for i in range(len(show_table_list)):
                                            third_window_show_list_box_show_table.insert(END, show_table_list[i])
                                    msgtk.showinfo("Refresh", "table is refreshed successfully.")




                            def delete_selected_table(dbn, tname):
                                conn = mysql.connect(host="localhost", port=3306,user="root", password="", db = f"{dbn}")
                                cmd = conn.cursor()
                                q = f"drop table {tname}"
                                cmd.execute(q)
                                d = conn.commit()
                                conn.close()
                                msgtk.showinfo("Success", "You database is deleted successfully.")
                                # connections_name.clear()



                            def quit_table():
                                yes_no_choice = msgtk.askyesno("Quit", "Do you want to Quit.")
                                if(yes_no_choice):
                                    quit()
                                    third_window.destroy()
                                    running = False


                            def delete_table():
                                clicked_items = third_window_show_list_box_show_table.curselection()
                                print(clicked_items)
                                if(len(clicked_items) == 0):
                                    msgtk.showwarning("Warning", "Please Select a Table first !")
                                else:
                                    for items in clicked_items:
                                        print(third_window_show_list_box_show_table.get(items))
                                        table_element_selected = third_window_show_list_box_show_table.get(items)
                                #         connections_name.append(table_element_selected)
                                        print(connections_name[0])
                                        delete_selected_table(connections_name[0], table_element_selected)
                                        # print(connections_name)


                            ####################################Create table#########################################################
                            def create_table_with_in_database(dname, tbname):
                                try:
                                    print(dname, tbname)
                                    # conn = mysql.connect(host = "localhost", port = 3306, user = "root", password = "", db = dname)
                                    conn = mysql.connect(host="localhost", port=3306,user="root", password="", db = f"{dname}")
                                    cmd = conn.cursor()
                                    q = f"create table {tbname}"
                                    cmd.execute(q)
                                    d = conn.commit()
                                    conn.close()
                                    msgtk.showinfo("Success", "You database is deleted successfully.")
                                    msgtk.showinfo("Success", "Your table is now created.")
                                except Exception as e:
                                    print("Error : ", e)
                                    msgtk.showerror("Error", "Your table is not created due to some technical issue. Sorry for your inconvinience")


                            db_data = []
                            def create_table():
                                clicked_database_items = third_window_show_list_box_show_database.curselection()
                                # print(clicked_database_items)
                                if(len(clicked_database_items) == 0):
                                    msgtk.showwarning("Warning", "Please Select a Database first")
                                else:
                                    for items in clicked_database_items:
                                        # print(third_window_show_list_box_show_database.get(items))
                                        database_element_selected = third_window_show_list_box_show_database.get(items)
                                    # table_name_new_window = Tk()
                                    from tkinter import ttk
                                    table_name_new_window = Toplevel(third_window)
                                    table_name_new_window.geometry("250x250")
                                    print(database_element_selected)
                                    def table_name_from_button():
                                        try:
                                            tbname = table_name_given_by_user.get()
                                            cnumber = table_number_given_by_user.get()
                                            if(tbname == "" or cnumber == ""):
                                                msgtk.showerror("Name Error", "No Table name Entered")
                                            elif(cnumber == 0):
                                                msgtk.showwarning("Warning", "Number of Rows Can't be Zero")
                                            elif(cnumber>9):
                                                msgtk.showwarning("Warning", "You can add maximum 9 Rows at a Time")
                                            else:
                                                print(tbname)
                                                print(cnumber)
                                                # table_name_new_window.destroy()
                                                # rows_window = Tk()
                                                rows_window = Toplevel(table_name_new_window)
                                                rows_window.geometry("900x800")
                                                number_of_rows = cnumber
                                                # print(cnumber)
                                                def create_table(dbname, tname, a, b, c):
                                                    try:
                                                        conn = mysql.connect(host="localhost", port=3306,user="root", password="", db = dbname)
                                                        cmd = conn.cursor()
                                                        if(len(a) == 1):
                                                            q = f'CREATE TABLE {tname} ({a[0]} {b[0]}({c[0]}))'
                                                        elif(len(a) == 2):
                                                            q = f'CREATE TABLE {tname} ({a[0]} {b[0]}({c[0]}), {a[1]} {b[1]}({c[1]}))'
                                                        elif(len(a) == 3):
                                                            q = f'CREATE TABLE {tname} ({a[0]} {b[0]}({c[0]}), {a[1]} {b[1]}({c[1]}), {a[2]} {b[2]}({c[2]}))'
                                                        elif(len(a) == 4):
                                                            q = f'CREATE TABLE {tname} ({a[0]} {b[0]}({c[0]}), {a[1]} {b[1]}({c[1]}), {a[2]} {b[2]}({c[2]}), {a[3]} {b[3]}({c[3]}))'
                                                        elif(len(a) == 5):
                                                            q = f'CREATE TABLE {tname} ({a[0]} {b[0]}({c[0]}), {a[1]} {b[1]}({c[1]}), {a[2]} {b[2]}({c[2]}), {a[3]} {b[3]}({c[3]}), {a[4]} {b[4]}({c[4]}))'
                                                        elif(len(a) == 6):
                                                            q = f'CREATE TABLE {tname} ({a[0]} {b[0]}({c[0]}), {a[1]} {b[1]}({c[1]}), {a[2]} {b[2]}({c[2]}), {a[3]} {b[3]}({c[3]}), {a[4]} {b[4]}({c[4]}), {a[5]} {b[5]}({c[5]}))'
                                                        elif(len(a) == 7):
                                                            q = f'CREATE TABLE {tname} ({a[0]} {b[0]}({c[0]}), {a[1]} {b[1]}({c[1]}), {a[2]} {b[2]}({c[2]}), {a[3]} {b[3]}({c[3]}), {a[4]} {b[4]}({c[4]}), {a[5]} {b[5]}({c[5]}), {a[6]} {b[6]}({c[6]}))'
                                                        elif(len(a) == 8):
                                                            q = f'CREATE TABLE {tname} ({a[0]} {b[0]}({c[0]}), {a[1]} {b[1]}({c[1]}), {a[2]} {b[2]}({c[2]}), {a[3]} {b[3]}({c[3]}), {a[4]} {b[4]}({c[4]}), {a[5]} {b[5]}({c[5]}), {a[6]} {b[6]}({c[6]}), {a[7]} {b[7]}({c[7]}))'
                                                        elif(len(a) == 9):
                                                            q = f'CREATE TABLE {tname} ({a[0]} {b[0]}({c[0]}), {a[1]} {b[1]}({c[1]}), {a[2]} {b[2]}({c[2]}), {a[3]} {b[3]}({c[3]}), {a[4]} {b[4]}({c[4]}), {a[5]} {b[5]}({c[5]}), {a[6]} {b[6]}({c[6]}), {a[7]} {b[7]}({c[7]}), {a[8]} {b[8]}({c[8]}))'

                                                        cmd.execute(q)
                                                        conn.commit()
                                                        # print(d)
                                                        # print("Your Database is successfully created")
                                                        conn.close()
                                                        msgtk.showinfo("Success on creating", "Table is successfully created.")
                                                        rows_window.destroy()
                                                    except Exception as e:
                                                        msgtk.showwarning("Warning", "Probably you typed wrong rows.")
                                                m = 20
                                                n = 60
                                                
                                                rows_label = Label(rows_window, text = "Enter row details", font = ("comicsansms, 14"))
                                                rows_label.grid()
                                                rows_label.place(x = 400, y = 0 )
                                                list_of_rows_name = []
                                                list_of_type = []
                                                list_of_length = []
                                                list_of_check_button = []
                                                row_name_entry1 = StringVar()
                                                row_name_entry2 = StringVar()
                                                row_name_entry3 = StringVar()
                                                row_name_entry4 = StringVar()
                                                row_name_entry5 = StringVar()
                                                row_name_entry6 = StringVar()
                                                row_name_entry7 = StringVar()
                                                row_name_entry8 = StringVar()
                                                row_name_entry9 = StringVar()
                                                row_combo_box_input1 = StringVar()
                                                row_combo_box_input2 = StringVar()
                                                row_combo_box_input3 = StringVar()
                                                row_combo_box_input4 = StringVar()
                                                row_combo_box_input5 = StringVar()
                                                row_combo_box_input6 = StringVar()
                                                row_combo_box_input7 = StringVar()
                                                row_combo_box_input8 = StringVar()
                                                row_combo_box_input9 = StringVar()
                                                rows_length_entry1 = IntVar()
                                                rows_length_entry2 = IntVar()
                                                rows_length_entry3 = IntVar()
                                                rows_length_entry4 = IntVar()
                                                rows_length_entry5 = IntVar()
                                                rows_length_entry6 = IntVar()
                                                rows_length_entry7 = IntVar()
                                                rows_length_entry8 = IntVar()
                                                rows_length_entry9 = IntVar()
                                                row_check_button_input1 = IntVar()
                                                row_check_button_input2 = IntVar()
                                                row_check_button_input3 = IntVar()
                                                row_check_button_input4 = IntVar()
                                                row_check_button_input5 = IntVar()
                                                row_check_button_input6 = IntVar()
                                                row_check_button_input7 = IntVar()
                                                row_check_button_input8 = IntVar()
                                                row_check_button_input9 = IntVar()
                                                def submit_details():
                                                    try:
                                                        for j in range(number_of_rows):
                                                            list_of_rows_name.append(row_name_entry[j].get())
                                                            list_of_type.append(row_combo_box_input[j].get())
                                                            list_of_length.append(rows_length_entry[j].get())
                                                            list_of_check_button.append(row_check_button_input[j].get())
                                                        print(list_of_rows_name)
                                                        print(list_of_type)
                                                        print(list_of_length)
                                                        print(list_of_check_button)
                                                        confirmyn = msgtk.askyesno("Confirm", "Do you want to really create the table")
                                                        if(confirmyn):
                                                            create_table(database_element_selected, tbname, list_of_rows_name, list_of_type, list_of_length)
                                                        else:
                                                            pass
                                                        list_of_rows_name.clear()
                                                        list_of_type.clear()
                                                        list_of_length.clear()
                                                        list_of_check_button.clear()
                                                    except:
                                                        msgtk.showerror("Error", "There was an internal server error please try again after some time.")
                                                row_name_entry = [row_name_entry1, row_name_entry2, row_name_entry3, row_name_entry4, row_name_entry5, row_name_entry6, row_name_entry7, row_name_entry8, row_name_entry9]
                                                row_combo_box_input = [row_combo_box_input1, row_combo_box_input2, row_combo_box_input3, row_combo_box_input4, row_combo_box_input5, row_combo_box_input6, row_combo_box_input7, row_combo_box_input8, row_combo_box_input9]
                                                rows_length_entry = [rows_length_entry1, rows_length_entry2, rows_length_entry3, rows_length_entry4, rows_length_entry5, rows_length_entry6, rows_length_entry7, rows_length_entry8, rows_length_entry9]
                                                row_check_button_input = [row_check_button_input1, row_check_button_input2, row_check_button_input3, row_check_button_input4, row_check_button_input5, row_check_button_input6, row_check_button_input7, row_check_button_input8, row_check_button_input9]




                                                rows_label = Label(rows_window, text = "Name", font = ("comicsansms, 14"))
                                                rows_label.grid()
                                                rows_label.place(x = 10, y = 25)


                                                rows_label = Label(rows_window, text = "Type", font = ("comicsansms, 14"))
                                                rows_label.grid()
                                                rows_label.place(x = 230, y = 25)


                                                rows_label = Label(rows_window, text = "Length/Values", font = ("comicsansms, 14"))
                                                rows_label.grid()
                                                rows_label.place(x = 450, y = 25)
                                                rows_label = Label(rows_window, text = "Auto Increament", font = ("comicsansms, 14"))
                                                rows_label.grid()
                                                rows_label.place(x = 630, y = 25)
                                                # m+=80
                                                for i in range(number_of_rows):
                                                    rows_entry = Entry(rows_window, textvariable = row_name_entry[i], font = ("comicsansms, 10"))
                                                    rows_entry.grid()
                                                    rows_entry.place(x = 10, y = n, width = 150, height = 24)
                                                    type_combobox = ttk.Combobox(rows_window, textvariable = row_combo_box_input[i], state = "readonly", font = ("10"))
                                                    type_combobox["values"] = ("INT", "VARCHAR", "TEXT", "DATETIME")
                                                    type_combobox.current(1)
                                                    type_combobox.grid()
                                                    type_combobox.place(x = 230, y = n, width = 150, height = 24)
                                                    rows_entry = Entry(rows_window, textvariable = rows_length_entry[i], font = ("comicsansms, 10"))
                                                    rows_entry.grid()
                                                    rows_entry.place(x = 450, y = n, width = 150, height = 24)
                                                    check_button = Checkbutton(rows_window, variable = row_check_button_input[i])    
                                                    check_button.grid()
                                                    check_button.place(x = 700, y = n)
                                                    n+=80
                                                submit_button = Button(rows_window, text = "Submit", command = submit_details)
                                                submit_button.grid()
                                                submit_button.place(x = 10, y = 650)

                                                rows_window.mainloop()

                                                
                                            
                                        except Exception as e:
                                            # msgtk.showwarning("Warning", "You can only select numbers")
                                            print(e)



                                    table_number_given_by_user = IntVar()
                                    table_user_ask_number_label = Label(table_name_new_window, text = "Number Of Rows", font = ("10"))
                                    table_user_ask_number_label.grid()
                                    table_user_ask_number_label.place(x = 15, y = 100)

                                    table_user_ask_number_input_box = Entry(table_name_new_window, textvariable = table_number_given_by_user, font = ("10"))
                                    table_user_ask_number_input_box.grid()
                                    table_user_ask_number_input_box.place(x = 15, y =150)

                                    table_user_ask_number_button = Button(table_name_new_window, text = "Enter", font = ("10"), command = table_name_from_button)
                                    table_user_ask_number_button.grid()
                                    table_user_ask_number_button.place(x = 70, y = 200)



                                    table_name_given_by_user = StringVar()
                                    table_user_ask_name_label = Label(table_name_new_window, text = "Enter New Table Name", font = ("10"))
                                    table_user_ask_name_label.grid()
                                    table_user_ask_name_label.place(x = 15, y = 20)

                                    table_user_ask_name_input_box = Entry(table_name_new_window, textvariable = table_name_given_by_user, font = ("10"))
                                    table_user_ask_name_input_box.grid()
                                    table_user_ask_name_input_box.place(x = 10, y = 60)

                                    # table_user_ask_name_button = Button(table_name_new_window, text = "Create", font = ("10"), command = table_name_from_button)
                                    # table_user_ask_name_button.grid()
                                    # table_user_ask_name_button.place(x = 70, y = 100)





                                    table_name_new_window.mainloop()





























                            dblist_selected = []
                            def select_database():
                                list_of_clicked_db_name = third_window_show_list_box_show_database.curselection()
                                for item in list_of_clicked_db_name:
                                        dbname_selected = third_window_show_list_box_show_database.get(item)
                                        dblist_selected.append(dbname_selected)

                            def show_record():

                                from tkinter import ttk
                                # list_of_clicked_db_name = third_window_show_list_box_show_database.curselection()
                                list_of_clicked_table_name = third_window_show_list_box_show_table.curselection()
                                if(len(list_of_clicked_table_name) == 0):
                                    msgtk.showwarning("Warning", "Please Select a table first")
                                # elif(len(dblist_selected) == 0):
                                #     msgtk.showwarning("Warning", "Please follow the given procedure\n1.Click on database than click on select database button\n2.Selct the table and press the Show Record button")
                                else:
                                    print(dblist_selected)
                                    # print(list_of_selected_db_name)
                                    row_window = Toplevel()
                                    row_window.geometry("1200x700")
                                    treev = ttk.Treeview(row_window, selectmode ='browse') 
                                    
                                    # Calling pack method w.r.to treeview 
                                    treev.pack(side ='right') 
                                    # for item in list_of_clicked_db_name:
                                    #     dbname_selected = third_window_show_list_box_show_database.get(item)
                                    #     dblist_selected.append(dbname_selected)
                                    for item in list_of_clicked_table_name:
                                        tbname_selected = third_window_show_list_box_show_table.get(item)
                                        dblist_selected.append(tbname_selected)
                                    
                                    print(dblist_selected)
                                    columns_name_list = []
                                    conn = mysql.connect(host="localhost", port=3306,user="root", password="")
                                    cmd = conn.cursor()
                                    # q = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'user'"
                                    # q = f"SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='dbname_selected' AND `TABLE_NAME`='tbname_selected'"
                                    q = f"SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='{dblist_selected[0]}' AND `TABLE_NAME`='{dblist_selected[1]}'"
                                    dblist_selected.clear()
                                    cmd.execute(q)
                                    l = cmd.fetchall()
                                    for i in l:
                                    # global total_database
                                        for k in i:
                                            # print(k)
                                            columns_name_list.append(k)
                                    # print(columns_name_list)
                                    conn.commit()
                                    # Constructing vertical scrollbar 
                                    # with treeview 
                                    verscrlbar = ttk.Scrollbar(row_window, orient ="vertical", command = treev.yview) 
                                    
                                    # Calling pack method w.r.to verical  
                                    # scrollbar 
                                    verscrlbar.pack(side ='right', fill ='x') 
                                    verscrlbar.place(x = 1180, y = 35, height = 650)
                                    
                                    # Configuring treeview 
                                    treev.configure(xscrollcommand = verscrlbar.set) 

                                    # Defining number of columns
                                    tup1 = []
                                    for i in range(len(columns_name_list)):
                                        tup1.append(str(i+1))
                                    # print(tuple(tup1))
                                    treev["columns"] = tuple(tup1)

                                    # Defining heading 
                                    treev['show'] = 'headings'
                                    
                                    # Assigning the width and anchor to  the 
                                    # respective columns
                                    # print(len(columns_name_list))
                                    total_width = 1200/len(columns_name_list)
                                    for i in range(len(treev["columns"])):
                                        treev.column(i+1, width = int(total_width), anchor ='nw') 
                                    # treev.column("2", width = int(1200/len(columns_name_list)), anchor ='nw') 
                                    # treev.column("3", width = int(1200/len(columns_name_list)), anchor ='nw') 
                                    
                                    # Assigning the heading names to the  
                                    # respective columns
                                    for i in range(len(columns_name_list)):
                                        treev.heading(i+1, text = columns_name_list[i]) 
                                    
                                    # Inserting the items and their features to the  
                                    # columns built
                                    conn = mysql.connect(host="localhost", port=3306,user="root", password="", db = "school")
                                    cmd = conn.cursor()
                                    q = "select * from faculties"
                                    cmd.execute(q)
                                    l = cmd.fetchall()
                                    total_number_label = Label(row_window, text = f"Total {len(l)} records found in this table")
                                    total_number_label.pack()
                                    total_number_label.place(x = 980, y = 25)
                                    for i in l:
                                        treev.insert("", 'end', text ="L1", values = i)
                                        # print(i)
                                    # print(len(l))



                                    treev.place(x = 10, y = 50, width = 1180, height = 650)

                                    row_window.mainloop()




                            #######################################################Tables Maupulation################################################################
                            third_window_main_label = Label(third_window, text = "Table Manager", font = ("comicsansms 22 bold"))
                            third_window_main_label.grid(row = 0, column = 0, padx = 400)









                            third_window_show_database_label = Label(third_window, text = "Databases", font = ("comicsansms 18 bold"))
                            third_window_show_database_label.grid(row = 1, column = 0)
                            third_window_show_database_label.place(x = 40, y = 40)
                            third_window_show_list_box_frame = Frame(third_window)
                            scrollbar = Scrollbar(third_window, orient = VERTICAL)
                            scrollbar.grid(row = 4, column = 0, ipady = 40, padx = 20)
                            scrollbar.place(x = 525, y = 60, height = 280)
                            third_window_show_list_box_show_database = Listbox(third_window, yscrollcommand = scrollbar.set, font = ("10"), selectmode = EXTENDED)
                            third_window_show_list_box_show_database.grid()
                            third_window_show_list_box_show_database.place(y = 80, x = 25, width = 500)
                            scrollbar.config(command = third_window_show_list_box_show_database.yview)
                            third_window_show_list_box_frame.grid()












                            third_window_show_table_label = Label(third_window, text = "Tables", font = ("comicsansms 18 bold"))
                            third_window_show_table_label.grid(row = 2, column = 0)
                            third_window_show_table_label.place(x = 40, y = 350)
                            third_window_show_list_box_frame = Frame(third_window)
                            scrollbar = Scrollbar(third_window, orient = VERTICAL)
                            scrollbar.grid(row = 4, column = 0, ipady = 40, padx = 20)
                            scrollbar.place(x = 525, y = 370, height = 280)
                            third_window_show_list_box_show_table = Listbox(third_window, yscrollcommand = scrollbar.set, font = ("10"), selectmode = EXTENDED)
                            third_window_show_list_box_show_table.grid()
                            third_window_show_list_box_show_table.place(y = 390, x = 25, width = 500)
                            scrollbar.config(command = third_window_show_list_box_show_table.yview)
                            third_window_show_list_box_frame.grid()

                            



                            ############################Buttons####################################

                            third_window_show_database_button = Button(third_window, text = "Show All", font = ("18"), command = showalldatabase)
                            third_window_show_database_button.grid(row = 3, column = 0 )
                            third_window_show_database_button.place(x = 220, y = 35)



                            third_window_show_database_button = Button(third_window, text = "Refresh", font = ("18"), command = refreshdatabase)
                            third_window_show_database_button.grid(row = 3, column = 0 )
                            third_window_show_database_button.place(x = 420, y = 35)



                            third_window_show_database_button = Button(third_window, text = "Show Table", font = ("18"), command = showalltable)
                            third_window_show_database_button.grid(row = 3, column = 0 )
                            third_window_show_database_button.place(x = 220, y = 340)



                            third_window_show_database_button = Button(third_window, text = "Create Table", font = ("18"), command = create_table)
                            third_window_show_database_button.grid(row = 3, column = 0 )
                            third_window_show_database_button.place(x = 20, y = 650)



                            third_window_show_database_button = Button(third_window, text = "Delete", font = ("18"), command = delete_table)
                            third_window_show_database_button.grid(row = 3, column = 0 )
                            third_window_show_database_button.place(x = 250, y = 650)



                            third_window_show_database_button = Button(third_window, text = "Quit", font = ("18"), command = quit_table)
                            third_window_show_database_button.grid(row = 3, column = 0 )
                            third_window_show_database_button.place(x = 450, y = 650)



                            third_window_show_database_button = Button(third_window, text = "Refresh", font = ("18"), command = refreshtable)
                            third_window_show_database_button.grid(row = 3, column = 0 )
                            third_window_show_database_button.place(x = 420, y = 340)

                            

                            third_window_show_database_button = Button(third_window, text = "Show Records", font = ("18"), command = show_record)
                            third_window_show_database_button.grid(row = 3, column = 0 )
                            third_window_show_database_button.place(x = 750, y = 650)

                            

                            third_window_show_database_button = Button(third_window, text = "Select Database", font = ("18"), command = select_database)
                            third_window_show_database_button.grid(row = 3, column = 0 )
                            third_window_show_database_button.place(x = 600, y = 650)







                            third_window.mainloop()




                        # variables

                        second_window = Toplevel(root)
                        second_window.geometry("800x700")
                        second_window.minsize(300, 400)
                        second_window.maxsize(800, 700)
                        main_heading_label_frame = Label(second_window, text = "Welcome to iServer Manager", font = ("comicsansms 22 bold"))
                        main_heading_label_frame.grid(padx = 200)

                        #####################################################Create Database Label###############################################################
                        create_new_database_label = Label(second_window, text = "Create New Database", font = ("comicsansms 18"))
                        create_new_database_label.grid(row = 1, column = 0, sticky = W, padx = 10)
                        dbname_original = StringVar()
                        create_new_database_entry = Entry(second_window, font = "20", textvariable = dbname_original)
                        create_new_database_entry.insert(0, "Name Of Database")
                        create_new_database_entry.grid(row = 1, column = 0, ipadx = 30, ipady = 8, pady= 20, padx = 20)
                        create2_new_database_label = Label(second_window)
                        create2_new_database_label.grid(row = 1, column = 0)
                        create2_new_database_label.place(x = 270, y = 105)
                        create_new_database_button = Button(second_window, text = "Create", font = ("18"), command = Create_New_Database)
                        create_new_database_button.grid(row = 1, column = 0 )
                        create_new_database_button.place(x = 600, y = 55)



                        ####################################################Delete Databases Label##################################################################
                        delete_database_label = Label(second_window, text = "Search Database", font = ("comicsansms 18"))
                        delete_database_label.grid(row = 2, column = 0, sticky = W, padx = 10)
                        db_delete_name = StringVar()
                        delete_database_entry = Entry(second_window, font = "20", textvariable = db_delete_name)
                        delete_database_entry.insert(0, "Name Of Database")
                        delete_database_entry.grid(row = 2, column = 0, ipadx = 30, ipady = 8, pady= 20, padx = 20)
                        delete_database_button = Button(second_window, text = "Delete", font = ("18"), command = delete)
                        delete_database_button.grid(row = 2, column = 0 )
                        delete_database_button.place(x = 600, y = 145)

                        ####################################################Show Databases Label####################################################################
                        show_database_button = Button(second_window, text = "Show All", font = ("18"), command = showall)
                        show_database_button.grid(row = 3, column = 0 )
                        show_database_button.place(x = 100, y = 225)



                        show_database_button = Button(second_window, text = "Refresh", font = ("18"), command = refresh)
                        show_database_button.grid(row = 3, column = 0 )
                        show_database_button.place(x = 600, y = 225)



                        ###################################################Total database#########################################################################################################
                        total_database_label = Label(second_window, text = f"Total Database present : {total_database}")
                        total_database_label.grid()
                        total_database_label.place(x = 600, y = 370)


                        ####################################################List Box Label#######################################################################
                        list_datbase_label = Label(second_window, text = "List of Databases", font = ("comicsansms 20 bold"))
                        list_datbase_label.grid()
                        list_datbase_label.place(x = 300 , y = 300)
                        list_box_frame = Frame(second_window)
                        scrollbar = Scrollbar(second_window, orient = VERTICAL, background='blue')
                        scrollbar.grid(row = 4, column = 0, ipady = 40, padx = 20)
                        scrollbar.place(x = 775, y = 380, height = 280)
                        list_box_show_database = Listbox(second_window, yscrollcommand = scrollbar.set, font = ("10"), selectmode = EXTENDED)
                        list_box_show_database.grid()
                        list_box_show_database.place(y = 400, x = 25, width = 750)
                        scrollbar.config(command = list_box_show_database.yview)
                        list_box_frame.grid()



                        show_database_button = Button(second_window, text = "Manupulate Tables", font = ("18"), command = tables)
                        show_database_button.grid(row = 5, column = 0 )
                        show_database_button.place(x = 300, y = 225)



                        show_database_button = Button(second_window, text = "Delete Selected", font = ("18"), command = delete_selected)
                        show_database_button.grid(row = 6, column = 0 )
                        show_database_button.place(x = 50, y = 655)



                        show_database_button = Button(second_window, text = "Quit", font = ("18"), command = exit_main_window)
                        show_database_button.grid(row = 6, column = 0 )
                        show_database_button.place(x = 700, y = 655)


                        # root.destroy()
                        second_window.mainloop()



                    else:
                        msgtk.showerror("Connection Error","You typed incorrect servername or username. That's why Your connection can't be made")






                root = Toplevel()                #initializing Tk variable
                root.geometry("750x400")    #Defining geometry or screen size
                root.minsize(100,100)       #Defining minimum size of the window
                root.maxsize(1000,1000)     #Defining maximum size of window
                root.title("iServer Login") #Defining title here
                # variables
                # host = (server_name_input.get()).lower()
                # username = user_name_input.get().lower()
                # password = password_input.get().lower()


                main_heading_label = Label(root, text = "iServer Manager", bg = "blue", fg = "white", font = ("comicsansms 34 bold"), relief = "sunken")
                main_heading_label.grid(row = 0, column = 0)

                manage_server_frame = Frame(root)
                start_server_label = Label(manage_server_frame, text = "Click this button to Manage server →", font = ("halvetica, 22"))
                start_server_label.grid(row = 1, column = 0)
                start_server_button = Button(manage_server_frame, text = "Start Server", font = ("Halvetica"), command = start)
                start_server_button.grid(padx = 10, row = 1, column = 1)
                stop_server_button = Button(manage_server_frame, text = "Stop Server", font = ("Halvetica"), command = stop)
                stop_server_button.grid(row = 1, column = 2)
                manage_server_frame.grid(pady = 20)






                server_input_frame = Frame(root)

                server_name_input = StringVar()
                user_name_input = StringVar()
                password_input = StringVar()
                server_name_label = Label(root, text = "Enter server name: ", font = ("Halvetica 18")).grid(row = 2, column = 0, sticky = W)
                server_name_entry = Entry(root, font = ("Halvetica 18"), textvariable = server_name_input).grid(row = 2, columnspan = 1, ipadx = 18, ipady = 4)
                user_name_label = Label(root, text = "Enter user name: ", font = ("Halvetica 18")).grid(row = 3, column = 0, sticky = W)
                user_name_entry = Entry(root, font = ("Halvetica 18"), textvariable = user_name_input).grid(row = 3, columnspan = 1, ipadx = 18, ipady = 4, pady = 10)
                password_label = Label(root, text = "Enter password: ", font = ("Halvetica 18")).grid(row = 4, column = 0, sticky = W)
                password_entry = Entry(root, font = ("Halvetica 18"), textvariable = password_input).grid(row = 4, columnspan = 1, ipadx = 18, ipady = 4, pady = 10)
                connection_button = Button(server_input_frame, text = "Login",font = ("Halvetica 18"), command = login)
                connection_button.grid(row = 5, column = 0)

                server_input_frame.grid()

                # create_database_frame = Frame(root)
                # create_database_label = Label(create_database_frame, text = "Database Name : ")
                # database_name = StringVar()
                # create_database_input = Entry(create_database_frame, textvariable = database_name).grid()
                # create_database_button = Button(create_database_frame, text = "Create Database", command = create_database)
                # create_database_button.grid()
                # create_database_label.grid()
                # create_database_frame.grid()
















                root.mainloop()
                break
            else:
                # print('unmatched')
                msgtk.showwarning("Warning", "You enter invalid credentials.") 
                break
        f.close()
    # signup_window.destroy()
    login_window = Toplevel(signup_window)
    login_window.geometry("500x500")
    image1 = Image.open("c.png")
    photo1 = ImageTk.PhotoImage(image1)
    mylabel1 = Label(login_window, image = photo1)
    mylabel1.grid()
    mylabel1.place(x = 150, y = 10)

    login_username_label = Label(login_window, text = "Name :", font = ("16"))
    login_username_label.grid()
    login_username_label.place(x = 50, y = 300)
    login_password_label = Label(login_window, text = "Password :", font = ("16"))
    login_password_label.grid()
    login_password_label.place(x = 50, y = 350)

    login_username_store = StringVar()
    login_password_store = StringVar()
    login_username_entry = Entry(login_window, font = ("16"), textvariable = login_username_store)
    login_username_entry.grid()
    login_username_entry.place(x = 200, y = 300)
    login_password_entry = Entry(login_window, font = ("16"), show = "*", textvariable = login_password_store)
    login_password_entry.grid()
    login_password_entry.place(x = 200, y = 350)

    login_button = Button(login_window, text = "Login", font = ("12"), command = login_creadentials)
    login_button.grid()
    login_button.place(x = 250, y = 400)




    login_window.mainloop()

image = Image.open("c.png")
photo = ImageTk.PhotoImage(image)
mylabel = Label(signup_window, image = photo)
mylabel.grid()
mylabel.place(x = 200, y = 50)

register_username_label = Label(signup_window, text = "Name :", font = ("16"))
register_username_label.grid()
register_username_label.place(x = 50, y = 300)
register_password_label = Label(signup_window, text = "Password :", font = ("16"))
register_password_label.grid()
register_password_label.place(x = 50, y = 350)
register_confirm_password_label = Label(signup_window, text = "Confirm Password :", font = ("16"))
register_confirm_password_label.grid()
register_confirm_password_label.place(x = 50, y = 400)


#Variables
username_store = StringVar()
password_store = StringVar()
cpassword_store = StringVar()
register_username_entry = Entry(signup_window, font = ("16"), textvariable = username_store)
register_username_entry.grid()
register_username_entry.place(x = 300, y = 300)
register_password_entry = Entry(signup_window, font = ("16"), show = "*", textvariable = password_store)
register_password_entry.grid()
register_password_entry.place(x = 300, y = 350)
register_conform_password_entry = Entry(signup_window, font = ("16"), show = "*", textvariable = cpassword_store)
register_conform_password_entry.grid()
register_conform_password_entry.place(x = 300, y = 400)

register_button = Button(signup_window, text = "Register", font = ("16"), command = register)
register_button.grid()
register_button.place(x = 250, y = 500)


already_label = Label(signup_window, text = "Already have an account want to sign in.")
already_label.grid()
already_label.place(x = 200, y = 550)

already_button = Button(signup_window, text = "Login", font = ("10"), command = login)
already_button.grid()
already_button.place(x = 430, y = 540)
# photo.place(x = 20, y = 20)
signup_window.mainloop()











