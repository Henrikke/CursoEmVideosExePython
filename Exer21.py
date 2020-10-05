"""
    algoritmo reproduz uma musica mp3 da biblioteca do pygame
"""
import pygame

pygame.init()
pygame.mixer.music.load('toca.mp3')
pygame.mixer.music.play()
pygame.event.wait()

