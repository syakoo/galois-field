# Galois Field GF(p^n) for 🐍

This is a library for using Galois Field GF(p^n) in Python,
which generates GF(p) and GF(p^n) and allows you to multiply, add, subtract, and divide elements.
[For Japanease](https://github.com/syakoo/galois-field/blob/master/README.ja.md)

## Assumed Environment

- Python 3.8 ~

## Features

- Generating GF(p) and GF(p^n).
- Generating an element of Galois Field. (from modulus operation)
- Four Arithmetic operations over GF(p^n).
- Compute the inverse of an element in GF(p^n).

## Usage

### Installation

You can install with `pip`:

```bash
$ pip install git+https://github.com/syakoo/galois-field
```

### Examples

#### GF(11)

```python
from galois_field import GFp

# Generating the field GF(11)
gf = GFp(11)

# Generating an element in GF(11)
el1 = gf.elm(5)  # 5 (mod 11)
el2 = gf.elm(13) # 2 (mod 11)

# Arithmetics
el1 + el2 # 7 (mod 11)
el1 - el2 # 3 (mod 11)
el1 * el2 # 10 (mod 11)
el1 / el2 # 8 (mod 11)

# The Inverse of elements.
el1.inverse() # 9 (mod 11)
el2.inverse() # 6 (mod 11)
```

#### GF(5^4)

We use a monic irreducible polynomial. (in this case, x^4 + 2)

```python
from galois_field import GFpn

# Generating the field GF(5^4)
gf = GFpn(5, [1, 0, 0, 0, 2])

# Generating an element in GF(5^4)
el1 = gf.elm([1, 2])  # 1x + 2
el2 = gf.elm([1, 2, 3, 4, 5]) # 2x^3 + 3x^2 + 4x + 3

# Arithmetics
el1 + el2 # 2x^3 + 3x^2
el1 - el2 # 3x^3 + 2x^2 + 2x + 4
el1 * el2 # 2x^3 + 1x + 2
el1 / el2 # 3x^3 + 4x^2

# The Inverse of elements.
el1.inverse() # 3x^3 + 4x^2 + 2x + 1
el2.inverse() # 1x^3 + 1x^2 + 2x + 1
```

### Cautions

- The range of values is up to `2^64 bits`, with a maximum of `2^32 bits` to ensure that the product gets the right value, and up to ten decimal digits.
- Please note that even if you use a value within the range, the value is not guaranteed with certainty. (We take no responsibility for this.)

## Contribute

This library has a lot of features we want to add and we are looking for contributors. Please feel free to add `Issues` and `PullRequest`.

### Development environment

Please set up your development environment with the following command:

#### Creating and activating the virtual environment `.venv`

```bash
$ python -m venv .venv
$ source .venv/bin/activate
```

#### Installing dependencies

```bash
$ pip install -r requirements.dev.txt
```

#### Testing

```bash
$ pytest
```

#### Formatting test

```bash
$ flake8 galois_field
```

## LICENSE

MIT LICENSE
