import sys

sys.path.insert(1, '/personal_fawkes')

from fawkes.protection import Fawkes
import os

sys.argv[1]

image_paths = {sys.argv[1]}
my_fawkes = Fawkes("extractor_2", '0', 1)
my_fawkes.run_protection(image_paths, debug=True)