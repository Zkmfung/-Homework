from Views.admin.a_city import Win as a_city_Win
from Controller.admin.a_city_control import Controller as a_city_Controller
from Views.admin.a_train import Win as a_train_Win
from Controller.admin.a_train_control import Controller as a_train_Controller
from Views.admin.a_plane import Win as a_plane_Win
from Controller.admin.a_plane_ctl import Controller as a_plane_Controller


class Controller:

    ui: a_city_Win
    params: {}
    def __init__(self,**kwargs):
        self.params = kwargs
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    def city(self, evt):
        print("city:", evt)
        a_City_info = a_city_Win(a_city_Controller(a_info = self.ui))
        a_City_info.mainloop()


    def train(self, evt):
        print("train:", evt)
        a_Train_info = a_train_Win(a_train_Controller(a_info=self.ui))
        a_Train_info.mainloop()
    def plane(self, evt):
        print("plane:", evt)
        a_plane_info = a_plane_Win(a_plane_Controller(a_info=self.ui))
        a_plane_info.mainloop()
    def mainmenu(self, evt):
        print("mm:", evt)
        self.ui.destroy()
