from __future__ import annotations

from typing import TYPE_CHECKING

from pygame.sprite import Group, Sprite
from pygame.surface import Surface

if TYPE_CHECKING:
    from pygame import Rect, Surface


class GrassSprite(Sprite):
    def __init__(
        self,
        group: Group[GrassSprite],
        image: Surface,
        position: tuple[int, int],
    ) -> None:
        super().__init__(group)
        self.image: Surface = image
        self.rect: Rect = image.get_rect()
        self.rect.center = position


class GrassGroup(Group[GrassSprite]): ...
