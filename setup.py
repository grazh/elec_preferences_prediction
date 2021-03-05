from distutils.core import setup
import py2exe
 
setup(
    windows=[{"script":"extract_data.py"}],
    options={"py2exe": {"includes":["sip"]}}
)