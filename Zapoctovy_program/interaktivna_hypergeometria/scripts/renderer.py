"""
Renderer object
"""

import pygame
import numpy as np
import scripts.utilities as utilities


class Renderer:
    def __init__(self, app) -> None:
        
        """Initialize Renderer object.
        
        Keyword arguments:
        app - Main application class
        """
        
        self.app = app
        self.config = app.config
        self.scale = 300

        self.default_colors = [
            [0, 0, 0],
            [255, 255, 255],
            [255, 0, 0]]

        self.colors = self.default_colors
        
    def render(self) -> None:
        
        """Renders everything"""
        
        self.app.window.app_window.fill(self.colors[0])
        self.surface = self.app.window.app_window
        
        try:
            for edge in self.app.vrt_space.edges:
                if (edge[0] not in self.app.vrt_space.subobjects[self.app.vrt_space.current_subobject]) or (edge[1] not in self.app.vrt_space.subobjects[self.app.vrt_space.current_subobject]):
                    pygame.draw.line(self.app.window.app_window, self.colors[1], -self.scale * np.array(self.app.vrt_space.updated_points[edge[0]]) + [400, 300],
                                                                                  -self.scale * np.array(self.app.vrt_space.updated_points[edge[1]]) + [400, 300])
                else:
                    pygame.draw.line(self.app.window.app_window, self.colors[2], -self.scale * np.array(self.app.vrt_space.updated_points[edge[0]]) + [400, 300],
                                                                              -self.scale * np.array(self.app.vrt_space.updated_points[edge[1]]) + [400, 300])
        except IndexError:
            try:
                for edge in self.app.vrt_space.edges:
                    pygame.draw.line(self.app.window.app_window, self.colors[1], -self.scale * np.array(self.app.vrt_space.updated_points[edge[0]]) + [400, 300],
                                                                                  -self.scale * np.array(self.app.vrt_space.updated_points[edge[1]]) + [400, 300])
            except: # Edges are optional
                pass


        for index, point in enumerate(self.app.vrt_space.updated_points):
            try:
                if index not in self.app.vrt_space.subobjects[self.app.vrt_space.current_subobject]:
                    pygame.draw.circle(self.app.window.app_window, self.colors[1], -self.scale * point + [400, 300], 2)
                else:
                    pygame.draw.circle(self.app.window.app_window, self.colors[2], -self.scale * point + [400, 300], 2) 
            except IndexError: # Subobjects are optional
                pygame.draw.circle(self.app.window.app_window, self.colors[1], -self.scale * point + [400, 300], 2)
                
        # Show debug values
        try:
            utilities.debug(self.surface, self.app.window.font, (750, 10), self.colors[1], 
                            self.app.window.fps,
                            self.app.vrt_space.subobject_list[self.app.vrt_space.subobject_index])
        except IndexError:
            utilities.debug(self.surface, self.app.window.font, (750, 10), self.colors[1],
                            self.app.window.fps)