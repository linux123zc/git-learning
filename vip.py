from tkinter import *
import webbrowser


class Application(Tk):
    def __init__(self):
        super().__init__()

        # 设置窗口
        self.title('VIP 视频解析器')
        self.geometry('400x200')
        self.init_widgets()

        # 变量
        self.lines = {
            "线路1": "https://okjx.cc/?url={}",
            "线路2": "https://jx.618g.com/?url={}",
            "线路3": "https://z1.m1907.cn/?jx={}",
            "线路4": "https://jx.ab33.top/vip/?url={}",
            "线路5": "https://api.653520.top/vip/?url=",
            "线路6": "https://jx.000180.top/jx/?url={}",
            "线路7": "https://jx.km58.top/58ds/?url={}",
            "线路8": "https://www.1717yun.com/jx/ty.php?url={}"
        }
        self.now_line = "线路1"
        self.now_line_number = 1

    def init_widgets(self):
        label = Label(self, text='请输入 VIP 视频的链接：', font=('微软雅黑', 14))
        label.place(relx=0.2, rely=0.113, relwidth=0.563, relheight=0.117)

        self.url_entry = Entry(self, font=('微软雅黑', 12))
        self.url_entry.place(relx=0.22, rely=0.3, relwidth=0.763, relheight=0.174)

        self.line_var = StringVar(value='线路1')
        line_button = Button(self, textvariable=self.line_var, command=self.switch_line)
        line_button.place(relx=0.02, rely=0.3, relwidth=0.183, relheight=0.169)

        play_button = Button(self, text='播放', command=self.play_video)
        play_button.place(relx=0.32, rely=0.601, relwidth=0.263, relheight=0.23)

    def switch_line(self):
        line_list = list(self.lines.keys())
        self.now_line_number += 1
        if self.now_line_number >= len(line_list):
            self.now_line_number = 0
        else:
            pass
        # self.now_line_number = 0 if self.now_line_number >= len(line_list) else self.now_line_number

        self.now_line = line_list[self.now_line_number-1]
        self.line_var.set(self.now_line)

    def play_video(self):
        video_url = self.lines[self.now_line].format(self.url_entry.get())

        webbrowser.open(video_url)


if __name__ == "__main__":
    app = Application()
    app.mainloop()

