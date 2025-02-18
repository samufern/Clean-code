# Clean Code Project

## 📌 Project Overview
This project is focused on **clean coding practices** while implementing a simple **text encoding and decoding system**. It also includes functionality for handling JSON-based vaccine management requests.

## 🚀 Getting Started

### 📋 Prerequisites
Ensure you have the following installed before running the project:

- Python 3.x
- PyBuilder (for project automation)

Install dependencies using:
```sh
pip install -r requirements.txt
```

### 🔧 Installation
Clone the repository:
```sh
git clone https://github.com/your_username/Clean-Code.git
cd Clean-Code
```

## 🏗 Project Structure
```
Clean-Code/
│── Main.py                 # Main program execution
│── requirements.txt        # Required dependencies
│── test.json               # Test input file
│── Normativa_de_codigo.pdf # Coding standards documentation
│── Proyecto/               # Subdirectory for package-related files
│    ├── README.md          # Documentation
│    ├── build.py           # PyBuilder automation script
│    ├── pyproject.toml     # Project build system configuration
│    ├── setup.py           # Package installation setup
│    ├── requirements.txt   # Additional dependencies
│    ├── test_100.json
│    ├── test_101.json
│    ├── test_102.json
│    ├── test_103.json
│    ├── test_104.json
│    ├── test_105.json
│    ├── test_106.json
│    ├── test_ok.json       # Expected successful cases
│    ├── test_ok_2.json
│    ├── JsonFiles/         # JSON test cases
│        ├── cancelled_store.json
│        ├── store_date.json
│        ├── store_patient.json
│        ├── store_patient_manipulated.json
│        ├── store_vaccine.json
│        ├── RF2/          # Additional JSON validation cases
│            ├── store_patient_manipulated.json
│            ├── test_dup_all.json
│            ├── test_dup_char_plus.json
│            ├── test_dup_colon.json
│            ├── test_dup_comillas.json
│            ├── test_dup_comma.json
```

## 🎯 Usage

### Running the Main Program
To run the main encoding/decoding functionality:
```sh
python Main.py
```
This script encodes a given text and then decodes it to verify correctness.

### Running with JSON Input
To test JSON-based request handling:
```sh
python Main.py test.json
```

## ✅ Testing
Test files are provided in the `Proyecto/JsonFiles/` directory, covering:
- Vaccine storage scenarios
- Patient data manipulation
- Error detection in JSON formatting

## 🛠 Built With
- [Python 3](https://www.python.org/)
- [PyBuilder](https://pybuilder.io/)

## 🤝 Contributing
Feel free to fork the repository, make improvements, and submit a pull request.

## 📜 License
No license file included. Please add one if necessary.

## 🎁 Acknowledgments
Thanks to the developers contributing to PyBuilder for making project automation easier.

---
Made with ❤️ by [Your Name]

