# Documentation

## Sytntax
Every element is a top level yaml property. As we cannot have equal properties, you must add a #id to every element, where id is simply a name to it. Probabbly on future versions this will be more useful.

So, the following is valid:

    element#header:
        This is an element
    stuff#content:
        This can be whatever you want
        src:
            some file path idunno

## Tittles
    You can do the equivalent of