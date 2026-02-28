# passdict
A Python tool for generating personalized password lists.

> **Note:** This tool is designed for educational purposes only. The author is not responsible for any illegal use.

## Description
passdict is a Python-based password list generator that creates unique, personalized password combinations based on information you provide, such as your name, surname, gender, hobbies, and favorite movies. It is useful for security research and understanding how personal information can be used to guess passwords.

## Screenshots
![passdict screenshot](images/screenshot.png)

## Getting Started

### Dependencies
* Linux
* Python 3.x
* pip or [Poetry](https://python-poetry.org)

### Installing

* Clone the repository:
```bash
git clone https://github.com/dincertekin/passdict.git
cd passdict/
```

* Install with pip:
```bash
pip install -r requirements.txt
```

* Or install with Poetry:
```bash
poetry install
```

### Executing program

* Run the tool:
```bash
python passdict.py
```

## Help
If you run into dependency issues, make sure you are using Python 3 and that pip is up to date.

```bash
pip install --upgrade pip
```

## Contributing
Contributions are welcome! To get started:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please open an issue first for major changes to discuss what you'd like to change.

## License
This project is licensed under the [Apache-2.0](LICENSE) License - see the LICENSE.md file for details

## Acknowledgments
* Inspired by Mebus's [cupp](https://github.com/Mebus/cupp)
