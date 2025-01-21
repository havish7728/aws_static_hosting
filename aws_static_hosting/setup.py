from setuptools import setup, find_packages

setup(
    name="aws_static_hosting",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["boto3", "click"],
    entry_points={
        'console_scripts': [
            'aws-static-hosting=aws_static_hosting.cli:cli',
        ]
    },
    description="A Python library to automate static website hosting on AWS",
    author="Havish Gadey",
    author_email="havish.gadey@gmail.com",
    url="https://github.com/havish7728/aws_static_hosting",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
