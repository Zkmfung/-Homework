
from tkinter import messagebox
from Views.login_ui import Win
from Views.admin_info_ui import Win as a_info_Win
from Controller.admin_info_control import Controller as a_info_Controller
from Views.user_info_ui import Win as u_info_Win
from Controller.user_info_control import Controller as u_info_Controller
class Controller:

    ui: object

    def __init__(self):
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    def admin_login(self, evt):
        print("登录成功！", evt)
        a_info = a_info_Win(a_info_Controller(login_ui = self.ui))
        a_info.mainloop()
        self.ui.withdraw()
    def user_login(self, evt):
        print("你好", evt)
        u_info = u_info_Win(u_info_Controller(login_ui = self.ui))
        u_info.mainloop()
        self.ui.withdraw()

