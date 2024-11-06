import serial
import time

serial_port = '/dev/tty.usbserial-1220'
filename = 'nrf51_firmware_edited.bin'
device_firmware = 'read_firmware.bin'

def append_pattern_to_bin(file_path, pattern):
    with open(file_path, 'ab') as f:
        f.write(pattern)

# Path to your .bin file
bin_file_path = filename    # currently sitting in the same directory

# Pattern to append (0xDEADBEEF)
expected_pattern = b'\xDE\xAD\xBE\xEF'

# Append the pattern to the .bin file
append_pattern_to_bin(bin_file_path, expected_pattern)

# Open the serial port
ser = serial.Serial(serial_port, 115200, timeout=1)

# Function to send firmware
def send_firmware(firmware_path):
    with open(firmware_path, 'rb') as f:
        firmware = f.read()
        ser.write(firmware)
        time.sleep(1)  # Adjust sleep time as needed

# Function to read and print the last 4 bytes of the firmware
def read_last_bytes():
    ser.write(b'READ_LAST_BYTES\n')
    time.sleep(1)  # Give the device time to respond
    response = ser.read(20)
    print(f"Last 4 bytes: {response.hex().upper()}")


# Function to read firmware
def read_firmware(firmware_path, size):
    with open(firmware_path, 'wb') as f:
        for i in range(0, size, 1024):
            ser.write(b'READ_CHUNK\n')
            time.sleep(0.5)  # Increased wait time to ensure device can respond
            chunk = ser.read(1024)
            if not chunk:
                print(f"Failed to read chunk {i // 1024 + 1}. No data received.")
                break
            f.write(chunk)
            print(f"Read chunk {i // 1024 + 1}, bytes read: {len(chunk)}")

# Open the serial port
ser = serial.Serial(serial_port, 115200, timeout=1)

# Send the firmware
send_firmware(filename)

# Read the entire firmware
firmware_size = 21 * 1024  # Adjust this size based on your device's flash size
read_firmware(device_firmware, firmware_size)

# Read and print the last 4 bytes
# read_last_bytes()

# Close the serial port
ser.close()
