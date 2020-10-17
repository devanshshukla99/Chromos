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
   * **pip install Chromos\*.whl**
 
 * Building From Source
   * Use **setup.py** either to install or to create the wheel file. 
   * Running **setup.py bdist_wheel** creates a wheel file which can then be used with **pip**.
   * Finally, executing **pip install Chromos\*.whl** installs the wheel file.


## Attributes Supported:

 **Text:**
   * Bold (default=**True**)
   * Itallic (default=**False**)
   * Underline (default=**False**)
   * Blink (default=**False**)
   * Strikethrough (default=**False**)
   
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
   * Black
   * Red
   * Green
   * Yellow
   * Blue
   * Purple
   * Cyan
   * White

## Usage
* Use cstr function for the colored text,
  * cstr(self, color, string)
* Can also use Individual color functions,
  * blue(self, string)
  * red(self, string)
  * etc....

## Example

**Illustration of usage**

```python
import Chromos
o = Chromos.Chromos()
print(o.cstr("blue", "Hello World! *"))
print(o.blue("Hey Chromos! "))
```

![Alt text](Imgs/chromos_img.png)
