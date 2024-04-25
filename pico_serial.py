# Raspberry Pi Pico W (MicroPython)
import machine
import utime
import urandom

# Configure UART
uart = machine.UART(0, baudrate=9600)

while True:
    # Generate random values for x and y
    x = urandom.getrandbits(8)
    y = urandom.getrandbits(8)

    # Construct the message to send
    message = f"x={x},y={y}\n"

    # Send the message over UART
    uart.write(message)

    # Wait for 1 second before sending the next message
    utime.sleep(1)