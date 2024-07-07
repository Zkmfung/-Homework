
from tkinter import messagebox
from Views.login_ui import Win
from Views.admin_info_ui import Win as a_info_Win
from Controller.admin_info_control import Controller as a_info_Controller
from Views.user_info_ui import Win as u_info_Win
from Controller.user_info_control import Controller as u_info_Controller
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
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
        a_info = a_info_Win(a_info_Controller())
        a_info.mainloop()
    def user_login(self, evt):
        print("你好", evt)
        u_info = u_info_Win(u_info_Controller())
        u_info.mainloop()