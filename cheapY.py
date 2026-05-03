from machine import Pin
import time

print("Starting...")

import machine
spi_bus = machine.SPI.Bus(host=1, mosi=13, sck=14)

import lcd_bus
display_bus = lcd_bus.SPIBus(spi_bus=spi_bus, freq=24_000_000, dc=2, cs=15)

import lvgl as lv
import ili9341
import Pin
scr = lv.screen_active()
btn1 = Pin(21,Pin.IN)
btn2 = Pin(22,Pin.IN)
btn3 = Pin(23,Pin.IN)
             

display = ili9341.ILI9341(
     data_bus=display_bus,
     display_width=320,
     display_height=240,
     backlight_pin=21,
     backlight_on_state=ili9341.STATE_PWM,
     color_space=lv.COLOR_FORMAT.RGB565,
     color_byte_order=ili9341.BYTE_ORDER_RGB,
     rgb565_byte_swap=1
)

whichBtn = [#array for the 3 physical buttons to have sting for display
    (btn1, "you pressed 1"),
    (btn2, "you pressed 2"),
    (btn3, "you pressed 3"),
]

display.set_power(True)
display.init(1)

display._ORIENTATION_TABLE = (0xE0, 0x0, 0x0, 0x0)
display.set_rotation(lv.DISPLAY_ROTATION._0)

display.set_backlight(100)
import task_handler
task_handler.TaskHandler()

while True:#if statment which keeps checking is a putton been presssed
    choice == 0
    pressed = btn1.value()
    if pressed == 1:
        choice == 1
        if choice == 1: 
            label = lv.label(whichBtn[choice])
            label.set_text(whichBtn[choice])
            label.center()
            time.sleep(2)
    elif pressed == 0 :
        choice == 2
        pressed = btn2.value()
        if pressed == 1:
            label = lv.label(whichBtn[choice])
            label.set_text(whichBtn[choice])
            label.center()
            time.sleep(2)
        elif pressed == 0:
            choice == 3
            pressed = btn3.value()
            if pressed == 1:
                label = lv.label(whichBtn[choice])
                label.set_text(whichBtn[choice])
                label.center()
                time.sleep(2)
            elif pressed == 0:
                choice == 0
                pressed = btn1.value()