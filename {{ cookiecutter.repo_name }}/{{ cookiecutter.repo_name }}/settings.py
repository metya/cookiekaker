import os
import dotenv
import signal

signal.signal(signal.SIGINT, signal.default_int_handler)

dotenv.load_dotenv(dotenv.find_dotenv())

cwd = os.getenv("CWD")
RAND_STATE = 42