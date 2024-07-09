from Views.admin.a_v_t_clk import Win as viewpclk_Win
from Controller.admin.a_v_p_clk_ctl import Controller as viewpclk_Controller
from Views.admin.a_v_p_pl import Win as viewppl_Win
from Controller.admin.a_v_p_pl_ctl import Controller as viewppl_Controller
from Views.admin.a_p_addrt import Win as addrt_Win
from Controller.admin.a_p_addrt_ctl import Controller as addrt_Controller
from Views.admin.a_p_delrt import Win as delrt_Win
from Controller.admin.a_p_delrt_ctl import Controller as delrt_Controller

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

    def view_p_clk(self, evt):
        print("view_p_clk:", evt)
        v_p_clk_ui = viewpclk_Win(viewpclk_Controller())
        v_p_clk_ui.mainloop()

    def view_p_pl(self, evt):
        print("view_p_pl:", evt)
        v_p_pl_ui = viewppl_Win(viewppl_Controller(city_ui=self.ui))
        v_p_pl_ui.mainloop()

    def ad_p_rt(self, evt):
        print("add_p_rt:", evt)
        a_addrt = addrt_Win(addrt_Controller())
        a_addrt.mainloop()
    def bk_to_p(self, evt):
        print("返回:", evt)
        self.ui.destroy()

    def del_p_rt(self, evt):
        print("<Button>事件未处理:", evt)
        a_delrt = delrt_Win(delrt_Controller())
        a_delrt.mainloop()
