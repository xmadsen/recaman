# Recamán sequence plot
A Python script to represent graphically the [Recamán sequence](http://mathworld.wolfram.com/RecamansSequence.html) in matplotlib.

### Usage

`python recaman_plot.py`*`max_size drawtype`*

where max_size determines the length of the Recamán sequence to calculate, and drawtype can be any of the following:
* *line* - Renders a connected scatter plot.
* *circle* - Renders a circle of diameter *i* for each index *i* of the sequence, centered exactly between 
* *point* - Renders a scatter plot with dots for each element.
* *arcs* - *In Progress*

I plan to fix arcs to be semicircles between adjacent points like a wavy ribbon, rather than the hacky method it uses now.
