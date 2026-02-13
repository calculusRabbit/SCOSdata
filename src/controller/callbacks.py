"""
Controller module for SCOS Data Acquisition Application
Contains all callback functions and event handlers
"""
import dearpygui.dearpygui as dpg
import cv2
import numpy as np


class SCOSController:
    def __init__(self, ui):
        self.ui = ui
        self.camera = cv2.VideoCapture(0)
        self.camera_texture = None
    

    