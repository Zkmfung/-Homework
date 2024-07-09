from Views.admin.a_cty_detcty import Win
from shared_data import delete_city
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

    def deleteC(self, evt):
        print("deletecity:", evt)
        ctyname = self.ui.tk_input_lye5lfdi.get()
        delete_city(ctyname)


    def back_ti_acty(self, evt):
        print("back:", evt)
        self.ui.destroy()
