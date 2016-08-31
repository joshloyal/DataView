from setuptools import setup


PACKAGES = [
        'dataview',
        'dataview.data',
        'dataview.tests',
]

def setup_package():
    setup(
        name="DataView",
        version='0.1.0',
        description='Library of Datasets with Munging Capabilities Built In',
        author='Joshua D. Loyal',
        url='https://github.com/joshloyal/DataView',
        license='MIT',
        install_requires=['numpy', 'scipy', 'scikit-learn', 'pandas'],
        packages=PACKAGES,
    )


if __name__ == '__main__':
    setup_package()
