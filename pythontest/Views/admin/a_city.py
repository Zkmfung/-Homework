import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *


class WinGUI(Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_Viewcity = self.__tk_button_Viewcity(self)
        self.tk_button_Addcity = self.__tk_button_Addcity(self)
        self.tk_button_Deletecity = self.__tk_button_Deletecity(self)
        self.tk_button_return_to_mm = self.__tk_button_return_to_mm(self)

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

    def __tk_button_Viewcity(self, parent):
        btn = Button(parent, text="查看城市", takefocus=False, bootstyle="default outline")
        btn.place(relx=0.4063, rely=0.1371, relwidth=0.1891, relheight=0.1405)
        return btn

    def __tk_button_Addcity(self, parent):
        btn = Button(parent, text="添加城市", takefocus=False, bootstyle="default outline")
        btn.place(relx=0.4063, rely=0.3645, relwidth=0.1891, relheight=0.1405)
        return btn

    def __tk_button_Deletecity(self, parent):
        btn = Button(parent, text="删除城市", takefocus=False, bootstyle="default outline")
        btn.place(relx=0.4063, rely=0.6087, relwidth=0.1891, relheight=0.1405)
        return btn

    def __tk_button_return_to_mm(self, parent):
        btn = Button(parent, text="返回上一页", takefocus=False, bootstyle="default")
        btn.place(relx=0.4295, rely=0.8328, relwidth=0.1426, relheight=0.1003)
        return btn


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_Viewcity.bind('<Button>', self.ctl.view_city)
        self.tk_button_Addcity.bind('<Button>', self.ctl.addCity)
        self.tk_button_Deletecity.bind('<Button>', self.ctl.deleteCity)
        self.tk_button_return_to_mm.bind('<Button>', self.ctl.bk_t_adm)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_button_Viewcity), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_Addcity), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_Deletecity), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_return_to_mm), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()