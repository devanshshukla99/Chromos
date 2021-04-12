# Chromos

```
   ____ _                                   
  / ___| |__  _ __ ___  _ __ ___   ___  ___ 
 | |   | '_ \| '__/ _ \| '_ ` _ \ / _ \/ __|
 | |___| | | | | | (_) | | | | | | (_) \__ \
  \____|_| |_|_|  \___/|_| |_| |_|\___/|___/
                                            
```

**Package for getting colored text output in Python.**

## Installation

 * With Wheel File
   * `pip install Chromos\*.whl`
 
 * Building From Source
   * Use `setup.py` either to install or to create the wheel file. 
   * Running `setup.py bdist_wheel` creates a wheel file which can then be used with `pip`.
   * Finally, executing `pip install Chromos\*.whl` installs the wheel file.


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

## Usage

* Use cstr function for the colored text,
  * cstr('\<color> \<bgcolor, optional>  \<attributes>', '\<string>')
* Can also use Individual color functions,
  * blue('\<color>', '\<string>')
  * red('\<color>', '\<string>')
  * Similarly for other colors...
* For Printing an Error Message
  * error_info('\<string>')
  * error_info_b('\<string>')
* For Printing an Info Message
  * info('\<string>')
  * info_y('\<string>')   

## Example

**Illustration of usage**

```python
import Chromos
o = Chromos.Chromos()
```
```python
print(o.cstr("blue", "Hello World! *"))
print(o.blue("Hey Chromos! "))
```

<img src="Imgs/chromos_hey.png" width="500px" height="60px">

**Global Attributes**
```python
o.underline = True
print(o.cstr("yellow", "Good stuff!"))
```
<img src="Imgs/chromos_good_stuff.png" width="500px" height="45px">

```python
o.itallic = True
o.strikethrough = True
print(o.cstr("red", "Alright, alright!"))
```
<img src="Imgs/chromos_alright.png" width="500px" height="45px">

**Local Attributes**
```python
print(o.cstr("yellow underline", "Cool!"))
```
<img src="Imgs/chromos_cool.png" width="500px" height="45px">

```python
print(o.cstr("yellow bgred bf", "Great!"))
```

<img src="Imgs/chromos_great.png" width="500px" height="45px">

**Function For Printing an Error Message**
```python
o.error_info("This is an Error Msg!" )
```
<img src="Imgs/chromos_error.png" width="500px" height="45px">

**Function For Printing an Info Message**
```python
o.info_y("This is an Info Msg!" )
```
<img src="Imgs/chromos_info.png" width="500px" height="45px">
