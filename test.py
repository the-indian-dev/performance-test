from subprocess import Popen, PIPE
from datetime import datetime
from time import sleep
import numpy as np
import matplotlib.pyplot as plt

res = {}

print('Starting C test')

process = Popen(['gcc', 'bruh.c'])
sleep(1)
start = datetime.now()
process = Popen(['./a.out'], stdout=PIPE, stderr=PIPE)
end = datetime.now()
res['C'] = ((end - start).microseconds)

print('Starting C++ test')

process = Popen(['g++', 'bruh.cpp'])
sleep(1)
start = datetime.now()
process = Popen(['./a.out'], stdout=PIPE, stderr=PIPE)
end = datetime.now()
res['C++'] = ((end - start).microseconds)

print('Starting JAVA test')

sleep(1)
start = datetime.now()
process = Popen(['java','bruh.java'], stdout=PIPE, stderr=PIPE)
end = datetime.now()
res['JAVA'] = ((end - start).microseconds)

print('Starting CPython3 test')

sleep(1)
start = datetime.now()
process = Popen(['python3', 'bruh.py'], stdout=PIPE, stderr=PIPE)
end = datetime.now()
res['Python3'] = ((end - start).microseconds)


print('Starting Node.js test')

sleep(1)
start = datetime.now()
process = Popen(['node', 'bruh.js'], stdout=PIPE, stderr=PIPE)
end = datetime.now()
res['node.js'] = ((end - start).microseconds)


print('Starting Dart test')

sleep(1)
start = datetime.now()
process = Popen(['dart','run','bruh.dart'], stdout=PIPE, stderr=PIPE)
end = datetime.now()
res['dart'] = ((end - start).microseconds)
print(res)
courses = list(res.keys())
values = list(res.values())

fig = plt.figure(figsize = (10,10))

# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)

plt.xlabel("Language")
plt.ylabel("Time Taken")
plt.title("Time taken to run per language")
plt.show()

