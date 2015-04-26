import shlex
import subprocess
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

cmdline = 'streamer/mjpg_streamer -i "streamer/input_uvc.so -n -d /dev/video0 -r 640x480 -f 5" -o "streamer/output_http.so -p 8090 -w streamer/www"'

args = shlex.split(cmdline)
log.debug("Arguments are: %s", args)
p = None


def start_streamer():
    global p
    p = subprocess.Popen(args, stdout=subprocess.PIPE)
    log.debug("Video streaming process started")


def stop_streamer():
    global p
    p.terminate()


if __name__ == '__main__':
    try:
        start_streamer()
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log.info("Stopping program")
        stop_streamer()
        log.info("Program stopped")
        import sys
        sys.exit(0)

