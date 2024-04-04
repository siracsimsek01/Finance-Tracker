from tkinter import Button, Label
import tkinter as tk


COLOR_BG = "#0F1C2E"
COLOR_PRIMARY = "#1F3A5F"
COLOR_SECONDARY = "#cee8ff"
COLOR_FRAME = "#4d648d"
COLOR_WHITE = "#FFF"
COLOR_BLACK = "#000"

TEXT_HEADING = ("Roboto", 18)
TEXT_TEXT = ("Roboto", 14)
TEXT_LABEL = ("Roboto", 12)


def primary_button(master, **kwargs):
    default = {
        "bg": COLOR_SECONDARY,
        "fg": COLOR_WHITE,
        "relief": "flat",
        "padx": 10,
        "pady": 5,    
    }
    
    default.update(kwargs)
    return Button(master, **default)

def primary_label(master, **kwargs):
    default = {
        "bg": COLOR_BG,
        "fg": COLOR_WHITE,
        "font": TEXT_TEXT,
    }
    
    default.update(kwargs)
    return Label(master, **default)

def secondary_label(master, **kwargs):
    default = {
        "bg": COLOR_BG,
        "fg": COLOR_WHITE,
        "font": TEXT_LABEL,
    }
    
    default.update(kwargs)
    return Label(master, **default)

def header_label(master, **kwargs):
    default = {
        "bg": COLOR_BG,
        "fg": COLOR_WHITE,
        "font": TEXT_HEADING,
    }
    default.update(kwargs)
    return Label(master, **default)
    
def balance_label(master, **kwargs):
    default = {
        "bg": COLOR_FRAME,
        "fg": COLOR_WHITE,
    }

    default.update(kwargs)
    return Label(master, **default)

    


