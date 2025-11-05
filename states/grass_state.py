from __future__ import annotations

import random
from typing import TYPE_CHECKING

import pygame
from game_state import State

from core.grass import GrassGroup, GrassSprite
from core.utils import load_sprite_sheet
from data.constants import GRASS_SPRITE_SHEET

if TYPE_CHECKING:
    from typing import Any

    from pygame import Event, Surface


class GrassState(State):
    def __init__(self) -> None:
        self.grass_sprites: list[Surface] = load_sprite_sheet(
            GRASS_SPRITE_SHEET
        )
        self.grass_group: GrassGroup = GrassGroup()

    def process_event(self, event: Event) -> None:
        if event.type == pygame.QUIT:
            self.manager.is_running = False

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         # print(event.pos)

    def process_update(self, *args: Any) -> None:
        self.window.fill((50, 50, 50))

        mouse_button_state = pygame.mouse.get_pressed()
        if mouse_button_state[0]:
            self.grass_group.add(
                GrassSprite(
                    self.grass_group,
                    random.choice(self.grass_sprites),
                    pygame.mouse.get_pos(),
                )
            )

            sorted_sprites = sorted(
                self.grass_group.spritedict.items(),
                key=lambda item: item[0].rect.y,
            )
            self.grass_group.spritedict = dict(sorted_sprites)

        self.grass_group.draw(self.window)

        pygame.display.update()


def hook() -> None:
    GrassState.manager.load_states(GrassState)
