from Views.admin.viewCity import Win as viewCity_Win
from Controller.admin.viewCity_control import Controller as viewCity_Controller
from Views.user.v_p_clk_pl import Win as vpclk_Win
from Controller.user.v_p_clk_pl_ctl import Controller as vpclk_Controller
from Views.user.v_t_clk_pl import Win as vtclk_Win
from Controller.user.v_t_clk_pl_clk import Controller as vtclk_Controller
from Views.user.v_p_rt import Win as vprt_Win
from Controller.user.v_p_rt_ctl import Controller as vprt_Controller
from Views.user.v_t_rt import Win as vtrt_Win
from Controller.user.v_t_rt_ctl import Controller as vtrt_Controller

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

    def u_viewCity(self, evt):
        print("viewcity:", evt)
        v_city_ui = viewCity_Win(viewCity_Controller())
        v_city_ui.mainloop()

    def view_train_list(self, evt):
        print("view_train_list:", evt)
        v_t_ui = vtclk_Win(vtclk_Controller())
        v_t_ui.mainloop()
    def view_plane_list(self, evt):
        print("view_plane_list:", evt)
        v_p_ui = vpclk_Win(vpclk_Controller())
        v_p_ui.mainloop()

    def view_train_rt(self, evt):
        print("view_train_rt:", evt)
        v_trt_ui = vtrt_Win(vtrt_Controller())
        v_trt_ui.mainloop()
    def view_plane_rt(self, evt):
        print("view_plane_r:", evt)
        v_prt_ui = vprt_Win(vprt_Controller())
        v_prt_ui.mainloop()
    def mainmenu(self, evt):
        print("mm:", evt)
        self.ui.destroy()
