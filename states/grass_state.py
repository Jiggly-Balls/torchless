from __future__ import annotations

from typing import TYPE_CHECKING

import pygame
from game_state import State

if TYPE_CHECKING:
    from pygame import Event


class GrassState(State):
    def process_event(self, event: Event) -> None:
        if event.type == pygame.QUIT:
            self.manager.is_running = False


def hook() -> None:
    GrassState.manager.load_states(GrassState)
