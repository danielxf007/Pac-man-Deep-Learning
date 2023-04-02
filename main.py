import sys
import retro
from PyQt5.QtWidgets import QApplication
from graphics.main_window import MainWindow
from graphics.game_window import GameWindow

if __name__ == '__main__':
    env = retro.make(game='PacManNamco-Nes')
    screen = env.reset()
    app = QApplication(sys.argv)
    main_window = MainWindow((150, 150), (1100, 700), 'Pac-man')
    game_window = GameWindow(main_window, (500, 50), (512, 480))
    game_window.setScreen(screen)
    main_window.addChild(game_window)
    sys.exit(app.exec())
