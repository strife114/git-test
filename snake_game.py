import tkinter as tk
import random


class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("贪吃蛇")
        self.window.resizable(False, False)

        # 游戏参数
        self.CELL = 20          # 每格像素大小
        self.COLS = 30          # 列数
        self.ROWS = 24          # 行数
        self.WIDTH = self.COLS * self.CELL
        self.HEIGHT = self.ROWS * self.CELL

        # 顶部信息栏
        self.info_frame = tk.Frame(self.window, height=40)
        self.info_frame.pack(fill=tk.X)
        self.info_frame.pack_propagate(False)

        self.score_label = tk.Label(
            self.info_frame, text="分数: 0",
            font=("Microsoft YaHei", 14, "bold"), fg="#333"
        )
        self.score_label.pack(side=tk.LEFT, padx=20)

        self.best_label = tk.Label(
            self.info_frame, text="最高分: 0",
            font=("Microsoft YaHei", 14), fg="#999"
        )
        self.best_label.pack(side=tk.RIGHT, padx=20)

        # 画布
        self.canvas = tk.Canvas(
            self.window, width=self.WIDTH, height=self.HEIGHT,
            bg="#1a1a2e", highlightthickness=0
        )
        self.canvas.pack()
        self.canvas.focus_set()

        # 底部控制栏
        self.ctrl_frame = tk.Frame(self.window, height=50)
        self.ctrl_frame.pack(fill=tk.X, pady=5)
        self.ctrl_frame.pack_propagate(False)

        self.status_label = tk.Label(
            self.ctrl_frame, text="按 空格键 开始 / 暂停",
            font=("Microsoft YaHei", 11), fg="#666"
        )
        self.status_label.pack(expand=True)

        # 绑定按键
        self.window.bind("<Up>", lambda e: self.change_dir("UP"))
        self.window.bind("<Down>", lambda e: self.change_dir("DOWN"))
        self.window.bind("<Left>", lambda e: self.change_dir("LEFT"))
        self.window.bind("<Right>", lambda e: self.change_dir("RIGHT"))
        self.window.bind("<space>", lambda e: self.toggle_pause())
        self.window.bind("<Return>", lambda e: self.restart())

        # w a s d 备选
        self.window.bind("w", lambda e: self.change_dir("UP"))
        self.window.bind("s", lambda e: self.change_dir("DOWN"))
        self.window.bind("a", lambda e: self.change_dir("LEFT"))
        self.window.bind("d", lambda e: self.change_dir("RIGHT"))

        self.init_game()
        self.draw_grid()
        self.draw_all()
        self.window.mainloop()

    def init_game(self):
        """初始化 / 重置游戏状态"""
        self.snake = [(self.COLS // 2, self.ROWS // 2)]
        self.direction = "RIGHT"
        self.next_dir = "RIGHT"
        self.food = None
        self.score = 0
        self.best_score = 0
        self.running = False
        self.game_over = False
        self.speed = 120          # 毫秒
        self.spawn_food()

    def spawn_food(self):
        """生成食物（避开蛇身）"""
        while True:
            fx = random.randint(1, self.COLS - 2)
            fy = random.randint(1, self.ROWS - 2)
            if (fx, fy) not in self.snake:
                self.food = (fx, fy)
                break

    def draw_grid(self):
        """绘制棋盘格背景"""
        for x in range(self.COLS):
            for y in range(self.ROWS):
                x1 = x * self.CELL
                y1 = y * self.CELL
                color = "#16213e" if (x + y) % 2 == 0 else "#1a1a2e"
                self.canvas.create_rectangle(
                    x1, y1, x1 + self.CELL, y1 + self.CELL,
                    fill=color, outline="", tags="grid"
                )

    def draw_all(self):
        """绘制蛇和食物"""
        self.canvas.delete("snake", "food")

        # 画蛇身
        for i, (sx, sy) in enumerate(self.snake):
            x1 = sx * self.CELL + 1
            y1 = sy * self.CELL + 1
            x2 = x1 + self.CELL - 2
            y2 = y1 + self.CELL - 2
            if i == 0:
                color = "#e94560"   # 蛇头
            else:
                # 渐变绿
                ratio = i / max(len(self.snake) - 1, 1)
                g = int(180 + 60 * (1 - ratio))
                color = f"#{0:02x}{g:02x}{60:02x}"
            self.canvas.create_rectangle(
                x1, y1, x2, y2, fill=color,
                outline="", tags="snake"
            )

        # 画食物
        if self.food:
            fx, fy = self.food
            x1 = fx * self.CELL + 3
            y1 = fy * self.CELL + 3
            x2 = x1 + self.CELL - 6
            y2 = y1 + self.CELL - 6
            self.canvas.create_oval(
                x1, y1, x2, y2,
                fill="#f5c518", outline="", tags="food"
            )

    def change_dir(self, new_dir):
        """改变方向（不能反向）"""
        if not self.running or self.game_over:
            return
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if opposites.get(new_dir) != self.direction:
            self.next_dir = new_dir

    def toggle_pause(self):
        """空格暂停 / 开始"""
        if self.game_over:
            self.restart()
        else:
            self.running = not self.running
            if self.running:
                self.status_label.config(text="游戏中...  空格暂停  ↑↓←→ 移动")
                self.game_loop()
            else:
                self.status_label.config(text="已暂停  按 空格键 继续")

    def restart(self):
        """重新开始"""
        self.init_game()
        self.draw_all()
        self.score_label.config(text="分数: 0")
        self.running = True
        self.game_over = False
        self.status_label.config(text="游戏中...  空格暂停  ↑↓←→ 移动")
        self.game_loop()

    def game_loop(self):
        """主循环"""
        if not self.running or self.game_over:
            return

        self.direction = self.next_dir
        head_x, head_y = self.snake[0]
        dx, dy = {"UP": (0, -1), "DOWN": (0, 1),
                  "LEFT": (-1, 0), "RIGHT": (1, 0)}[self.direction]
        new_head = (head_x + dx, head_y + dy)

        # 碰墙检测
        if not (0 <= new_head[0] < self.COLS and 0 <= new_head[1] < self.ROWS):
            self.end_game()
            return

        # 碰自己检测
        if new_head in self.snake:
            self.end_game()
            return

        self.snake.insert(0, new_head)

        # 吃到食物
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"分数: {self.score}")
            if self.score > self.best_score:
                self.best_score = self.score
                self.best_label.config(text=f"最高分: {self.best_score}")
            self.spawn_food()
            # 加速
            if self.speed > 60:
                self.speed = max(60, self.speed - 2)
        else:
            self.snake.pop()

        self.draw_all()
        self.window.after(self.speed, self.game_loop)

    def end_game(self):
        """游戏结束"""
        self.running = False
        self.game_over = True
        self.status_label.config(
            text=f"游戏结束！得分: {self.score}  按 回车键 重新开始"
        )

        # 蛇头变灰
        if self.snake:
            sx, sy = self.snake[0]
            x1 = sx * self.CELL + 1
            y1 = sy * self.CELL + 1
            self.canvas.create_rectangle(
                x1, y1, x1 + self.CELL - 2, y1 + self.CELL - 2,
                fill="#888", outline="", tags="snake"
            )


if __name__ == "__main__":
    SnakeGame()
