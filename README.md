
```
   ____ _                                   
  / ___| |__  _ __ ___  _ __ ___   ___  ___ 
 | |   | '_ \| '__/ _ \| '_ ` _ \ / _ \/ __|
 | |___| | | | | | (_) | | | | | | (_) \__ \
  \____|_| |_|_|  \___/|_| |_| |_|\___/|___/
                                            
```

<br>

![Build](https://github.com/devanshshukla99/Chromos/actions/workflows/main.yml/badge.svg)

<hr>

Package for getting colored text output in Python.

<hr>

## Installation

- With Wheel File

```console
pip install Chromos\*.whl`
```

- Building From Source

```python
python setup.py install
```

<hr>

## Attributes Supported:

 **Text:**
   * Bold (default=True)
   * Itallic (default=False)
   * Underline (default=False)
   * Blink (default=False)
   * Strikethrough (default=False)
   
 **Text Colors:**
   * Black
   * Red
   * Green
   * Yellow
   * Blue
   * Purple
   * Cyan
   * White

 **Background Colors:**
   * Black  (default)
   * Red
   * Green
   * Yellow
   * Blue
   * Purple
   * Cyan
   * White

<hr>

## Usage

- Use `cstr` function for the colored text,
  
```python
  cstr(attributes, string)
```

- Can also use individual color functions,

```python
blue(color, string)
# Similarly for other color functions
```  

- For printing an error message

```python
# Use error_info or error_info_b
error_info("Error occured!")
```

- For printing an info message

```python
# Use info or info_y
info("Just informing about the new release :P")
```

<hr>

## Example

Illustration of usage

```python
import Chromos
o = Chromos.Chromos()
```

```python
print(o.cstr("blue", "Hello World! *"))
print(o.blue("Hey Chromos! "))
```

<img src="docs/imgs/chromos_hey.png" width="500px" height="60px">

Global Attributes
```python
o.underline = True
print(o.cstr("yellow", "Good stuff!"))
```
<img src="docs/imgs/chromos_good_stuff.png" width="500px" height="45px">

```python
o.itallic = True
o.strikethrough = True
print(o.cstr("red", "Alright, alright!"))
```
<img src="docs/imgs/chromos_alright.png" width="500px" height="45px">

Local Attributes
```python
print(o.cstr("yellow underline", "Cool!"))
```
<img src="docs/imgs/chromos_cool.png" width="500px" height="45px">

```python
print(o.cstr("yellow bgred bf", "Great!"))
```

<img src="docs/imgs/chromos_great.png" width="500px" height="45px">

Function For Printing an Error Message
```python
o.error_info("This is an Error Msg!" )
```
<img src="docs/imgs/chromos_error.png" width="500px" height="45px">

Function For Printing an Info Message
```python
o.info_y("This is an Info Msg!" )
```
<img src="docs/imgs/chromos_info.png" width="500px" height="45px">
