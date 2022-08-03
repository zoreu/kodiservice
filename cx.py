#test deploy
import os
try:
  os.mkdir('build')
except:
  pass
jsonfile = os.path.join('build','cx.json')
with open(jsonfile, 'w') as f:
  f.write('teste')
