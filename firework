class Fireworks():
    is_show = False
    x, y = 0, 0
    vy = 0
    p_list = []
    color = [0, 0, 0]
    v = 0
 
    def __init__(self, x, y, vy, n=300, color=[0, 255, 0], v=10):
        self.x = x
        self.y = y
        self.vy = vy
        self.color = color
        self.v = v
        for i in range(n):
            self.p_list.append([random.random() * 2 * math.pi, 0, v * math.pow(random.random(), 1 / 3)])
 
    def again(self):
        self.is_show = True
        self.x = random.randint(WIN_W // 2 - 350, WIN_W // 2 + 350)
        self.y = random.randint(int(WIN_H / 2), int(WIN_H * 3 / 5))
        self.vy = -40 * (random.random() * 0.4 + 0.8) - self.vy * 0.2
        self.color = color_list[random.randint(0, len(color_list) - 1)].copy()
        n = len(self.p_list)
        self.p_list = []
        for i in range(n):
            self.p_list.append([random.random() * 2 * math.pi, 0, self.v * math.pow(random.random(), 1 / 3)])
 
    def run(self):
        global show_n
        for p in self.p_list:
            p[1] = p[1] + (random.random() * 0.6 + 0.7) * p[2]
            p[2] = p[2] * 0.97
            if p[2] < 1.2:
                self.color[0] *= 0.9999
                self.color[1] *= 0.9999
                self.color[2] *= 0.9999
 
            if max(self.color) < 10 or self.y>WIN_H+p[1]:
                show_n -= 1
                self.is_show = False
                break
        self.vy += 10 * t1
        self.y += self.vy * t1
