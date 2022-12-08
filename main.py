from dino_runner.components.game import Game
import pygame

if __name__ == "__main__":    
     game = Game()
     death_count = 0
     while game.runing:     #mientras el juego se esta ejecutando
          if not game.playing:     #si no estamos jugando mostramos el menu
               game.show_menu()
