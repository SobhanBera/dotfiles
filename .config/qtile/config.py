# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer
import arcobattery

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [

# CUSTOM KEY
# FOR INCREASING AND DECREASING LAYOUT SIZE...
     Key(["control", "shift"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key(["control", "shift"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key(["control", "shift"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key(["control", "shift"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),

# FUNCTION KEYS

    Key([], "F12", lazy.spawn('xfce4-terminal --drop-down')),

# SUPER + FUNCTION KEYS

    Key([mod], "e", lazy.spawn('google-chrome-stable')),
    Key([mod], "c", lazy.spawn('conky-toggle')),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "m", lazy.spawn('pragha')),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "r", lazy.spawn('rofi-theme-selector')),
    Key([mod], "t", lazy.spawn('urxvt')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "w", lazy.spawn('vivaldi-stable')),
    Key([mod], "x", lazy.spawn('arcolinux-logout')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn('alacritty -e zsh')),
    Key([mod], "KP_Enter", lazy.spawn('termite')),
    Key([mod], "F1", lazy.spawn('vivaldi-stable')),
    Key([mod], "F2", lazy.spawn('atom')),
    Key([mod], "F3", lazy.spawn('inkscape')),
    Key([mod], "F4", lazy.spawn('gimp')),
    Key([mod], "F5", lazy.spawn('meld')),
    Key([mod], "F6", lazy.spawn('vlc --video-on-top')),
    Key([mod], "F7", lazy.spawn('virtualbox')),
    Key([mod], "F8", lazy.spawn('pcmanfm')),
    Key([mod], "F9", lazy.spawn('evolution')),
    Key([mod], "F10", lazy.spawn("spotify")),
    Key([mod], "F11", lazy.spawn('rofi -show run -fullscreen')),
    Key([mod], "F12", lazy.spawn('rofi -show run')),

# SUPER + SHIFT KEYS

    Key([mod, "shift"], "Return", lazy.spawn('thunar')),
    Key([mod], "d", lazy.spawn("dmenu_run -l 25 -i -nb '#191919' -nf '#0f60b6' -sb '#0f60b6' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key(["mod1"], "d", lazy.spawn("dmenu_run -l 25 -i -nb '#191919' -nf '#0f60b6' -sb '#0f60b6' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    # Key([mod, "shift"], "x", lazy.shutdown()),

# CONTROL + ALT KEYS

    Key(["mod1", "control"], "Next", lazy.spawn('conky-rotate -n')),
    Key(["mod1", "control"], "Prior", lazy.spawn('conky-rotate -p')),
    Key(["mod1", "control"], "a", lazy.spawn('xfce4-appfinder')),
    Key(["mod1", "control"], "b", lazy.spawn('thunar')),
    Key(["mod1", "control"], "c", lazy.spawn('catfish')),
    Key(["mod1", "control"], "e", lazy.spawn('arcolinux-tweak-tool')),
    Key(["mod1", "control"], "f", lazy.spawn('firefox')),
    Key(["mod1", "control"], "g", lazy.spawn('chromium -no-default-browser-check')),
    Key(["mod1", "control"], "i", lazy.spawn('nitrogen')),
    Key(["mod1", "control"], "k", lazy.spawn('arcolinux-logout')),
    Key(["mod1", "control"], "l", lazy.spawn('arcolinux-logout')),
    Key(["mod1", "control"], "m", lazy.spawn('xfce4-settings-manager')),
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "p", lazy.spawn('pamac-manager')),
    Key(["mod1", "control"], "r", lazy.spawn('rofi-theme-selector')),
    Key(["mod1", "control"], "s", lazy.spawn('spotify')),
    Key(["mod1", "control"], "t", lazy.spawn('termite')),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
    Key(["mod1", "control"], "v", lazy.spawn('vivaldi-stable')),
    Key(["mod1", "control"], "w", lazy.spawn('arcolinux-welcome-app')),
    Key(["mod1", "control"], "Return", lazy.spawn('termite')),

# ALT + ... KEYS

    Key(["mod1"], "f", lazy.spawn('variety -f')),
    Key(["mod1"], "h", lazy.spawn('urxvt -e htop')),
    Key(["mod1"], "n", lazy.spawn('variety -n')),
    Key(["mod1"], "p", lazy.spawn('variety -p')),
    Key(["mod1"], "t", lazy.spawn('variety -t')),
#    Key(["mod1"], "Up", lazy.spawn('variety --pause')),
#    Key(["mod1"], "Down", lazy.spawn('variety --resume')),
#    Key(["mod1"], "Left", lazy.spawn('variety -p')),
#    Key(["mod1"], "Right", lazy.spawn('variety -n')),
    Key(["mod1"], "F2", lazy.spawn('gmrun')),
    Key(["mod1"], "F3", lazy.spawn('xfce4-appfinder')),

# VARIETY KEYS WITH PYWAL

    Key(["mod1", "shift"], "f", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -f')),
    Key(["mod1", "shift"], "p", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -p')),
    Key(["mod1", "shift"], "n", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -n')),
    Key(["mod1", "shift"], "u", lazy.spawn(home + '/.config/qtile/scripts/set-pywal.sh -u')),

# CONTROL + SHIFT KEYS

    Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),

# SCREENSHOTS

    Key([], "Print", lazy.spawn("scrot 'ArcoLinux-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    Key([mod2], "Print", lazy.spawn('xfce4-screenshooter')),
    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
group_labels = ["  ", "   ", "   ", "  ", "  ", "  ", "  ", "  ", "  ", "  "]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        #Key(["mod1"], "Tab", lazy.screen.next_group()),
        # alt + tab will shift focus of layouts... like in windows
        # and S + tab will change screens...
        Key(["mod1"], "Tab", lazy.layout.up()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

# custom name in different fonts...
# and remove conky bvy default...
lazy.spawn('conky-toggle')
import random
import datetime # will require at widget part
my_name_list = [
    "🅂🄾🄱🄷🄰🄽 🄱🄴🅁🄰",
    "🆂🅾🅱🅷🅰🅽 🅱🅴🆁🅰",
    "🅢🅞🅑🅗🅐🅝 🅑🅔🅡🅐",
    "ⓈⓄⒷⒽⒶⓃ ⒷⒺ ⓇⒶ",
    "𝕊𝕆𝔹ℍ𝔸ℕ 𝔹𝔼ℝ𝔸",
    "S̶O̶B̶H̶A̶N̶ B̶E̶R̶A̶",
    # "𝒮𝒪ℬℋ𝒜𝒩 ℬℰℛ𝒜",
    "𝓢𝓞𝓑𝓗𝓐𝓝 𝓑𝓔𝓡𝓐",
    # "ϨⲞⲂⲎⲀⲚ ⲂⲈꞄⲀ",
    "SOẞԨ𝓐Ɲ ẞƐᎡ𝓐",
    "⟆〇ᗷᕼᗩƝ ᗷᕮᖇᗩ",
    "𝙎𝙊𝘽𝙃𝘼𝙉 𝘽𝙀𝙍𝘼",
    "🆂 🄾 🅑 ℍ ᗩ 𝓝 ẞ Ǝ 🆁 𝓐",
    # "$⊙β¦-¦Д⁄(⁄  β€®Д"
]

# COLORS FOR THE BAR

#def init_colors():
#    return [["#2F343F", "#2F343F"], # color 0
#            ["#2F343F", "#2F343F"], # color 1
#            ["#c0c5ce", "#c0c5ce"], # color 2
#            ["#fba922", "#fba922"], # color 3
#            ["#3384d0", "#3384d0"], # color 4
#            ["#f3f4f5", "#f3f4f5"], # color 5
#            ["#cd1f3f", "#cd1f3f"], # color 6
#            ["#62FF00", "#62FF00"], # color 7
#            ["#6790eb", "#6790eb"], # color 8
#            ["#a9a9a9", "#a9a9a9"]] # color 9

def init_color_final():
    return [
        ["#160e19", "#160e19"], # 0- main background 0b0f1a
        ["#bdbdbd", "#bdbdbd"], # 1- main foreground
        ["#df3917", "#df3917"], # 2- arrow 1 background
        ["#ffffff", "#ffffff"], # 3- arrow 1 foreground
        ["#2d3236", "#2d3236"], # 4- arrow 2 background
        ["#ffffff", "#ffffff"], # 5- arrow 2 foreground
        ["#cfcfcf", "#cfcfcf"], # 6- enabled
        ["#909090", "#909090"], # 7- disabled
        ["#df3917", "#df3917"], # 8- highlight background
        ["#ffffff", "#ffffff"], # 9- highlight foreground
        "#df3917",            # 10 - single color
    ]

colors = init_color_final()
currcolor = True

def init_layout_theme(name):
    return {
        "margin":3,
        "border_width":2,
        "border_focus": "#dfdfdf",
        "border_normal": "#656565",
        "name": f"{random.choice(my_name_list)} ({name})"
    }
# layout_theme = init_layout_theme("tab name")

layouts = [
    layout.MonadTall(
        margin=0,
        border_width=1,
        border_focus=colors[10],
        border_normal="#000000",
        max_ratio=0.95,
        change_size= 0.085,
        change_ratio=0.038,
        name=random.choice(my_name_list) + "    (MonadTall)",
        fontsize=20,
#       new_at_current=True,
        ratio=0.5
    ),
    layout.MonadWide(
        # margin=10,
        # border_width=1,
        # border_focus="#dfdfdf",
        # border_normal="#656565",
        margin=0,
        border_width=1,
        border_focus="#303030",
        border_normal="#000000",
        max_ratio=0.95,
        change_size= 0.085,
        change_ratio=0.038,
        name=random.choice(my_name_list) + "    (MonadWide)",
        fontsize=20,
        new_at_current=True,
        ratio=0.5
    ),
    layout.Matrix(**init_layout_theme("Matrix")),
    layout.Bsp(**init_layout_theme("Bsp")),
    layout.Floating(**init_layout_theme("Floating")),
    layout.RatioTile(**init_layout_theme("RatioTile")),
    layout.Max(**init_layout_theme("Max"))
]

def colorsToggler():
    if currcolor == True:
        colors = init_colors()
        currcolor = False
    else:
        colors = init_colors2()
        currcolor = True

# change color
# keys.extend([Key([mod], "c", colorsToggler)])

# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

# mouse callbacks functions...
# opens nvim or vim...
def open_vim(qtile):
    qtile.cmd_spawn('alacritty -e vim')
def open_htop_memory(qtile):
    qtile.cmd_spawn('alacritty -e htop')

def init_widgets_list():
    # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.GroupBox(
                        font="FontAwesome",
                        fontsize = 15,
                        margin_y = 0,
                        margin_x = 0,
                        padding_y = 8,
                        padding_x = 5,
                        borderwidth = 0,
                        disable_drag = False,
                        active = colors[6],
                        inactive = colors[7],
                        rounded = True,
                        highlight_color=colors[8],
                        highlight_method = "line",
                        this_current_screen_border = colors[1],
                        this_screen_border=colors[1],
                        foreground = colors[1],
                        background = colors[0],
                        invert_mouse_wheel=True,
                        center_aligned=False,
                        hide_unused=False,
                        block_highlight_text_color=colors[9]
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[0]
                        ),
               widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors[1],
                        background = colors[0]
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[1],
                        background = colors[0]
                        ),
               widget.WindowName(font="Noto Sans",
                        fontsize = 14,
                        foreground = colors[8],
                        background = colors[0],
                        ),
                widget.TextBox(
                        text="",
                        foreground=colors[2],
                        background=colors[0],
                        padding = 0,
                        fontsize=50
                        ),
               widget.TextBox(
                        text="",
                        foreground=colors[4],
                        background=colors[2],
                        padding = 0,
                        fontsize=50
                        ),
              widget.TextBox(
                        text="",
                        foreground=colors[2],
                        background=colors[4],
                        padding = 0,
                        fontsize=50
                        ),
               widget.TextBox(
                        text="",
                        foreground=colors[4],
                        background=colors[2],
                        padding = 0,
                        fontsize=50
                        ),
              widget.TextBox(
                        text="",
                        foreground=colors[2],
                        background=colors[4],
                        padding = 0,
                        fontsize=50
                        ),
               widget.Net(
                   foreground=colors[3],
                   background=colors[2],
                   fontsize=13,
                   format="↓{down}  ↑{up}",
                   #↓↑
                   ),
               widget.TextBox(
                        text="",
                        foreground=colors[4],
                        background=colors[2],
                        padding = 0,
                        fontsize=50
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="   ",
                        foreground=colors[5],
                        background=colors[4],
                        padding = 0,
                        fontsize=13
                        ),
               widget.Battery(
                         font="Noto Sans",
                         update_interval = 10,
                         fontsize = 13,
                         foreground = colors[5],
                         background = colors[4],
                         format='{percent:2.0%} {char}'
	                 ),
               #widget.TextBox(
               #         text="",
               #         foreground=colors[5],
               #         background=colors[1],
               #         padding = 0,
               #         fontsize=50
               #         ),
               #widget.TextBox(
               #         font="FontAwesome",
               #         text="   ",
               #         foreground=colors[1],
               #         background=colors[5],
               #         padding = 0,
               #         fontsize=13
               #         ),
               #widget.CPUGraph(
               #         border_color = colors[1],
               #         fill_color = colors[1],
               #         graph_color = colors[1],
               #         background=colors[5],
               #         border_width = 1,
               #         line_width = 1,
               #         core = "all",
               #         type = "linefill"
               #         ),
               widget.TextBox(
                        text="",
                        foreground=colors[2],
                        background=colors[4],
                        padding = 0,
                        fontsize=50
                        ),
               #widget.TextBox(
               #         font="FontAwesome",
               #         text="   ",
               #         foreground=colors[1],
               #         background=colors[1],
               #         padding = 0,
               #         fontsize=13
               #         ),
               widget.Memory(
                        font="Noto Sans",
                        format = '{MemUsed} / {MemTotal}',
                        update_interval = 1,
                        fontsize = 13,
                        foreground = colors[3],
                        background = colors[2],
                        mouse_callbacks={'Button1': open_htop_memory}
                       ),
               widget.TextBox(
                        text="",
                        foreground=colors[4],
                        background=colors[2],
                        padding = 0,
                        fontsize=50
                        ),
               #widget.TextBox(
               #         font="FontAwesome",
               #         text="   ",
               #         foreground=colors[1],
               #         background=colors[1],
               #         padding = 0,
               #         fontsize=13
               #         ),
               widget.Clock(
                        foreground = colors[5],
                        background = colors[4],
                        fontsize = 13,
                        format="%d-%b-%Y %H:%M %p",
                        #format="%c",
                        ),
                widget.TextBox(
                        text="",
                        foreground=colors[2],
                        background=colors[4],
                        padding = 0,
                        fontsize=50
                        ),
               widget.TextBox(
                        text="",
                        foreground=colors[4],
                        background=colors[2],
                        padding = 0,
                        fontsize=50
                        ),
               widget.Systray(
                        background=colors[0],
                        icon_size=22,
                        padding = 8,
                        margin = 2
                        ),
              ]
    return widgets_list

widgets_list = init_widgets_list()

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_list(), size=27, opacity=0.99999, margin=0, background=colors[1])),
            Screen(top=bar.Bar(widgets=init_widgets_list(), size=27, opacity=0.99999, margin=0, background=colors[1]))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #########################################################
#     ################ assgin apps to groups ##################
#     #########################################################
#     d["1"] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d["2"] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d["3"] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d["4"] = ["Gimp", "gimp" ]
#     d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d["7"] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d["8"] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d["0"] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ##########################################################
#     wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'arcolinux-logout'},
    {'wmclass': 'xfce4-terminal'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
