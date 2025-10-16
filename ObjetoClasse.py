#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 16:18:56 2025

@author: jacques
"""

class ObjetoClasse:
    def __init__(self, data: dict):
        self.id = data.get("id")
        self.title = data.get("title")
        self.worth = data.get("worth")
        self.thumbnail = data.get("thumbnail")
        self.image = data.get("image")
        self.description = data.get("description")
        self.instructions = data.get("instructions")
        self.open_giveaway_url = data.get("open_giveaway_url")
        self.published_date = data.get("published_date")
        self.type = data.get("type")
        self.platforms = data.get("platforms")
        self.end_date = data.get("end_date")
        self.users = data.get("users")
        self.status = data.get("status")
        self.gamerpower_url = data.get("gamerpower_url")
        self.open_giveaway = data.get("open_giveaway")