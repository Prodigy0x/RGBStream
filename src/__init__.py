from typing import List, Tuple
import math
import time

class Rainbow:
    def __init__(self, frequency: float = 0.1) -> None:
        self.frequency = frequency

    def _calrgb(self, index: int, s: float) -> Tuple[int, int, int]:
        r = math.sin(self.frequency * index + s) * 127 + 128
        g = math.sin(self.frequency * index + 2 * math.pi / 3 + s) * 127 + 128
        b = math.sin(self.frequency * index + 4 * math.pi / 3 + s) * 127 + 128
        return int(r), int(g), int(b)

    def colorize(self, text: str) -> str:
        c: List[str] = []
        s: float = time.time() % (2 * math.pi)

        for index, char in enumerate(text):
            r, g, b = self._calrgb(index, s)
            c.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")

        return "".join(c)

    def animate(self, text: str, interval: float = 0.1) -> None:
        try:
            while True:
                print(self.colorize(text), end="\r", flush=True)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nStopped.")

    def Print(self, text: str) -> None:
        print(self.colorize(text))  
