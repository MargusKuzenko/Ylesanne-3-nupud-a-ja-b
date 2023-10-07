def on_gesture_shake():
    basic.show_string("Palun ei!")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.HAPPY)
    elif input.button_is_pressed(Button.B):
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.ASLEEP)
basic.forever(on_forever)
