# script from https://github.com/raspberrypi/picamera2/blob/main/examples/capture_jpeg.py
#!/usr/bin/python
import time
import fcntl
import os
from picamera2 import Picamera2


def capture():
    picam2 = Picamera2()

    preview_config = picam2.create_preview_configuration(
        main={"size": (800, 600)})
    picam2.configure(preview_config)

    picam2.start()
    time.sleep(2)

    filename = int(time.time())
    _filename = str(filename) + ".png"
    picam2.capture_file(_filename)

    # open local fifo and insert name of image taken
    # reference:
    # https://stackoverflow.com/questions/39948721/reading-and-writing-fifo-files-between-c-and-python
    # fifo_name = "/tmp/local_fifo"
    # fd = os.open(fifo_name, os.O_WRONLY )
    # os.write(fd, str.encode(_filename + '\n'))
    # os.close(fd)
    return


if __name__ == "__main__":
    capture()
