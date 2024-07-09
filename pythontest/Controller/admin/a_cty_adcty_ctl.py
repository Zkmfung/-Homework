from shared_data import add_city
from Views.admin.a_cty_addcty import Win
class Controller:
    ui: Win

    params: {}

    def __init__(self, **kwargs):
        self.params = kwargs
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    def addC(self, evt):
        print("addCity:", evt)
        cityname = self.ui.tk_input_lye5lfdi.get()
        add_city(cityname)


    def back_ti_acty(self, evt):
        print("back:", evt)
        self.ui.destroy()
