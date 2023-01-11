from machine import Pin, I2C
import ssd1306
import time

def timestring(t):
    return str(t[2]-1) + "d" + str(t[3]) + "h" + str(t[4]) + "m" + str(t[5]) + "s"

boot_time = time.time()

previous_diff = 0 # this is for detecting overflows
overflows = 0

# using default address 0x3C
i2c = I2C(id=0, sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 32, i2c)


while(True):
    display.fill(0)
    display.text("TIME SINCE BOOT", 0, 0, 1)
    diff = time.time() - boot_time
    difftuple = time.localtime(diff)
    display.text(timestring(difftuple), 0, 8, 1)
    display.text(str(overflows) + " OVERFLOWS", 0, 17, 1)
    display.show()
    time.sleep(1)
    if(diff < previous_diff):
        overflows = overflows + 1
    previous_diff = diff

