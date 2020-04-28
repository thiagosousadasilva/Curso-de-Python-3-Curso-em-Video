# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
import pygame
print("=========== desafio 021 ============")
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Exerc021.mp3')
pygame.mixer.music.play()
pygame.event.wait()