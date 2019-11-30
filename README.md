# Prompt
Python module to create simple colored and interactive prompt

## use Example

```python
#!/usr/bin/env python3

from Prompt.prompt import Prompt
from Prompt.check import check_length, check_int

def echo( args ):
    print( " ".join( args ))
    return True

@check_length( 2 )
@check_int
def sum_2_numbers( args ):
    print( sum( args ))
    return True

@check_int
def sum_numbers( args ):
    print( sum( args ))
    return True

prompt = Prompt(debug=True)

prompt.set( "query", "Input? -->" )

prompt.addApp( "echo", echo, "Echo the given arguments" )
prompt.addApp( "add", sum_2_numbers, "Sum 2 numbers given in arguments" )
prompt.addApp( "sum", sum_numbers, "Sum all the numbers given in arguments" )

if __name__ == '__main__':
    prompt.run()
```
