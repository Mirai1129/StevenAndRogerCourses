from tkinter import *
import random
import colorsys # 引入 colorsys 函式庫來轉換顏色

class Ball:
    # 移除了 color 參數，因為顏色會是動態變化的
    def __init__(self, canvas):
        self.canvas = canvas
        # 建立小球，初始顏色不重要，因為會馬上更新
        self.id = canvas.create_oval(10, 10, 25, 25, fill='red') 
        self.canvas.move(self.id, 245, 100)
        
        starts = [-100]
        self.x = random.choice(starts)
        self.y = -3
        
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
        # 新增一個屬性來追蹤目前的色相 (hue)
        self.hue = 0.0

    def update(self):
        # --- 1. 移動和反彈 (原本 draw 方法的邏輯) ---
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = self.x * -1
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.y  = self.y * -1
            
        # --- 2. 更新顏色為彩虹色 ---
        self.hue += 0.01  # 每次更新時，微調色相值 (數值越小，變化越慢)
        if self.hue >= 1.0:
            self.hue = 0.0 # 回到起點，形成循環

        # 將 HSV 顏色轉換為 Tkinter 的 16 進位色碼
        rgb_float = colorsys.hsv_to_rgb(self.hue, 1.0, 1.0)
        rgb_int = [int(c * 255) for c in rgb_float]
        hex_color = f'#{rgb_int[0]:02x}{rgb_int[1]:02x}{rgb_int[2]:02x}'
        
        # 使用 itemconfig 更新小球的顏色
        self.canvas.itemconfig(self.id, fill=hex_color)


# --- 主程式 ---
tk = Tk()
tk.title("彩虹反彈球")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=300, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update() # 確保 canvas 尺寸已就緒

# 建立 Ball 物件時不再需要傳入顏色
ball = Ball(canvas)

# 定義一個動畫循環函式
def game_loop():
    ball.update() # 呼叫 ball 的 update 方法來移動和變色
    tk.after(15, game_loop) # 告訴 Tkinter 在 15 毫秒後再次執行此函式

# 啟動動畫
game_loop()

# 進入 Tkinter 的主事件循環
tk.mainloop()