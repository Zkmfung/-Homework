
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
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

    def train(self, evt):
        print("train:", evt)

    def plane(self, evt):
        print("plane:", evt)

    def mainmenu(self, evt):
        print("mm:", evt)
        self.params["login_ui"].deiconify
        self.ui.destroy()
