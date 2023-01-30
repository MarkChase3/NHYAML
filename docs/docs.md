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
You can do the equivalent of an # on markdown easily by putting a center-text property on your file.
Example:

    center-text#header:
        Page tittle
    center-text#another:
        Another tittle

## Text
Just put a text element on the same way with the tittles!
## Images
Just put a fig element, set the src and text (caption) on the sons of that element and you have it.
Example:

    center-text#header:
        NHYAML
    text#content:
        My bad logo was made in paint. Look
    fig#logo:
        src:
            https://markchase3.github.io/NHYAML.png
        text:
            The logo

## Link on images
Do the same as above but with fig-link and add a link son!
This was made for help me in my [blog](https://markchase3.github.io/), and the language will grow with it!
Example:
    fig-link#image:
        src:
            https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png
        text:
            Wikipedia man
        link:
            https://www.wikipedia.org

## GRIDS
Probably the best of NHYAML are grids, just use a grid-5 or grid-3 elements and inside them put more elements, they will wrap automaticcaly.
Pratical Example:
    center-text#header:
        Bisteca

    grid-5#header:
        fig-link#DownToTheCenterFig:
            src:
            DownToTheCenter.png
            text:
                A demo-game where you can explore dungeons in an old mine until the eart's center
            link:
                DownToTheCenter/post.html
        fig-link#NHYAMLFig:
            src:
            YAML.png
            text:
                A yaml markup language that powers this blog!
            link:
                NHYAML/post.html
    center-text#footer:
        "That's it! Go back here later to see more posts!"

The code from my blog homepage.

## Compiling

Put your code in a file named blog.py and call NHYAML.py using pyhton, copy and paste the result on a html and you are ready to go!
that's basiccaly it! For now...
