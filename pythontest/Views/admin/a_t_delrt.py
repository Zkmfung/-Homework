import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *


class WinGUI(Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_beginc = self.__tk_label_beginc(self)
        self.tk_input_begincity = self.__tk_input_begincity(self)
        self.tk_label_lyea9q29 = self.__tk_label_lyea9q29(self)
        self.tk_input_endcity = self.__tk_input_endcity(self)
        self.tk_label_lyeaakbu = self.__tk_label_lyeaakbu(self)
        self.tk_label_lyeaav5x = self.__tk_label_lyeaav5x(self)
        self.tk_label_lyeab11c = self.__tk_label_lyeab11c(self)
        self.tk_button_add = self.__tk_button_add(self)
        self.tk_input_begintime = self.__tk_input_begintime(self)
        self.tk_input_endtime = self.__tk_input_endtime(self)
        self.tk_input_price = self.__tk_input_price(self)
        self.tk_button_lyeafn17 = self.__tk_button_lyeafn17(self)

    def __win(self):
        self.title("城市交通咨询系统（管理员）")
        # 设置窗口大小、居中
        width = 463
        height = 332
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

    def __tk_label_beginc(self, parent):
        label = Label(parent, text="出发城市", anchor="center", bootstyle="default")
        label.place(relx=0.2333, rely=0.0392, relwidth=0.1080, relheight=0.0904)
        return label

    def __tk_input_begincity(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(relx=0.4298, rely=0.0392, relwidth=0.3240, relheight=0.0904)
        return ipt

    def __tk_label_lyea9q29(self, parent):
        label = Label(parent, text="到达城市", anchor="center", bootstyle="default")
        label.place(relx=0.2333, rely=0.1687, relwidth=0.1080, relheight=0.0904)
        return label

    def __tk_input_endcity(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(relx=0.4298, rely=0.1687, relwidth=0.3240, relheight=0.0904)
        return ipt

    def __tk_label_lyeaakbu(self, parent):
        label = Label(parent, text="出发时间", anchor="center", bootstyle="default")
        label.place(relx=0.2333, rely=0.2892, relwidth=0.1080, relheight=0.0904)
        return label

    def __tk_label_lyeaav5x(self, parent):
        label = Label(parent, text="到达时间", anchor="center", bootstyle="default")
        label.place(relx=0.2333, rely=0.4187, relwidth=0.1080, relheight=0.0904)
        return label

    def __tk_label_lyeab11c(self, parent):
        label = Label(parent, text="价格", anchor="center", bootstyle="default")
        label.place(relx=0.2354, rely=0.5602, relwidth=0.1080, relheight=0.0904)
        return label

    def __tk_button_add(self, parent):
        btn = Button(parent, text="删除", takefocus=False, bootstyle="default")
        btn.place(relx=0.4471, rely=0.6988, relwidth=0.1080, relheight=0.0904)
        return btn

    def __tk_input_begintime(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(relx=0.4298, rely=0.2892, relwidth=0.3240, relheight=0.0904)
        return ipt

    def __tk_input_endtime(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(relx=0.4298, rely=0.4187, relwidth=0.3240, relheight=0.0904)
        return ipt

    def __tk_input_price(self, parent):
        ipt = Entry(parent, bootstyle="default")
        ipt.place(relx=0.4298, rely=0.5602, relwidth=0.3240, relheight=0.0904)
        return ipt

    def __tk_button_lyeafn17(self, parent):
        btn = Button(parent, text="返回上一页", takefocus=False, bootstyle="default")
        btn.place(relx=0.3996, rely=0.8193, relwidth=0.2030, relheight=0.0904)
        return btn


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        self.tk_button_add.bind('<Button>', self.ctl.delrt)
        self.tk_button_lyeafn17.bind('<Button>', self.ctl.bk)
        pass

    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_beginc), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lyea9q29), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lyeaakbu), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lyeaav5x), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_label_lyeab11c), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_add), font=("微软雅黑", -12))
        sty.configure(self.new_style(self.tk_button_lyeafn17), font=("微软雅黑", -12))
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()