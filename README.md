
# PyBin

**PyBin** is a Python bytecode compiler that produces `.pybin` files instead of `.pyc` files, supporting multiple optimization levels and parallel processing.

## 🚀 Features
- Compile Python files to `.pybin` format.
- Supports multiple optimization levels (`-O`, `-OO`).
- Parallel compilation for faster results.

## 📦 Installation
Currently, PyBin is not available on PyPI. You can clone this repository:

```bash
git clone https://github.com/zimoshi/PyBin.git
cd pybin
pip install .
```

## 🧑‍💻 Usage
```bash
pybin -r 2 -f -j 4 myproject/
```
or:
```bash
python -m pybin.org -r 2 -f -j 4 myproject/
```

## 🤝 Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License
This project is licensed under the MIT License.
