import pip
import subprocess

print('Checking python moduls...')
modules_list = []
modules_list.append('pip')
modules_list.append('numpy')
modules_list.append('matplotlib')
modules_list.append('pyyaml')
modules_list.append('threading')
modules_list.append('Queue')
modules_list.append('httplib')
modules_list.append('urllib')
modules_list.append('random')
modules_list.append('json')
modules_list.append('requests')


# option for pip 

option_up  = '--upgrade'
option_U  = '-U'

print '\n%%%%% List of modules %%%%\n'
pip.main(['list'])
print 'instal and update missing modules...\n'
    
for module in modules_list:
    print 'Checking %s ....' % module
    pip.main(['install', module])
    pip.main(['install',option_U,module])


print '\n%%%%% List of modules %%%%\n'
pip.main(['list'])

print 'test of imports...'
import_dict = {}
import_dict.update({'pyyaml':'yaml'})

for module in modules_list:
    print 'Checking %s ....' % module
    if module in import_dict:
        module = import_dict[module]
    try:
        exec('import '+ module)
    except:
        print 'import problem for %s' % module
    print 'import of %s was successful' % module
        
    
      




