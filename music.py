#Import modules
import pygame
import time
from colorama import Fore, Style

#Init pygame mixer
pygame.init()

#Plays main game music.
def play_main_game_music():
    pygame.mixer.music.load("music_assets/main_theme.mp3")
    pygame.mixer.music.play()

#Plays title screen music.
def play_title_screen_music():
    pygame.mixer.music.load("music_assets/title_screen_music.mp3")
    pygame.mixer.music.play()

def play_click_music():
    pygame.mixer.music.load("music_assets/confirm_sound.mp3")
    pygame.mixer.music.play()

def play_defeat_music():
    pass

def play_boss_music():
    pass

def play_victory_music():
    pass