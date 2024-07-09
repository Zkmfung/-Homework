import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *
#from shared_data import   """ 时刻表元组 """

class WinGUI(Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_return_to_mm = self.__tk_button_return_to_mm(self)
        self.tk_label_frame_vt = self.__tk_label_frame_vt(self)
        self.tk_table_listCity = self.__tk_table_listCity(self.tk_label_frame_vt)

    def __win(self):
        self.title("城市交通咨询系统（管理员）")
        # 设置窗口大小、居中
        width = 603
        height = 299
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.minsize(width=width, height=height)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def new_style(self, widget):
        ctl = widget.cget('style')
        ctl = "".join(random.sample('0123456789', 5)) + "." + ctl
        widget.configure(style=ctl)
        return ctl

    def __tk_button_return_to_mm(self, parent):
        btn = Button(parent, text="返回上一页", takefocus=False, bootstyle="default")
        btn.place(relx=0.4295, rely=0.8328, relwidth=0.1426, relheight=0.1003)
        return btn

    def __tk_label_frame_vt(self, parent):
        frame = LabelFrame(parent, text="城市列表", bootstyle="default")
        frame.place(relx=0.0000, rely=0.0000, relwidth=0.9934, relheight=0.7391)
        return frame

    def __tk_table_listCity(self, parent):
        # 表头字段 表头宽度
        columns = {"num": 109, "出发城市": 109, "到达城市": 109, "时刻": 218}
        tk_table = Treeview(parent, show="headings", columns=list(columns), bootstyle="light")
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        """
        for item in 
        """


        tk_table.place(relx=0.0451, rely=0.0679, relwidth=0.9115, relheight=0.7330)
        self.create_bar(parent, tk_table, True, False, 27, 15, 546, 162, 599, 221)
        return tk_table


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_return_to_mm.bind('<Button>', self.ctl.bk_to_train)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_button_return_to_mm), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()