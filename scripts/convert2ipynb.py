import os
from subprocess import call

import yaml

PREFIX = ''#'qmlcourse'+'/'

with open('qmlcourse/_toc.yml') as f:
    toc = yaml.safe_load(f)
# make dir for ipynbs
os.makedirs("notebooks", exist_ok=True)
# remove index file
for part in toc[1:]:
    for chapter in part['chapters']:
        call(['poetry', 'run', 'jupytext', PREFIX + chapter['file'], '--to', 'ipynb'])
        os.makedirs( 'notebooks/' + '/'.join(chapter['file'].split("/")[1:-1]), exist_ok=True)
        call(['mv', PREFIX + chapter['file'].split('.')[0] + '.ipynb', 'notebooks/' + '/'.join(chapter['file'].split("/")[1:]) + '.ipynb'])