import sys
a,b=int(sys.argv[1]),int(sys.argv[2])
ps=open('src/paras.txt',encoding='utf-8').read().split('\n\n')
print('\n\n'.join(ps[a:b]))
