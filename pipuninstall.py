import sys
import subprocess


def get_pip_output_and_list(argument):
	if argument:
		argument = ' ' + argument
	output = subprocess.check_output('pip list' + argument).decode('ascii')
	freeze = output.replace('\r\n', '\n').split('\n')[2:-1]
	return output, [line.split(' ')[0] for line in freeze]


def get_pip_list(argument):
	output, list = get_pip_output_and_list(argument)
	return list


# uninstall packages from arguments, exclude argv[0] which is scriptname
args = sys.argv[1:]

# get not-required packages, that user installed manually
installed = get_pip_list('--not-required')

# color might be messed up even in the previous process, just reset
print('\033[0m', end='')

uninstall = set(args).intersection(set(installed))
conflict = set(args) - uninstall
if conflict:
	print("\033[93mWARNING: Can't uninstall packages, requiered by dependencies: " + ' '.join(conflict))
	print('\033[0m')
	
if uninstall:
	subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', *uninstall])
else:
	print('No packages to uninstall')

# color might be messed up even in the previous process, just reset
print('\033[0m', end='')

# check not-required packages again, maybe some old dependency got removed, but package remains installed
done = False
while not done:
	notrequired = get_pip_list('--not-required')

	uninstall = set(notrequired) - set(installed)
	if uninstall:
		print()
		subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-y', *uninstall])
	else:
		done = True
