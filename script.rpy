# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Ma = Character("Elizabeth Arc", color="#ffd700")
define hyles = Character("Hyles", color="#ffff")
define arab = Character("Arab",color="#c54b85")
define mau = Character("Angela(Mau)",color="#c54b85")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    play sound "mundian.mp3"
    arab "Hello Hello, testing"
    show arab normal:
        xalign 0.0
        yalign 0.65
    arab "Hello there"
    play sound "choir.mp3"
    show mau normal:
        xalign 1.0
        yalign 0.65
    mau "Yahalo! "
    hyles "Oh! Didn't notice you there"
    hyles "this is Visual Novel based on a Story/Quest called {a=https://shorturl.at/NoHRw}A Simple Jaune Quest{/a}"
    # This shows a character sprite. A placeholder is used, but you can

    return