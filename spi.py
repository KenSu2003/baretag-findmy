from pyftdi.spi import SpiController
import time

# Initialize the SpiController
spi = SpiController()
spi.configure('ftdi://ftdi:232h/1')  # Channel 1 of FT232H

# Get a port to use the CS line (chip select)
slave = spi.get_port(cs=0)  # Using CS0 line

# Set the SPI clock frequency
spi_frequency = 1_000_000  # 1 MHz
slave.set_frequency(spi_frequency)

# Example of sending data
data_to_send = b'\x9F'  # Example command
response = slave.exchange(data_to_send, len(data_to_send))
print("Response from NRF51822:", response)

spi.terminate()
