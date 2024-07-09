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
        print("<Button>事件未处理:", evt)

    def view_t_pricelist(self, evt):
        print("<Button>事件未处理:", evt)

    def add_t_rot(self, evt):
        print("<Button>事件未处理:", evt)

    def bk_t_adm(self, evt):
        print("返回:", evt)
        self.ui.destroy()

    def delete_t_rot(self, evt):
        print("<Button>事件未处理:", evt)
