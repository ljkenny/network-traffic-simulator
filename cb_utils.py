import os
import time
import random

#DEBUG_ON = True
DEBUG_ON = False

MAIN_LOG = "chatterbot.log"
DEBUG_LOG = "chatterbot_debug.log"

dumb = False

def random_sleep(agent):
    # Lee: HACK HACK HACK 
    return

    sleep_time_secs = random.randint(5, 30)
    write_debug(agent, "sleep: %s" % (sleep_time_secs))
    time.sleep(sleep_time_secs)
    
    
def get_dir_path():
    abspath =  os.path.abspath(__file__)     # path of this file including the file
    dir_path = os.path.dirname(abspath)      # dir path to this file excluding the file
    return dir_path

def get_log_file():
    dir_path = get_dir_path()
    debug_file_path = os.path.join(dir_path, "logs", "%s" % MAIN_LOG)
    if not os.path.exists(os.path.join(dir_path, "logs")):
        os.makedirs(os.path.join(dir_path, "logs"))
    return debug_file_path

def write_log(agent, log_message, new_line=False):
    '''
    writes message to main chatterbot.log
    '''

    log_file_path = get_log_file()

    if os.path.isfile(log_file_path):
        open_as = "a"   # append
    else:
        open_as = "w"

    with open(log_file_path, open_as) as log_file:
        if new_line is True:
           log_file.write("\n")
        log_file.write("\n%s [%s] %s" % (time.ctime(), agent, log_message))
        print "[%s] %s" % (agent, log_message)

def get_debug_file():
    dir_path = get_dir_path()
    debug_file_path = os.path.join(dir_path, "logs", "%s" % DEBUG_LOG)
    if not os.path.exists(os.path.join(dir_path, "logs")):
        os.makedirs(os.path.join(dir_path, "logs"))
    return debug_file_path

def write_debug(agent, debug_message, new_line=False):
    '''
    writes debug message to main chatterbot_debug.log if debug is on
    '''
    debug_file_path = get_debug_file()
            
    if DEBUG_ON:    
        if os.path.isfile(debug_file_path):
            open_as = "a"   # append
        else:
            open_as = "w"
            
        with open(debug_file_path, open_as) as debug_file:
            if new_line is True:
               debug_file.write("\n") 
            debug_file.write("\n%s[%s] : %s" % ( time.ctime(), agent, debug_message))
            
        print(debug_message)
    return None

def get_dump_file(agent_name):
    dir_path = get_dir_path()
    dump_file = os.path.join("output_dumps", "%s_dump.csv" % agent_name)  #.json"
    if not os.path.exists("output_dumps"):
        os.makedirs("output_dumps")
    return dump_file

def get_spider_path(spider_name):
    dir_path = get_dir_path()
    spider_path = os.path.join(dir_path, "%s.py" % spider_name)
    return spider_path

def get_wav_files(wav_name):
    dir_path = get_dir_path()
    wav_file_path = os.path.join(dir_path, "inputs", "%s.wav" % wav_name)
    return wav_file_path

def enter_dumb_mode():
    write_log("COMMAND", "Entering dumb mode")
    dumb = True

def leave_dumb_mode():
    write_log("COMMAND", "Leaving dumb mode")
    dumb = False

def is_dumb():
    return dumb
