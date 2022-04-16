"""
buildconfig/stubs/gen_stubs.py
A script to auto-generate constants.pyi and __init__.pyi typestubs

IMPORTANT NOTE: Do not edit this file by hand!
"""

from typing import List

ACTIVEEVENT: int
ANYFORMAT: int
APPACTIVE: int
APPINPUTFOCUS: int
APPMOUSEFOCUS: int
APP_DIDENTERBACKGROUND: int
APP_DIDENTERFOREGROUND: int
APP_LOWMEMORY: int
APP_TERMINATING: int
APP_WILLENTERBACKGROUND: int
APP_WILLENTERFOREGROUND: int
ASYNCBLIT: int
AUDIODEVICEADDED: int
AUDIODEVICEREMOVED: int
AUDIO_ALLOW_ANY_CHANGE: int
AUDIO_ALLOW_CHANNELS_CHANGE: int
AUDIO_ALLOW_FORMAT_CHANGE: int
AUDIO_ALLOW_FREQUENCY_CHANGE: int
AUDIO_S16: int
AUDIO_S16LSB: int
AUDIO_S16MSB: int
AUDIO_S16SYS: int
AUDIO_S8: int
AUDIO_U16: int
AUDIO_U16LSB: int
AUDIO_U16MSB: int
AUDIO_U16SYS: int
AUDIO_U8: int
BIG_ENDIAN: int
BLENDMODE_ADD: int
BLENDMODE_BLEND: int
BLENDMODE_MOD: int
BLENDMODE_NONE: int
BLEND_ADD: int
BLEND_ALPHA_SDL2: int
BLEND_MAX: int
BLEND_MIN: int
BLEND_MULT: int
BLEND_PREMULTIPLIED: int
BLEND_RGBA_ADD: int
BLEND_RGBA_MAX: int
BLEND_RGBA_MIN: int
BLEND_RGBA_MULT: int
BLEND_RGBA_SUB: int
BLEND_RGB_ADD: int
BLEND_RGB_MAX: int
BLEND_RGB_MIN: int
BLEND_RGB_MULT: int
BLEND_RGB_SUB: int
BLEND_SUB: int
BUTTON_LEFT: int
BUTTON_MIDDLE: int
BUTTON_RIGHT: int
BUTTON_WHEELDOWN: int
BUTTON_WHEELUP: int
BUTTON_X1: int
BUTTON_X2: int
CLIPBOARDUPDATE: int
CONTROLLERAXISMOTION: int
CONTROLLERBUTTONDOWN: int
CONTROLLERBUTTONUP: int
CONTROLLERDEVICEADDED: int
CONTROLLERDEVICEREMAPPED: int
CONTROLLERDEVICEREMOVED: int
CONTROLLERSENSORUPDATE: int
CONTROLLERTOUCHPADDOWN: int
CONTROLLERTOUCHPADMOTION: int
CONTROLLERTOUCHPADUP: int
CONTROLLER_AXIS_INVALID: int
CONTROLLER_AXIS_LEFTX: int
CONTROLLER_AXIS_LEFTY: int
CONTROLLER_AXIS_MAX: int
CONTROLLER_AXIS_RIGHTX: int
CONTROLLER_AXIS_RIGHTY: int
CONTROLLER_AXIS_TRIGGERLEFT: int
CONTROLLER_AXIS_TRIGGERRIGHT: int
CONTROLLER_BUTTON_A: int
CONTROLLER_BUTTON_B: int
CONTROLLER_BUTTON_BACK: int
CONTROLLER_BUTTON_DPAD_DOWN: int
CONTROLLER_BUTTON_DPAD_LEFT: int
CONTROLLER_BUTTON_DPAD_RIGHT: int
CONTROLLER_BUTTON_DPAD_UP: int
CONTROLLER_BUTTON_GUIDE: int
CONTROLLER_BUTTON_INVALID: int
CONTROLLER_BUTTON_LEFTSHOULDER: int
CONTROLLER_BUTTON_LEFTSTICK: int
CONTROLLER_BUTTON_MAX: int
CONTROLLER_BUTTON_RIGHTSHOULDER: int
CONTROLLER_BUTTON_RIGHTSTICK: int
CONTROLLER_BUTTON_START: int
CONTROLLER_BUTTON_X: int
CONTROLLER_BUTTON_Y: int
DOUBLEBUF: int
DROPBEGIN: int
DROPCOMPLETE: int
DROPFILE: int
DROPTEXT: int
FINGERDOWN: int
FINGERMOTION: int
FINGERUP: int
FULLSCREEN: int
GL_ACCELERATED_VISUAL: int
GL_ACCUM_ALPHA_SIZE: int
GL_ACCUM_BLUE_SIZE: int
GL_ACCUM_GREEN_SIZE: int
GL_ACCUM_RED_SIZE: int
GL_ALPHA_SIZE: int
GL_BLUE_SIZE: int
GL_BUFFER_SIZE: int
GL_CONTEXT_DEBUG_FLAG: int
GL_CONTEXT_FLAGS: int
GL_CONTEXT_FORWARD_COMPATIBLE_FLAG: int
GL_CONTEXT_MAJOR_VERSION: int
GL_CONTEXT_MINOR_VERSION: int
GL_CONTEXT_PROFILE_COMPATIBILITY: int
GL_CONTEXT_PROFILE_CORE: int
GL_CONTEXT_PROFILE_ES: int
GL_CONTEXT_PROFILE_MASK: int
GL_CONTEXT_RELEASE_BEHAVIOR: int
GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH: int
GL_CONTEXT_RELEASE_BEHAVIOR_NONE: int
GL_CONTEXT_RESET_ISOLATION_FLAG: int
GL_CONTEXT_ROBUST_ACCESS_FLAG: int
GL_DEPTH_SIZE: int
GL_DOUBLEBUFFER: int
GL_FRAMEBUFFER_SRGB_CAPABLE: int
GL_GREEN_SIZE: int
GL_MULTISAMPLEBUFFERS: int
GL_MULTISAMPLESAMPLES: int
GL_RED_SIZE: int
GL_SHARE_WITH_CURRENT_CONTEXT: int
GL_STENCIL_SIZE: int
GL_STEREO: int
GL_SWAP_CONTROL: int
HAT_CENTERED: int
HAT_DOWN: int
HAT_LEFT: int
HAT_LEFTDOWN: int
HAT_LEFTUP: int
HAT_RIGHT: int
HAT_RIGHTDOWN: int
HAT_RIGHTUP: int
HAT_UP: int
HIDDEN: int
HWACCEL: int
HWPALETTE: int
HWSURFACE: int
JOYAXISMOTION: int
JOYBALLMOTION: int
JOYBUTTONDOWN: int
JOYBUTTONUP: int
JOYDEVICEADDED: int
JOYDEVICEREMOVED: int
JOYHATMOTION: int
KEYDOWN: int
KEYMAPCHANGED: int
KEYUP: int
KMOD_ALT: int
KMOD_CAPS: int
KMOD_CTRL: int
KMOD_GUI: int
KMOD_LALT: int
KMOD_LCTRL: int
KMOD_LGUI: int
KMOD_LMETA: int
KMOD_LSHIFT: int
KMOD_META: int
KMOD_MODE: int
KMOD_NONE: int
KMOD_NUM: int
KMOD_RALT: int
KMOD_RCTRL: int
KMOD_RGUI: int
KMOD_RMETA: int
KMOD_RSHIFT: int
KMOD_SHIFT: int
KSCAN_0: int
KSCAN_1: int
KSCAN_2: int
KSCAN_3: int
KSCAN_4: int
KSCAN_5: int
KSCAN_6: int
KSCAN_7: int
KSCAN_8: int
KSCAN_9: int
KSCAN_A: int
KSCAN_AC_BACK: int
KSCAN_APOSTROPHE: int
KSCAN_B: int
KSCAN_BACKSLASH: int
KSCAN_BACKSPACE: int
KSCAN_BREAK: int
KSCAN_C: int
KSCAN_CAPSLOCK: int
KSCAN_CLEAR: int
KSCAN_COMMA: int
KSCAN_CURRENCYSUBUNIT: int
KSCAN_CURRENCYUNIT: int
KSCAN_D: int
KSCAN_DELETE: int
KSCAN_DOWN: int
KSCAN_E: int
KSCAN_END: int
KSCAN_EQUALS: int
KSCAN_ESCAPE: int
KSCAN_EURO: int
KSCAN_F: int
KSCAN_F1: int
KSCAN_F10: int
KSCAN_F11: int
KSCAN_F12: int
KSCAN_F13: int
KSCAN_F14: int
KSCAN_F15: int
KSCAN_F2: int
KSCAN_F3: int
KSCAN_F4: int
KSCAN_F5: int
KSCAN_F6: int
KSCAN_F7: int
KSCAN_F8: int
KSCAN_F9: int
KSCAN_G: int
KSCAN_GRAVE: int
KSCAN_H: int
KSCAN_HELP: int
KSCAN_HOME: int
KSCAN_I: int
KSCAN_INSERT: int
KSCAN_INTERNATIONAL1: int
KSCAN_INTERNATIONAL2: int
KSCAN_INTERNATIONAL3: int
KSCAN_INTERNATIONAL4: int
KSCAN_INTERNATIONAL5: int
KSCAN_INTERNATIONAL6: int
KSCAN_INTERNATIONAL7: int
KSCAN_INTERNATIONAL8: int
KSCAN_INTERNATIONAL9: int
KSCAN_J: int
KSCAN_K: int
KSCAN_KP0: int
KSCAN_KP1: int
KSCAN_KP2: int
KSCAN_KP3: int
KSCAN_KP4: int
KSCAN_KP5: int
KSCAN_KP6: int
KSCAN_KP7: int
KSCAN_KP8: int
KSCAN_KP9: int
KSCAN_KP_0: int
KSCAN_KP_1: int
KSCAN_KP_2: int
KSCAN_KP_3: int
KSCAN_KP_4: int
KSCAN_KP_5: int
KSCAN_KP_6: int
KSCAN_KP_7: int
KSCAN_KP_8: int
KSCAN_KP_9: int
KSCAN_KP_DIVIDE: int
KSCAN_KP_ENTER: int
KSCAN_KP_EQUALS: int
KSCAN_KP_MINUS: int
KSCAN_KP_MULTIPLY: int
KSCAN_KP_PERIOD: int
KSCAN_KP_PLUS: int
KSCAN_L: int
KSCAN_LALT: int
KSCAN_LANG1: int
KSCAN_LANG2: int
KSCAN_LANG3: int
KSCAN_LANG4: int
KSCAN_LANG5: int
KSCAN_LANG6: int
KSCAN_LANG7: int
KSCAN_LANG8: int
KSCAN_LANG9: int
KSCAN_LCTRL: int
KSCAN_LEFT: int
KSCAN_LEFTBRACKET: int
KSCAN_LGUI: int
KSCAN_LMETA: int
KSCAN_LSHIFT: int
KSCAN_LSUPER: int
KSCAN_M: int
KSCAN_MENU: int
KSCAN_MINUS: int
KSCAN_MODE: int
KSCAN_N: int
KSCAN_NONUSBACKSLASH: int
KSCAN_NONUSHASH: int
KSCAN_NUMLOCK: int
KSCAN_NUMLOCKCLEAR: int
KSCAN_O: int
KSCAN_P: int
KSCAN_PAGEDOWN: int
KSCAN_PAGEUP: int
KSCAN_PAUSE: int
KSCAN_PERIOD: int
KSCAN_POWER: int
KSCAN_PRINT: int
KSCAN_PRINTSCREEN: int
KSCAN_Q: int
KSCAN_R: int
KSCAN_RALT: int
KSCAN_RCTRL: int
KSCAN_RETURN: int
KSCAN_RGUI: int
KSCAN_RIGHT: int
KSCAN_RIGHTBRACKET: int
KSCAN_RMETA: int
KSCAN_RSHIFT: int
KSCAN_RSUPER: int
KSCAN_S: int
KSCAN_SCROLLLOCK: int
KSCAN_SCROLLOCK: int
KSCAN_SEMICOLON: int
KSCAN_SLASH: int
KSCAN_SPACE: int
KSCAN_SYSREQ: int
KSCAN_T: int
KSCAN_TAB: int
KSCAN_U: int
KSCAN_UNKNOWN: int
KSCAN_UP: int
KSCAN_V: int
KSCAN_W: int
KSCAN_X: int
KSCAN_Y: int
KSCAN_Z: int
K_0: int
K_1: int
K_2: int
K_3: int
K_4: int
K_5: int
K_6: int
K_7: int
K_8: int
K_9: int
K_AC_BACK: int
K_AMPERSAND: int
K_ASTERISK: int
K_AT: int
K_BACKQUOTE: int
K_BACKSLASH: int
K_BACKSPACE: int
K_BREAK: int
K_CAPSLOCK: int
K_CARET: int
K_CLEAR: int
K_COLON: int
K_COMMA: int
K_CURRENCYSUBUNIT: int
K_CURRENCYUNIT: int
K_DELETE: int
K_DOLLAR: int
K_DOWN: int
K_END: int
K_EQUALS: int
K_ESCAPE: int
K_EURO: int
K_EXCLAIM: int
K_F1: int
K_F10: int
K_F11: int
K_F12: int
K_F13: int
K_F14: int
K_F15: int
K_F2: int
K_F3: int
K_F4: int
K_F5: int
K_F6: int
K_F7: int
K_F8: int
K_F9: int
K_GREATER: int
K_HASH: int
K_HELP: int
K_HOME: int
K_INSERT: int
K_KP0: int
K_KP1: int
K_KP2: int
K_KP3: int
K_KP4: int
K_KP5: int
K_KP6: int
K_KP7: int
K_KP8: int
K_KP9: int
K_KP_0: int
K_KP_1: int
K_KP_2: int
K_KP_3: int
K_KP_4: int
K_KP_5: int
K_KP_6: int
K_KP_7: int
K_KP_8: int
K_KP_9: int
K_KP_DIVIDE: int
K_KP_ENTER: int
K_KP_EQUALS: int
K_KP_MINUS: int
K_KP_MULTIPLY: int
K_KP_PERIOD: int
K_KP_PLUS: int
K_LALT: int
K_LCTRL: int
K_LEFT: int
K_LEFTBRACKET: int
K_LEFTPAREN: int
K_LESS: int
K_LGUI: int
K_LMETA: int
K_LSHIFT: int
K_LSUPER: int
K_MENU: int
K_MINUS: int
K_MODE: int
K_NUMLOCK: int
K_NUMLOCKCLEAR: int
K_PAGEDOWN: int
K_PAGEUP: int
K_PAUSE: int
K_PERCENT: int
K_PERIOD: int
K_PLUS: int
K_POWER: int
K_PRINT: int
K_PRINTSCREEN: int
K_QUESTION: int
K_QUOTE: int
K_QUOTEDBL: int
K_RALT: int
K_RCTRL: int
K_RETURN: int
K_RGUI: int
K_RIGHT: int
K_RIGHTBRACKET: int
K_RIGHTPAREN: int
K_RMETA: int
K_RSHIFT: int
K_RSUPER: int
K_SCROLLLOCK: int
K_SCROLLOCK: int
K_SEMICOLON: int
K_SLASH: int
K_SPACE: int
K_SYSREQ: int
K_TAB: int
K_UNDERSCORE: int
K_UNKNOWN: int
K_UP: int
K_a: int
K_b: int
K_c: int
K_d: int
K_e: int
K_f: int
K_g: int
K_h: int
K_i: int
K_j: int
K_k: int
K_l: int
K_m: int
K_n: int
K_o: int
K_p: int
K_q: int
K_r: int
K_s: int
K_t: int
K_u: int
K_v: int
K_w: int
K_x: int
K_y: int
K_z: int
LIL_ENDIAN: int
LOCALECHANGED: int
MIDIIN: int
MIDIOUT: int
MOUSEBUTTONDOWN: int
MOUSEBUTTONUP: int
MOUSEMOTION: int
MOUSEWHEEL: int
MULTIGESTURE: int
NOEVENT: int
NOFRAME: int
NUMEVENTS: int
OPENGL: int
OPENGLBLIT: int
PREALLOC: int
QUIT: int
RENDER_DEVICE_RESET: int
RENDER_TARGETS_RESET: int
RESIZABLE: int
RLEACCEL: int
RLEACCELOK: int
SCALED: int
SCRAP_BMP: str
SCRAP_CLIPBOARD: int
SCRAP_PBM: str
SCRAP_PPM: str
SCRAP_SELECTION: int
SCRAP_TEXT: str
SHOWN: int
SRCALPHA: int
SRCCOLORKEY: int
SWSURFACE: int
SYSTEM_CURSOR_ARROW: int
SYSTEM_CURSOR_CROSSHAIR: int
SYSTEM_CURSOR_HAND: int
SYSTEM_CURSOR_IBEAM: int
SYSTEM_CURSOR_NO: int
SYSTEM_CURSOR_SIZEALL: int
SYSTEM_CURSOR_SIZENESW: int
SYSTEM_CURSOR_SIZENS: int
SYSTEM_CURSOR_SIZENWSE: int
SYSTEM_CURSOR_SIZEWE: int
SYSTEM_CURSOR_WAIT: int
SYSTEM_CURSOR_WAITARROW: int
SYSWMEVENT: int
TEXTEDITING: int
TEXTINPUT: int
TIMER_RESOLUTION: int
USEREVENT: int
USEREVENT_DROPFILE: int
VIDEOEXPOSE: int
VIDEORESIZE: int
WINDOWCLOSE: int
WINDOWDISPLAYCHANGED: int
WINDOWENTER: int
WINDOWEXPOSED: int
WINDOWFOCUSGAINED: int
WINDOWFOCUSLOST: int
WINDOWHIDDEN: int
WINDOWHITTEST: int
WINDOWICCPROFCHANGED: int
WINDOWLEAVE: int
WINDOWMAXIMIZED: int
WINDOWMINIMIZED: int
WINDOWMOVED: int
WINDOWRESIZED: int
WINDOWRESTORED: int
WINDOWSHOWN: int
WINDOWSIZECHANGED: int
WINDOWTAKEFOCUS: int

__all__: List[str]
