import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *


class WinGUI(Window):
    def __init__(self):
        super().__init__(themename="cosmo", hdpi=False)
        self.__win()
        self.tk_button_adminlogin = self.__tk_button_adminlogin(self)
        self.tk_button_userlogin = self.__tk_button_userlogin(self)

    def __win(self):
        self.title("城市交通资讯系统")
        # 设置窗口大小、居中
        width = 527
        height = 212
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

    def __tk_button_adminlogin(self, parent):
        btn = Button(parent, text="管理员登录", takefocus=False, bootstyle="default outline")
        btn.place(relx=0.3264, rely=0.2075, relwidth=0.3491, relheight=0.1981)
        return btn

    def __tk_button_userlogin(self, parent):
        btn = Button(parent, text="用户登录", takefocus=False, bootstyle="default outline")
        btn.place(relx=0.3264, rely=0.5849, relwidth=0.3491, relheight=0.1981)
        return btn


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_adminlogin.bind('<Button>', self.ctl.admin_login)
        self.tk_button_userlogin.bind('<Button>', self.ctl.user_login)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_button_adminlogin), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_userlogin), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
