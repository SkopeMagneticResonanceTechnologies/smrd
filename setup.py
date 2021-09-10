import os
from setuptools import setup, find_packages
from distutils.command.build import build
from distutils.command.build_py import build_py

import logging
import shutil
from pathlib import Path
import re 

logging.basicConfig()
log_ = logging.getLogger(__name__)

schema_file = os.path.join('schema','smrd.xsd')
config_file = os.path.join('schema','.xsdata.xml')

class my_build_py(build_py):
    def run(self):
        # honor the --dry-run flag
        if not self.dry_run:
            outloc = self.build_lib
            outloc = os.path.join(outloc,'smrd/xsd/ismrmrdschema')

            
            generate_schema(schema_file, config_file, outloc)
                    # distutils uses old-style classes, so no super()
        build_py.run(self)


def fix_init_file(package_name,filepath):

    with open(filepath,'r+') as f:
        text = f.read()
        text = re.sub(f'from {package_name}.smrd', 'from .smrd',text)
        f.seek(0)
        f.write(text)
        f.truncate()




def generate_schema(schema_filename, config_filename, outloc  ):
    def to_uri(filename):
        return Path(filename).absolute().as_uri()

    import sys 
    import subprocess
    
    subpackage_name = 'ismrmrdschema'
    args = [sys.executable,'-m','xsdata', str(schema_filename), '--config',str(config_filename), '--package',subpackage_name]
    subprocess.run(args)
    fix_init_file(subpackage_name,f"{subpackage_name}/__init__.py")
    shutil.rmtree(os.path.join(outloc,subpackage_name),ignore_errors=True)
    shutil.move(subpackage_name,outloc)

setup(
    name='smrd',
    version='1.0.8',
    author='MRD Developers',
    author_email='software@skope.ch',
    description='Python implementation compatible with the version of the MRD format used by Skope',
    license='Public Domain',
    keywords='smrd',
    url='https://github.com/SkopeMagneticResonanceTechnologies/ismrmrd',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
        ],
    install_requires=['xsdata>=21', 'numpy', 'h5py>=2.10'],
    setup_requires=['nose>=1.0', 'xsdata[cli]>=21', 'jinja2 >= 2.11'],
    test_suite='nose.collector',
    cmdclass={'build_py':my_build_py}
)
