# Chromos

```
   ____ _                                   
  / ___| |__  _ __ ___  _ __ ___   ___  ___ 
 | |   | '_ \| '__/ _ \| '_ ` _ \ / _ \/ __|
 | |___| | | | | | (_) | | | | | | (_) \__ \
  \____|_| |_|_|  \___/|_| |_| |_|\___/|___/
                                            
```

**Package for gettting colored text output in Python.**

## Installation

 * With Wheel File

   * **pip install Chromos\*.whl**

## Attributes Supported:

 * Text:
   * Bold (default=**True**)
   * Underline (default=**False**)
   * Negative styles (default=**False**)

 * Text Colors:
   * Black
   * Red
   * Green
   * Yellow
   * Blue
   * Purple
   * Cyan
   * White
   
 * Background Colors:
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
Illustration of usage

	import Chromos
	o = Chromos.Chromos()
	print(o.cstr("blue", "Hello World! *"))
	print(o.blue("Hey Chromos! "))

