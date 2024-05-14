#!/usr/bin/env python
# coding: utf-8

# In[53]:


# this notebook is for exploratory purposes
# to better understand the data 

# loading packages

# basics 

import pandas as pd
import matplotlib.pyplot as plt

# for plots 

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[54]:


# loading all the data

blink = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/Blink.txt',
                    sep='\t', 
                    header=None)

blink_2 = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/Blink2.txt',
                    sep='\t', 
                    header=None)

eyebrow_raise = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/EyebrowRaise.txt',
                    sep='\t', 
                    header=None)

eyebrow_raise_hold = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/EyebrowRaiseHold.txt',
                    sep='\t', 
                    header=None)

look_left = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookLeft.txt',
                    sep='\t', 
                    header=None)

look_left_hold = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookLeftHold.txt',
                    sep='\t', 
                    header=None)

look_right = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookRight.txt',
                    sep='\t', 
                    header=None)

look_right_hold = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookRightHold.txt',
                    sep='\t', 
                    header=None)

look_right_hold_2 = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookRightHold2.txt',
                    sep='\t', 
                    header=None)

look_right_hold_3 = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookRightHold3.txt',
                    sep='\t', 
                    header=None)

look_up = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookUp.txt',
                    sep='\t', 
                    header=None)

look_up_hold = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookUpHold.txt',
                    sep='\t', 
                    header=None)

look_down = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookDown.txt',
                    sep='\t', 
                    header=None)

look_down_hold = pd.read_csv(r'/Users/sfoulsham/Desktop/data3888/Week_7/LookDownHold.txt',
                    sep='\t', 
                    header=None)


# In[55]:


# exploring the basic eye movements:

# blinking, eyebrow raises, looking left, right, up and down 

# looking at the first few rows of blink

print(blink.head())


# In[56]:


# some other basic info for blink

print(blink.info())


# In[57]:


# visualising the basic eye movements

# blinking

blink_plot = px.line(blink, 
                     y=blink[0], 
                     title='Blinking')

blink_plot.update_xaxes(title='Time')
blink_plot.update_yaxes(title='Eye Movement Data')
blink_plot.show()


# In[58]:


# eyebrow raises

eyebrow_raise_plot = px.line(eyebrow_raise, 
                     y=eyebrow_raise[0], 
                     title='Eyebrow Raises')

eyebrow_raise_plot.update_xaxes(title='Time')
eyebrow_raise_plot.update_yaxes(title='Eye Movement Data')
eyebrow_raise_plot.show()


# In[59]:


# looking left

look_left_plot = px.line(look_left, 
                     y=look_left[0], 
                     title='Looking Left')

look_left_plot.update_xaxes(title='Time')
look_left_plot.update_yaxes(title='Eye Movement Data')
look_left_plot.show()


# In[60]:


# looking right

look_right_plot = px.line(look_right, 
                     y=look_right[0], 
                     title='Looking Right')

look_right_plot.update_xaxes(title='Time')
look_right_plot.update_yaxes(title='Eye Movement Data')
look_right_plot.show()


# In[61]:


# looking up

look_up_plot = px.line(look_up, 
                     y=look_up[0], 
                     title='Looking Up')

look_up_plot.update_xaxes(title='Time')
look_up_plot.update_yaxes(title='Eye Movement Data')
look_up_plot.show()


# In[62]:


# looking down 

look_down_plot = px.line(look_down, 
                     y=look_down[0], 
                     title='Looking Down')

look_down_plot.update_xaxes(title='Time')
look_down_plot.update_yaxes(title='Eye Movement Data')
look_down_plot.show()


# In[63]:


# now want to compare holding vs not holding an eye movement 


# In[64]:


# raising eyebrows vs holding an eyebrow raise 

# making sure they have the same x-axis length (did not from previous exploration)

length = min(len(eyebrow_raise), len(eyebrow_raise))

# now doing the plot 

fig = make_subplots(rows=1, 
                    cols=2, 
                    subplot_titles=("Raising Eyebrows", 
                                    "Holding Raising Eyebrows"))

fig.add_trace(go.Scatter(x=eyebrow_raise.index[:length], 
                         y=eyebrow_raise[0][:length], 
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=1)

fig.add_trace(go.Scatter(x=eyebrow_raise_hold.index[:length], 
                         y=eyebrow_raise_hold[0][:length],
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=2)

fig.update_layout(title_text="Eyebrow Raises")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text='Eye Movement Data', row=1, col=1)

fig.show()


# In[65]:


# looking left vs holding a left look 

length = min(len(look_left), len(look_left_hold))

fig = make_subplots(rows=1, 
                    cols=2, 
                    subplot_titles=("Looking Left", 
                                    "Holding Looking Left"))

fig.add_trace(go.Scatter(x=look_left.index[:length], 
                         y=look_left[0][:length], 
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=1)

fig.add_trace(go.Scatter(x=look_left_hold.index[:length], 
                         y=look_left_hold[0][:length],
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=2)

fig.update_layout(title_text="Left")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text='Eye Movement Data', row=1, col=1)

fig.show()


# In[66]:


# looking right vs holding a right look 

length = min(len(look_right), len(look_right_hold))

fig = make_subplots(rows=1, 
                    cols=2, 
                    subplot_titles=("Looking Right", 
                                    "Holding Looking Right"))

fig.add_trace(go.Scatter(x=look_right.index[:length], 
                         y=look_right[0][:length], 
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=1)

fig.add_trace(go.Scatter(x=look_right_hold.index[:length], 
                         y=look_right_hold[0][:length],
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=2)

fig.update_layout(title_text="Right")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text='Eye Movement Data', row=1, col=1)

fig.show()


# In[67]:


# looking up vs holding an up look 

length = min(len(look_up), len(look_up_hold))

fig = make_subplots(rows=1, 
                    cols=2, 
                    subplot_titles=("Looking Up", 
                                    "Holding Looking Up"))

fig.add_trace(go.Scatter(x=look_up.index[:length], 
                         y=look_up[0][:length], 
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=1)

fig.add_trace(go.Scatter(x=look_up_hold.index[:length], 
                         y=look_up_hold[0][:length],
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=2)

fig.update_layout(title_text="Up")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text='Eye Movement Data', row=1, col=1)

fig.show()


# In[68]:


# looking down vs holding a down look 

length = min(len(look_down), len(look_down_hold))

fig = make_subplots(rows=1, 
                    cols=2, 
                    subplot_titles=("Looking Down", 
                                    "Holding Looking Down"))

fig.add_trace(go.Scatter(x=look_down.index[:length], 
                         y=look_down[0][:length], 
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=1)

fig.add_trace(go.Scatter(x=look_down_hold.index[:length], 
                         y=look_down_hold[0][:length],
                         mode='lines',
                         showlegend=False), 
              row=1, 
              col=2)

fig.update_layout(title_text="Down")
fig.update_xaxes(title_text="Time")
fig.update_yaxes(title_text='Eye Movement Data', row=1, col=1)

fig.show()


# In[ ]:





# In[ ]:




