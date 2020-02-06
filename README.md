# SmallCompanyHierarchy

## Requirements:

 - [python3+](https://www.python.org/downloads/)

 - [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Quick start:

The guide below is for Unix based systems. Few steps may differ for Windows based systems.

After cloning the repository, set up the isolated python environment:

`$> virtualenv -p <your/path/to/python3/binary> env`

`$> source env/bin/activate`

Install the required python packages listed in requirements.txt with pip:

`$> pip install -r requirements.txt`

Execute the python file with the interpreter:

`$> python small_company.py`

## Details

If you open small_company.py, you will see that the dataset `employees` at the top declares the  relationships between employees and managers.
The goal of this program is to display a tree representation of this data :

```
Jamie
├── Allan
│   ├── Martin
│   └── Alex
└── Steve
    └── David
```
