from Views.admin.viewCity import Win as viewCity_Win
from Controller.admin.viewCity_control import Controller as viewCity_Controller
from Views.admin.a_cty_addcty import Win as addcity_Win
from Controller.admin.a_cty_adcty_ctl import Controller as addcity_Controller
from Views.admin.a_cty_detcty import Win as delcity_Win
from Controller.admin.a_cty_detcty_ctl import Controller as delcity_Controller

class Controller:
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

    def view_city(self, evt):
        print("viewCity:", evt)
        v_city_ui = viewCity_Win(viewCity_Controller(city_ui=self.ui))
        v_city_ui.mainloop()

    def addCity(self, evt):
        print("addCity:", evt)
        addCity_info = addcity_Win(addcity_Controller(addc_info=self.ui))
        addCity_info.mainloop()

    def deleteCity(self, evt):
        print("deleteCity:", evt)
        delcity_info = delcity_Win(delcity_Controller(delc_info=self.ui))
        delcity_info.mainloop()
    def bk_t_adm(self, evt):
        print("返回:", evt)
        self.params["a_info"].deiconify
        self.ui.destroy()
