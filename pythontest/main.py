



from Views.login_ui import Win as MainWin

from Controller.login_control import Controller as MainUIController

app = MainWin(MainUIController())                   #窗口控制器传递给UI

if __name__ == '__main__':
    app.mainloop()
