import time
import tkinter as tk
import pygame

pygame.mixer.init()
pygame.mixer.music.load("mrs_m.mp3")

# timestamps
lyrics = [
    (30.5, "mrs. magic to and fro"),
    (37.5, "please give me one last show"),
    (45, "loosen my mind from within"),
    (52.5, "before it starts to wear and thin"),
    (60.5, "i don't know :("),
    (64, "i don't know what i'm doing here."),
    (75, "i don't know :("),
    (78.5, "i don't know what i'm doing here."),
    (95.5, "mrs. magic radio"),
    (103, "give me one last chance to show"),
    (110, "tell you what lurks deep inside"),
    (117.5, "deep inside my battered mind"),
    (125.5, "i don't know :("),
    (129, "i don't know what i'm doing here."),
    (139.5, "i don't know :("),
    (144.5, "i don't know what i'm doing here."),
    (155.5, "leaving me outside"),
    (160.5, "no, i can't get back in"),
    (164, "no, i can't get back in"),
    (170, "leaving me outside"),
    (175, "no, i can't get back in"),
    (179, "no, i can't get back in, ooh"),
    (190, "mrs. magic to and fro"),
    (195.5, "just let me"),
    (197.5, "be myself"),
]

box_width, box_height = 350, 260
font = ("Helvetica", 25, "italic")
bg_color = "#AE3A70"
fg_color = "#FFFFFF"
speed = 60

class lyric_card:
    def __init__(self, parent, text, x, y):
        self.win = tk.Toplevel(parent)
        self.win.overrideredirect(True)
        self.win.configure(bg=bg_color)
        self.win.geometry(f"{box_width}x{box_height}+{int(x)}+{int(y)}")

        self.full_text = text
        self.label = tk.Label(
            self.win, 
            text="",
            font=font,
            bg=bg_color,
            fg=fg_color,
            wraplength=box_width - 40,
            justify="center",
        )
        self.label.pack(expand=True, fill="both")

        self.x = x
        self.y = float(y)
        self.typewriter_index = 0
        self.typewriter()

        self.win.attributes("-topmost", True)
        self.win.update()

    def typewriter(self):
        if self.typewriter_index <= len(self.full_text):
            self.label.config(text=self.full_text[: self.typewriter_index])
            self.typewriter_index += 1
            self.win.after(60, self.typewriter)

    def rise(self, dy):
        self.y -= dy
        self.win.geometry(f"{box_width}x{box_height}+{int(self.x)}+{int(self.y)}")

class lyricfloatapp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1x1+0+0")
        self.root.attributes("-alpha", 0.0)

        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()

        self.next_lyric_idx = 0
        self.cards = []
        self.last_frame_time = None
        self.current_side = "left"

        pygame.mixer.music.play()
        self.start_time = time.time()
        self.update_loop()

    def get_x_position(self):
        if self.current_side == "left":
            self.current_side = "right"
            return self.screen_w // 6
        else:
            self.current_side = "left"
            return (self.screen_w // 2)

    def update_loop(self):
        now = time.time()
        elapsed = now - self.start_time

        if self.next_lyric_idx < len(lyrics):
            t, text = lyrics[self.next_lyric_idx]
            if elapsed >= t:
                x = self.get_x_position()
                y = self.screen_h - box_height - 100
                card = lyric_card(self.root, text, x, y)
                self.cards.append(card)
                self.next_lyric_idx += 1
        if self.last_frame_time:
            dt = now - self.last_frame_time
            dy = speed * dt
            for card in self.cards:
                card.rise(dy)
        self.last_frame_time = now
        self.root.after(20, self.update_loop)


if __name__ == "__main__":
    root = tk.Tk()
    app = lyricfloatapp(root)
    root.mainloop()