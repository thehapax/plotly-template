# plotly-template

<h4> Dexbot visualization guidelines</h4>

<li> Privacy
<li> Pandas Time Series
<li> Real Time Updates
<li> Interactivity
<li> local webserver driven display

1. Privacy: Plot.ly will serve your data publically if privacy settings are on. 
all code using plot.ly should have in configuration sharing set to private, or else end user 
data can be shared publically.

2. Pandas: Dexbot data prechart should be managed in pandas. 
This library is geared for financial applications and easier to manage large amounts of financial data dynamically. 
Do not use numpy arrays or javascript arrays for handling and parsing data

3. Real Time Updates. Plot.ly enables real time updates to charts. see https://plot.ly/python/sending-data-to-charts/

4. Interactivity: Plot.ly enables end users to modify and filter data views.  https://plot.ly/python/figurewidget-app/       

5. Local data display:  Use plotly offline from command line to enable html to be displayed inside of a website page.
plot.ly runs a webserver locally when plot() is used. https://plot.ly/python/offline/#plotly-offline-from-command-line

<b>Todo:</b> Integration with existing PyQT5 desktop app or pywebview should be doable. This is a todo for investigation. 


<h5> Links to additional resources: </h5>

https://plot.ly/pandas/time-series/                                                                                      
https://plot.ly/python/candlestick-charts/                                                                               
https://towardsdatascience.com/python-for-finance-dash-by-plotly-ccf84045b8be
https://plot.ly/python/user-guide/   
