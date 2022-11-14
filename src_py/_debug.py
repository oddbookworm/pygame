"""Debug functionality that allows for more useful issue reporting
"""

import sys

from pygame.base import get_sdl_version
from pygame.mixer import get_sdl_mixer_version
from pygame.font import get_sdl_ttf_version
from pygame.image import get_sdl_image_version
from pygame.freetype import get_version as get_freetype_version

from pygame.version import ver

def str_from_tuple(version_tuple):
    if version_tuple is None:
        return "None"

    strs = [str(i) for i in version_tuple]
    return ".".join(strs)

def debug(filename = None):
    debug_str = (f"pygame version: {ver}\n"
                    f"python version: {str_from_tuple(sys.version_info[0:3])}\n")

    debug_str += (f"SDL versions:\t\tLinked: {str_from_tuple(get_sdl_version())}\t"
                    f"Compiled: {str_from_tuple(get_sdl_version(linked = False))}\n")

    debug_str += (f"SDL Mixer versions:\tLinked: {str_from_tuple(get_sdl_mixer_version())}\t"
                    f"Compiled: {str_from_tuple(get_sdl_mixer_version(linked = False))}\n")

    debug_str += (f"SDL Font versions:\tLinked: {str_from_tuple(get_sdl_ttf_version())}\t"
                    f"Compiled: {str_from_tuple(get_sdl_ttf_version(linked = False))}\n")

    debug_str += (f"SDL Image versions:\tLinked: {str_from_tuple(get_sdl_image_version())}\t"
                    f"Compiled: {str_from_tuple(get_sdl_image_version(linked = False))}\n")

    debug_str += (f"Freetype versions:\tLinked: {str_from_tuple(get_freetype_version())}\t"
                    f"Compiled: {str_from_tuple(get_freetype_version(linked = False))}")

    if filename is None:
        print(debug_str)
