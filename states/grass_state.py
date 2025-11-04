from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pygame
from game_state import State

from core.utils import load_sprite_sheet
from data.constants import GRASS_SPRITE_SHEET

if TYPE_CHECKING:
    from pygame import Event


class GrassState(State):
    def __init__(self) -> None:
        self.grass_sprites = load_sprite_sheet(GRASS_SPRITE_SHEET)
        print(f"{self.grass_sprites=}")

    def process_event(self, event: Event) -> None:
        if event.type == pygame.QUIT:
            self.manager.is_running = False

    def process_update(self, *args: Any) -> None:
        self.window.fill((50, 50, 50))

        pygame.display.update()


def hook() -> None:
    GrassState.manager.load_states(GrassState)
