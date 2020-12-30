"""
A set of utilities for macApp\n
© Anime no Sekai — 2020
"""
from re import sub
from json import dumps
from shutil import move
import signal as python_signal
from os import listdir, makedirs
from subprocess import check_output
from os.path import isdir, expanduser, basename, exists, splitext

from safeIO import TextFile

home = expanduser("~")

class OptimizedPath():
    """
    Opitmized locations for relatives()
    """
    def __init__(self) -> None:
        return

def get_scaled_size(bytes, suffix="B"):
    """
    Credit to PythonCode for this function.\n
    > https://www.thepythoncode.com/article/get-hardware-system-information-python\n
    Scale bytes to its proper format\n
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    (> string)
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return str(round(bytes, 2)) + unit + suffix
        bytes /= factor


def convert_to_boolean(element):
    """
    Safely converts an element to a boolean value
    """
    element = str(element)
    if element.lower().replace(' ', '') in ['true', '1', 'yes']:
        return True
    else:
        return False

    
def convert_to_int(element):
    """
    Safely converts anything to an integer
    """
    negative = False
    if str(element)[0] == "-":
        negative = True
    element = sub("[^0-9]", "", str(element).split('.')[0])
    if element != '':
        if negative:
            return - int(element)
        else:
            return int(element)
    else:
        return 0

def removeSpaceBeforeAndAfter(string):
    """
    Removes any space before and after a string.
    """
    new_text = string
    for index, _ in enumerate(string):
        if string[index] != ' ':
            new_text = string[index:] + ' '
            break
    try:
        if new_text[-1] == ' ':
            for index, _ in enumerate(new_text):
                if new_text[-int(index + 1)] != ' ':
                    new_text = new_text[:-int(index)]
                    break
    except:
        pass
    return new_text


def signal_to_name(signal):
    """
    Converts a signal to the signal name for killall
    """
    signals = ['HUP', 'INT', 'QUIT', 'ILL', 'TRAP', 'ABRT', 'EMT', 'FPE', 'KILL', 'BUS', 'SEGV', 'SYS', 'PIPE', 'ALRM', 'TERM', 'URG', 'STOP', 'TSTP', 'CONT', 'CHLD', 'TTIN', 'TTOU', 'IO', 'XCPU', 'XFSZ', 'VTALRM', 'PROF', 'WINCH', 'INFO', 'USR1', 'USR2']
    if isinstance(signal, str):
        signal = signal.replace(" ", "").upper().replace("SIG", "")
        if signal in signals:
            return signal
    elif signal == python_signal.SIGHUP:
        return "HUP"
    elif signal == python_signal.SIGINT:
        return "INT"
    elif signal == python_signal.SIGQUIT:
        return "QUIT"
    elif signal == python_signal.SIGILL:
        return "ILL"
    elif signal == python_signal.SIGTRAP:
        return "TRAP"
    elif signal == python_signal.SIGABRT:
        return "ABRT"
    elif signal == python_signal.SIGEMT:
        return "SIGEMT"
    elif signal == python_signal.SIGFPE:
        return "FPE"
    elif signal == python_signal.SIGKILL:
        return "KILL"
    elif signal == python_signal.SIGBUS:
        return "BUS"
    elif signal == python_signal.SIGSEGV:
        return "SEGV"
    elif signal == python_signal.SIGSYS:
        return "SYS"
    elif signal == python_signal.SIGPIPE:
        return "PIPE"
    elif signal == python_signal.SIGALRM:
        return "ALRM"
    elif signal == python_signal.SIGTERM:
        return "TERM"
    elif signal == python_signal.SIGURG:
        return "URG"
    elif signal == python_signal.SIGSTOP:
        return "STOP"
    elif signal == python_signal.SIGTSTP:
        return "TSTP"
    elif signal == python_signal.SIGCONT:
        return "CONT"
    elif signal == python_signal.SIGCHLD:
        return "CHLD"
    elif signal == python_signal.SIGTTIN:
        return "TTIN"
    elif signal == python_signal.SIGTTOU:
        return "TTOU"
    elif signal == python_signal.SIGIO:
        return "IO"
    elif signal == python_signal.SIGXCPU:
        return "XCPU"
    elif signal == python_signal.SIGXFSZ:
        return "XFSZ"
    elif signal == python_signal.SIGVTALRM:
        return "VTALRM"
    elif signal == python_signal.SIGPROF:
        return "PROF"
    elif signal == python_signal.SIGWINCH:
        return "WINCH"
    elif signal == python_signal.SIGINFO:
        return "INFO"
    elif signal == python_signal.SIGUSR1:
        return "USR1"
    elif signal == python_signal.SIGUSR2:
        return "USR2"
    else:
        return None