
input = ['C','Eb', 'G', 'F']

naturals = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
sharps= ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')
flats= ('A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab')

### Sharp or flat mode
sharp_mode = 0
flat_mode = 0

for i in input:
  if len(i) == 2:
    if i[1] == '#':
      print('Sharp Mode')
      sharp_mode = 1
      break
    elif i[1] == 'b':
      print('Flat Mode')
      flat_mode = 1
      break
    else:
      print('Unknown Symbol:defaulting to Sharp Mode')
      sharp_mode = 1

#### If Sharp mode is on convert any flats to sharps

if sharp_mode == 1:
  for p,i in enumerate(input):
    if len(i) == 2:
      if i[1] == 'b':
        for k,j in zip(sharps, flats):
          if i == j:
            input[p] = k
            print('Converting flat note to sharp')
            print(i)
            print(k)

#### If Flat mode is on convert any sharps to flats

if flat_mode == 1:
  for p,i in enumerate(input):
    if len(i) == 2:
      if i[1] == '#':
        for k,j in zip(sharps, flats):
          if i == k:
            input[p] = j
            print('Converting sharp note to flat') # Combine with below prints
            print(i)
            print(j)

### Dictionary tracking present notes

reg = {}

for i in naturals:
  reg[i] = 0

for i in input:
  reg[i[0]] = 1

### Dictionary tracking accidentals

sharp_reg = {}
flat_reg = {}

for i in naturals:
  sharp_reg[i] = 0
  flat_reg[i] = 0

for i in input:
  if len(i) == 2:
    if i[1] == '#':
      sharp_reg[i[0]] = 1
    elif i[1] == 'b':
      flat_reg[i[0]] = 1

### Scale with naturals with each note as root

p = [] # List of list of scale from each root
u= []

for i in input:
  for n, j in enumerate(naturals):
    if i[0] == j:
      w = list(naturals[n:])
      r = list(naturals[:n])
      u = w + r + w + r
  p.append(u)

### List of thirds up to seventh

d = [] # List of list of thirds from each root
t = []

for i in p:
  for j, k in enumerate(i):
    if j%2 == 0:
      t.append(k)
  d.append(t)
  t = []

### Remove thirds not present from in in put

q = []
l = [] # List with only present thirds but no accidentals

for i in d:
  for j in i:
    if reg[j] == 1:
      q.append(j)
    else:
      q.append('x')
  l.append(q)
  q = []

### Add back in accidentals

if sharp_mode == 1:
  for i in l:
    for p,j in enumerate(i):
      if j != 'x':
        if sharp_reg[j] == 1:
          i[p] = j + '#'

if flat_mode == 1:
  for i in l:
    for p,j in enumerate(i):
      if j != 'x':
        if flat_reg[j] == 1:
          i[p] = j + 'b'

### Final Readout

print(['1','3','5','7', '9', '11', '13'])
for i in l:
  print(i)
