from techniques.config.constants import open_green
from techniques.config.constants import open_red
from techniques.config.constants import hashes
from techniques.config.constants import close

def print_title_technique(text):
	print(open_green + "\n" + text.center(hashes, "#") + "\n" + close)
	
def print_mitigation(text):
        print(open_red + "\n[*] MITIGATION: " + text + "\n" + close)
