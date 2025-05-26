from distutils.core import setup
from pathlib import Path


# Use importlib.metadata instead of pkg_resources (which is deprecated)
try:
    from importlib.metadata import distribution, PackageNotFoundError
except ImportError:
    # For Python < 3.8
    from importlib_metadata import distribution, PackageNotFoundError


def get_install_requires():
    """Returns requirements.txt parsed to a list"""
    fname = Path(__file__).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets


def is_package_installed(package_name):
    """Check if a package is installed using importlib.metadata"""
    try:
        distribution(package_name)
        return True
    except PackageNotFoundError:
        return False


requirements = get_install_requires()

# Check if MolScribe is installed, if not add it to dependencies
if not is_package_installed('MolScribe'):
    requirements.append('MolScribe @ git+https://github.com/alexey-krasnov/MolScribe')

setup(name='RxnScribe',
      version='1.0',
      description='RxnScribe',
      author='Yujie Qian',
      author_email='yujieq@csail.mit.edu',
      url='https://github.com/Ozymandias314/MolDetect',
      packages=['rxnscribe', 'rxnscribe.inference', 'rxnscribe.pix2seq', 'rxnscribe.transformer'],
      package_dir={'rxnscribe': 'rxnscribe'},
      package_data={},
      setup_requires=['numpy'],
      install_requires=requirements,
      )