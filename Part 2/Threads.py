# zad4   ###########################################
# zaimplementować wielowatkowe liczenie histogramu
# (monitorowac wykonanie htop)
#####################################################
import threading
from collections import Counter
import subprocess

data = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e', 'e']
l = int(len(a)/2)


def count_histogram(data):

    counts = Counter(data)
    width = 16
    longest_key = max(len(key) for key in counts)
    graph_width = width - longest_key - 2
    widest = counts.most_common(1)[0][1]
    scale = graph_width / float(widest)
    #result = subprocess.run('htop', stdout=subprocess.PIPE)
    #result.stdout.decode('utf-8')
    for key, size in sorted(counts.items()):
        print('{}: {}'.format(key, int(size * scale) * '*'))


thread = threading.Thread(target=count_histogram(data[0:l+1]))
thread2 = threading.Thread(target=count_histogram(data[l+1:]))
thread.setDaemon(True)
thread2.setDaemon(True)
thread.start()
thread2.start()

thread.join()
thread2.join()
