import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *


class WinGUI(Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_return_to_mm = self.__tk_button_return_to_mm(self)
        self.tk_input_begincity = self.__tk_input_begincity(self)
        self.tk_label_lyecezkk = self.__tk_label_lyecezkk(self)
        self.tk_label_lyecf5bz = self.__tk_label_lyecf5bz(self)
        self.tk_input_endcity = self.__tk_input_endcity(self)
        self.tk_button_leasttime = self.__tk_button_leasttime(self)
        self.tk_button_leastprice = self.__tk_button_leastprice(self)

    def __win(self):
        self.title("城市交通咨询系统（用户）")
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

    def __tk_input_begincity(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(relx=0.4743, rely=0.1271, relwidth=0.2488, relheight=0.1003)
        return ipt

    def __tk_label_lyecezkk(self, parent):
        label = Label(parent, text="出发城市", anchor="center", bootstyle="default")
        label.place(relx=0.3118, rely=0.1271, relwidth=0.0829, relheight=0.1003)
        return label

    def __tk_label_lyecf5bz(self, parent):
        label = Label(parent, text="到达城市", anchor="center", bootstyle="default")
        label.place(relx=0.3118, rely=0.2910, relwidth=0.0829, relheight=0.1003)
        return label

    def __tk_input_endcity(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(relx=0.4743, rely=0.2910, relwidth=0.2488, relheight=0.1003)
        return ipt

    def __tk_button_leasttime(self, parent):
        btn = Button(parent, text="最短时间", takefocus=False, bootstyle="default")
        btn.place(relx=0.2703, rely=0.5686, relwidth=0.1559, relheight=0.1003)
        return btn

    def __tk_button_leastprice(self, parent):
        btn = Button(parent, text="最低价格", takefocus=False, bootstyle="default")
        btn.place(relx=0.5887, rely=0.5686, relwidth=0.1559, relheight=0.1003)
        return btn


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_return_to_mm.bind('<Button>', self.ctl.bk)
        self.tk_button_leasttime.bind('<Button>', self.ctl.leasttime)
        self.tk_button_leastprice.bind('<Button>', self.ctl.leastprice)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_button_return_to_mm), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lyecezkk), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lyecf5bz), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_leasttime), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_leastprice), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()