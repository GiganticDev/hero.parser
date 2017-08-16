# Gigantic Parser Module

A Module to Parse Data from *Motiga's* **Gigantic**

## Purpose:
This community built API is made with the hopes of grabbing as much Hero data as possible. This will allow people to learn more about their favorite hero. 

## Installation:

#### For Production:
```
pip install .
```

#### For development:
```
pip install -e .[development]
```

Run `python -m gigantic.parser` in the 'RxGame' directory of your gigantic folder and it will print out json parsed output.
You may use `python -m gigantic.parser > target_file.json` to output this to a file.


## TODO: 

* Successfully Parse references to ALL game heroes.
* Change In Game Names with Official Character Name.
* A Method to Store this information.
