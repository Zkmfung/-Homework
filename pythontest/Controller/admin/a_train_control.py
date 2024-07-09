from Views.admin.a_v_t_clk import Win as viewtclk_Win
from Controller.admin.a_v_t_clk_ctl import Controller as viewtclk_Controller
from Views.admin.a_v_t_pl import Win as viewtpl_Win
from Controller.admin.a_v_t_pl_ctl import Controller as viewtpl_Controller
from Views.admin.a_t_addrt import Win as addrt_Win
from Controller.admin.a_t_addrt_clt import Controller as addrt_Controller
from Views.admin.a_t_delrt import Win as delrt_Win
from Controller.admin.a_t_delrt_clt import Controller as delrt_Controller


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object

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

    def view_t_clk(self, evt):
        print("view_t_clk:", evt)
        v_t_clk_ui = viewtclk_Win(viewtclk_Controller(city_ui=self.ui))
        v_t_clk_ui.mainloop()

    def view_t_pricelist(self, evt):
        print("view_t_pricelist:", evt)
        v_t_pl_ui = viewtpl_Win(viewtpl_Controller(city_ui=self.ui))
        v_t_pl_ui.mainloop()

    def add_t_rot(self, evt):
        print("add_t_rot:", evt)
        a_addrt = addrt_Win(addrt_Controller())
        a_addrt.mainloop()

    def bk_t_adm(self, evt):
        print("返回:", evt)
        self.ui.destroy()

    def delete_t_rot(self, evt):
        print("delete_t_rot:", evt)
        a_delrt = delrt_Win(delrt_Controller())
        a_delrt.mainloop()
