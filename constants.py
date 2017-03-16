FILE_NAME='data.json'

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

ADD_TOPIC_COMMAND = "at" # at title=[new_title]
REMOVE_TOPIC_COMMAND = "rt" # rt index
CHANGE_TITLE_COMMAND = "ct" # ct index title=[new_title]
CHANGE_COMMENT_COMMAND = "cc" # cc index comment=[new_comment]
ADD_LINK_COMMAND = "al" # al index link=[newlink]
REMOVE_LINK_COMMAND = "rl" # rl index link=[link_index]
CHANGE_LINK_COMMAND = "cl" # cl index link=[link_index] new=[new_link]
SHOW_ALL_TOPICS_COMMAND = "sat" # sat
SHOW_TOPIC = 'swt' # swt index
SAVE_COMMAND = "save" #
SEARCH_TOPICS_COMMAND = "st" # st search=[search_text]
SEARCH_IN_LINKS_COMMAND = "sl"
SHOW_COMMANDS = "sc"
PRINT_COMMAND = "com"
USE_DATASTORE_COMMAND = "use" # use db=[json_file_name]
ADD_TAG_COMMAND = "tag" # tag index link=[link_index] t=[tag_string] t=[tag_string]