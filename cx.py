#test deploy
try:
  os.mkdir('build')
except:
  pass
with open('build/cx.json', 'w') as f:
  f.write('teste')
