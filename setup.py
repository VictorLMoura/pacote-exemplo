from setuptools import setup

setup(name='dev_aberto_victorlm2',
        version='0.1',
        packages=['dev_aberto'],
        author="Victor Laperuta",
        author_email="victorlm2@al.insper.edu.br",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        install_requires=[
            'requests'
        ],
        scripts=['scripts/hello.py']
     )

