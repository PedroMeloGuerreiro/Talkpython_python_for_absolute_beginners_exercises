d = {
    "Sam": 7,
    'rolls': ['rock', 'paper', 'scissors'],
    'done': True
}

print(d["Sam"])           # outputs 7
print(d['rolls'])         # outputs ['rock', 'paper', 'scissors']
print(d.get('Sarah'))     # outputs None
print(d.get('Jeff', -1))  # outputs -1
print(d['done'])          # outputs True
