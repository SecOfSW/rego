# REGO

One-Click Registry Management Tool with GUI

## Getting Started

### OS
Windows10

### Installing

```
git clone https://github.com/SecOfSW/rego.git
```

### Requirement

Following python modules are required

```
pip install -r requirements.txt
```

## Running the tools

***__Need to be run as ADMINISTRATOR privilege__***

After cloning the repo, just run `REGO_main.py`

```
python3 ./REGO_main.py
```

or run executable file at release page

```
REGO.exe
```

### Functions

<u> Database is not fully prepared yet... </u>

- **Scan**
Scan security related registry based on our database.
- **Monitor**
Monitoring registry based on our database.
- **Dump**
Dump registry related to users.
`HKEY_CURRENT_USER` and `HKEY_USERS` will be dumped.
Also, support making diff of two dump files.
- **Utility**
Activate functions with one-click.


## Built With

* [Python3.7](https://www.python.org/)


## Authors

* **Jinwoo Choi** - *Initial work*
* **Yeonseok Jang** - *Initial work* - [7illume21](https://github.com/7illume21)
* **Sangwon Shin** - *Initial work* - [husask11](https://github.com/husask11)
* **Taejun Lee** - *Initial work* - [HckEX](https://github.com/HckEX)


## License

This project is licensed under the MIT License
