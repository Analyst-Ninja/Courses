import logging

# logger = logging.getLogger(__name__)
# logger.propagate = False
# logger.info('Hello from helper')

logger = logging.getLogger(__name__)

# create handler

stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

# Level & Format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a Warning")
logger.error("This is a Error")
