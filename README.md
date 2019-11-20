# REGO

One-Click Registry Management Tool with GUI

## Getting Started

### Prerequisites

Following python modules are required

```
pip install pyqt5
pip install jsondiff
```

### Installing


```
git clone https://github.com/SecOfSW/rego
```


## Running the tools

After Clone, just run `REGO_main.py`

```
python3 ./REGO_main.py
```

or run executable file

```
REGO.exe
```

### Functions

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
<u> Only DarkMode/WhiteMode works for now. </u>
We will update later.


## Built With

* [Python3.7](https://www.python.org/)


## Authors

* **Jinwoo Choi** - *Initial work*
* **Yeonseok Jang** - *Initial work* - [7illume21](https://github.com/7illume21)
* **Sangwon Shin** - *Initial work* - [husask11](https://github.com/husask11)
* **Taejun Lee** - *Initial work* - [HckEX](https://github.com/HckEX)


## License

This project is licensed under the MIT License
