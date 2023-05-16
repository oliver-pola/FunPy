import sys
import subprocess

# cyclic uninstall all not required packages

# keep pip

keep = ['pip']

done = False
while not done:
	# get not required packages list

	output = subprocess.check_output('pip list --not-required').decode('ascii')
	print(output)
	print('Keep packages: ' + ' '.join(keep))

	freeze = output.replace('\r\n', '\n').split('\n')[2:-1]
	notrequired = [line.split(' ')[0] for line in freeze]
	uninstall = set(notrequired) - set(keep)

	# uninstall
	 
	if uninstall:
		subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', *uninstall])
	else:
		done = True
