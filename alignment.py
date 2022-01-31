import numpy
from axes import Axes
import matplotlib.pyplot

class Alignment:

  def __init__(self, nrows, ncols):

    self._figure = matplotlib.pyplot.figure()

    self._left, self._right, self._top, self._bottom = [], [], [], []

    self._array = numpy.empty(shape=(nrows, ncols), dtype=object)
    
    for row_idx, row in enumerate(self.array()):
      for col_idx, value in (enumerate(row)):

        value = Axes(self)
        self.array()[row_idx][col_idx] = value
        
        if row_idx in [0]:            
          self._top.append(value)
        
        if row_idx == (nrows - 1):     
          self._bottom.append(value)
        
        if col_idx in [0]:            
          self._left.append(value)
        
        if col_idx == (len(row) - 1): 
          self._right.append(value)

  def figure(self):
    return self._figure

  def array(self):
    return self._array

  def left(self):
    return self._left

  def right(self):
    return self._right
  
  def top(self):
    return self._top
  
  def bottom(self):
    return self._bottom

  def array(self):
    return self._array

  def figure_size(self):
    fig_w = 0.0
    fig_h = 0.0
    for r, row in enumerate(self):
      row_w = 0.0
      row_h = 0.0
      for c, ax in enumerate(row):
        w = ax.total_width()
        h = ax.total_height()
        row_w += w
        if row_w > fig_w: fig_w = row_w
        if h > row_h: row_h = h
      fig_h += row_h
    size = (fig_w, fig_h)
    return size
  
  def __repr__(self):
    return f'Alignment({self.array()})'

  def __len__(self):
    return self.array().__len__()

  def __getitem__(self, idx):
    return self.array().__getitem__(idx)

  def __iter__(self):
    return self.array().__iter__()

  def flatten(self):
    return self.array().flatten()