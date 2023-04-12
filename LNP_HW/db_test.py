from tkinter import Tk, Label, Button, Entry, Frame
from tkinter.ttk import Notebook, Combobox
from tkinter.ttk import Treeview, Scrollbar
import pymysql
from pymysql.cursors import DictCursor


class example:

    def __init__(self):
        self.window = Tk()
        self.window.title("데이터베이스 전략과 실습")
        self.window.geometry("1000x600")
        self.setTabs()
        self.setLabels()
        self.setEntry()
        self.setButton()
        self.setCombobox()
        self.setButton2()
        self.setTreeview()
        self.c = {
            "host":"localhost",
            "port":3307,
            "user":"root",
            "password":"1234",
            "db":"test",
            "charset":"utf8",
            "cursorclass": DictCursor
        }
        self.setTreeviewValues()
        self.set_Entry23_Button3()
        self.setScrollbar()

        self.window.mainloop()
    def setTabs(self):
        self.notebook = Notebook(self.window, width=1000, height=1000)
        self.notebook.pack()
        self.tab1 = Frame(self.window)
        self.tab2 = Frame(self.window)
        self.notebook.add(self.tab1, text="tab1 입니다.")
        self.notebook.add(self.tab2, text="tab2 입니다.")

    def setLabels(self):
        self.label1 = Label(self.tab1, text="위치 x100 y100")
        self.label1.place(x=100, y=100)

        self.label2 = Label(self.tab1, text="위치 x100 y200")
        self.label2.place(x=100, y=200)

        Label(self.tab1, text="위치 x400 y100").place(x=400, y=100)

        Label(self.tab1, text="위치 x400 y200").place(x=400, y=200)

        self.label3 = Label(self.tab1, text="변경할 라벨")
        self.label3.place(x=400, y=300)

    def setEntry(self):
        self.entry1 = Entry(self.tab1)
        self.entry1.place(x=100, y=300, width=170, height=30)

    def setButton(self):
        self.button1 = Button(self.tab1, text="변경", command=self.change)
        self.button1.place(x=300, y=300)

    def change(self):
        self.label3['text'] = self.entry1.get()

    def setCombobox(self):
        self.combobox1 = Combobox(self.tab1, height=15, values=['1번', '2번', '3번', '4번'])
        self.combobox1.place(x=100, y=400, width=100, height=30)
        self.combobox1.set("몇번?")

    def setButton2(self):
        self.button2 = Button(self.tab1, text="변경2", command=self.change2)
        self.button2.place(x=300, y=400)

    def change2(self):
        self.label3['text'] = self.combobox1.get()

    def setTreeview(self):
        self.treeview1 = Treeview(self.tab2, columns=["ID", "NAME", "AGE"], show="headings")
        self.treeview1.place(x=50, y=50, width=610, height=190)

        self.treeview1.column("ID", anchor='center')
        self.treeview1.column("NAME", anchor='center')
        self.treeview1.column("AGE", anchor='center')

        self.treeview1.heading("ID", text="번호")
        self.treeview1.heading("NAME", text="이름")
        self.treeview1.heading("AGE", text="나이")

    def setTreeviewValues(self):
        self.treeview1.delete(*self.treeview1.get_children())

        db_conn = pymysql.connect(**self.c)
        sql = "SELECT * FROM table1"
        with db_conn:
            with db_conn.cursor() as cur:
                cur.execute(sql)
                result = cur.fetchall()
                for data in result:
                    self.treeview1.insert(parent="", index='end', text="",
                                          values=(data["id"], data["name"], data["age"]), iid=data)

    def set_Entry23_Button3(self):
        self.entry2 = Entry(self.tab2)
        self.label_e2 = Label(self.tab2, text="name")
        self.entry2.place(x=300, y=300, width=100, height=30)
        self.label_e2.place(x=250, y=300)
        self.entry3 = Entry(self.tab2)
        self.label_e3 = Label(self.tab2, text="id")
        self.label_e3.place(x=450, y=300)
        self.entry3.place(x=500, y=300, width=100, height=30)

        self.button3 = Button(self.tab2, text="추가", command=self.insertValues)
        self.button3.place(x=750, y=300)

    def insertValues(self):
        sql = f"insert into table1 (name, age) values ('{self.entry2.get()}',{self.entry3.get()})"
        db_conn = pymysql.connect(**self.c)
        with db_conn:
            with db_conn.cursor() as cur:
                cur.execute(sql)
                db_conn.commit()
        self.setTreeviewValues()

    def setScrollbar(self):
        vsb = Scrollbar(self.tab2, orient="vertical", command=self.treeview1.yview)
        vsb.place(x=700, y=55, height=200)
        self.treeview1.configure(yscrollcommand=vsb.set)


e=example()

