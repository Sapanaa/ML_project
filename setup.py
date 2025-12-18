from setuptools import find_packages, setup

def get_requirements(file_path):
    '''
     Return the requirements 
    '''
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return []

    requirements = []
    for line in lines:
        line = line.strip()

        # ignore editable installs like '-e .' or '--editable'
        if line.startswith('-e') or line.startswith('--editable'):
            continue

        requirements.append(line)

    return requirements

setup(
    name='ml_project',
    packages=find_packages(), # find the init file and then build it 
    version='0.1.0',
    author='sapana',
    license='MIT',
    install_requires= get_requirements('requirements.txt'),
)