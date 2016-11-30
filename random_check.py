#!/usr/bin/env python
import random
name_list = ['yu-pon', 'mattsun', 'shinshin', 'mae-chan', 'takatan','nisshi-']
result = {}
for name in name_list:
  choice = random.randint(1,6)
  while choice in result.values():
    choice = random.randint(1,6)
  result[name] = choice
print(result)
