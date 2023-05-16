import sys
import subprocess


# example how to freeze updates for certain packages, because others are just too specific about their dependencies 

# example output (outdated) which lead to the decision to reverse and then freeze updates:
# tensorflow 2.3.1 requires tensorflow-estimator<2.4.0,>=2.3.0, but you have tensorflow-estimator 2.4.0 which is incompatible.
# tensorboard 2.10.1 requires google-auth-oauthlib<0.5,>=0.4.1, but you have google-auth-oauthlib 0.5.3 which is incompatible.
# tensorboard 2.10.1 requires protobuf<3.20,>=3.9.2, but you have protobuf 4.21.7 which is incompatible.
# matplotlib 3.6.0 requires numpy>=1.19, but you have numpy 1.18.5 which is incompatible.
# requests 2.28.1 requires charset-normalizer<3,>=2, but you have charset-normalizer 3.0.0 which is incompatible.
# notebook 6.5.1 requires nbclassic==0.4.5, but you have nbclassic 0.4.7 which is incompatible.

# frozen = ['charset-normalizer', 'gast', 'google-auth-oauthlib', 'h5py', 'matplotlib', 'nbclassic', 'numpy', 'protobuf', 'tensorflow', 'tensorflow-estimator']
frozen = []


def get_pip_output_and_list(argument):
	if argument:
		argument = ' ' + argument
	output = subprocess.check_output('pip list' + argument).decode('ascii')
	freeze = output.replace('\r\n', '\n').split('\n')[2:-1]
	return output, [line.split(' ')[0] for line in freeze]


def get_pip_list(argument):
	output, list = get_pip_output_and_list(argument)
	return list


# get outdated packages list
output, outdated = get_pip_output_and_list('--outdated')

# previous pip call may output colored warning about upgrading pip itself, 
# but seems to forget to reset this warning color, so we have to do that
print('\033[0m' + output)

if frozen:
	print('Frozen packages: ' + ' '.join(frozen))

update = set(outdated) - set(frozen)
if update:
	print()

	# get not-required packages, that user installed manually
	installed = get_pip_list('--not-required')

	# color might be messed up even in the previous process, just reset
	print('\033[0m', end='')

	subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', *update])

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

else:
	if frozen:
		print('Everything else up to date')
	else:
		print('Everything up to date')
