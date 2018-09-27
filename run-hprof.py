import os
import subprocess

benchmarks = ['avrora', 'batik', 'fop', 'h2', 'jython', 'luindex', 'lusearch', 'pmd', 'tomcat', 'xalan']


for b in benchmarks:
	command = 'java -agentlib:hprof=cpu=samples,file=profiles/hprof/%s-samples.hprof,interval=1,depth=10 -jar dacapo-9.12-MR1-bach.jar %s -n 30' % (b, b)

	print('Running benchmark %s' % b)
	try:
		subprocess.run(command, shell=True, check=True)
	except:
		print('Error on benchmark %s' % b)
		continue
	print('Benchmark run successfully')

	




