from setuptools import setup


setup(
    name="clitodo",
    version="1.0",
    py_modules=["todo"],
    install_requires=['Click', "plyvel"],
    entry_points="""
        [console_scripts]
        todo=clitodo:cli
        """
)
