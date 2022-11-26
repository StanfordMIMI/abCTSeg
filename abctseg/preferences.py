import os
import warnings

from yacs.config import CfgNode as CN

_PREFERENCES_FILE = os.path.join(os.path.join(os.path.dirname(__file__), "preferences.yaml"))
_HOME_DIR = os.path.expanduser("~")

_CWD = os.getcwd()

_C = CN()
# FIXME: have a default output folder path
_C.OUTPUT_PATH = os.path.join(_CWD, "outputs")
_C.CACHE_DIR = os.path.join(_CWD, ".abctseg/cache")
_C.MODELS_DIR = os.path.join(_CWD, ".abct_model_dir")
_C.INPUT_PATH = ""
_C.HF_TOKEN = ""

_C.BATCH_SIZE = 16
_C.NUM_WORKERS = 1


def save_preferences(filename=None):
    """Save preferences to a file.

    Args:
        filename (str, optional): Filename. Defaults to None.
    """
    if filename is None:
        filename = _PREFERENCES_FILE
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        f.write(PREFERENCES.dump())


def reset_preferences():
    """Reset preferences."""
    global PREFERENCES
    PREFERENCES = _C.clone()


PREFERENCES = _C.clone()
if not os.path.isfile(_PREFERENCES_FILE):
    save_preferences()
else:
    try:
        PREFERENCES.merge_from_file(_PREFERENCES_FILE)
    except KeyError:
        warnings.warn("Preference file is outdated. Please reset your preferences.")
        warnings.warn("Loading default config...")
