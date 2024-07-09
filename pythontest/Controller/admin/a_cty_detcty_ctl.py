class Controller:
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

    def deleteC(self, evt):
        print("<Button>事件未处理:", evt)

    def back_ti_acty(self, evt):
        print("back:", evt)
        self.ui.destroy()
