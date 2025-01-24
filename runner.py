import sys

sys.path.insert(1, '/personal_fawkes')
#sys.path.insert(1, '/fawkes')

from fawkes.protection import Fawkes
import os

image_paths = {sys.argv[1]}
my_fawkes = Fawkes("extractor_2", '0', 1)
my_fawkes.run_protection(image_paths, debug=True)