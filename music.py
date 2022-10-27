#Import modules.
import pygame
import time
from colorama import Fore, Style

#Init pygame mixer.
pygame.init()

#Plays 'main game' music.
def play_main_game_music():
    pygame.mixer.music.load("music_assets/main_music_theme.mp3")
    pygame.mixer.music.play(-1) #Loops music infinitely "-1".

#Plays 'title screen' music.
def play_title_screen_music():
    pygame.mixer.music.load("music_assets/title_music.mp3")
    pygame.mixer.music.play()

#Plays the 'click' sound.
def play_click_music():
    pygame.mixer.music.load("music_assets/confirm_sound.mp3")
    pygame.mixer.music.play()

#Plays the 'boss' music.
def play_boss_music():
    pygame.mixer.music.load("music_assets/boss_music.mp3")
    pygame.mixer.music.play(-1) #Loops music infinitely "-1".

#Plays the 'victory' music.
def play_ending_music():
    pygame.mixer.music.load("music_assets/ending_music.mp3")
    pygame.mixer.music.play(-1)
    
def play_good_ending():
    pygame.mixer.music.load("music_assets/good_ending.mp3")
    pygame.mixer.music.play(-1)