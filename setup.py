import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    name="galois_field",
    version="2.1.1",
    author="Sakoda Takuya",
    author_email="sakodata0318@gmail.com",
    description="Galois Field: GF(p^n)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/syakoo/galois_field",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    test_requires=["pytest"],
    python_requires='>=3.8',
)
