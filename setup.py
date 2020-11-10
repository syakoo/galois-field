import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    name="galois_field_pn",
    version="0.1.0",
    author="Sakoda Takuya",
    author_email="sakodata0318@gmail.com",
    description="galois_field_pn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/syakoo/galois_field_pn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': ['galois_field_pn = src.GF_pn:GF_pn']
    },
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    test_requires=["pytest"],
    python_requires='>=3.8',
)
