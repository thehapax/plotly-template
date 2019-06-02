# plotly-template for dexbot

<h4> Working Document: Dexbot visualization guidelines</h4>
<ul>
<li> Privacy
<li> Pandas Time Series
<li> Real Time Updates
<li> Interactivity
<li> local webserver offline display
</ul>

1. Privacy: Plot.ly will serve your data publically if privacy settings are not set. Also plot settings by default will redirect users to register for an account online. Dexbot desktop app should be able to retain information locally. In order to do so, all code using plot.ly should have in configuration sharing set to private, or else end user data can be shared publically. see sample code in this repository. see privacy-local-sample.py for points #1, 2, 5

If you want to use the online account, for the community edition that is free, this is the message given:
`Accounts on the Community Plan cannot save private files.  You can still save unlimited public files on Plotly, or you can upgrade your account to be able to save private files. UPGRADE HERE: https://plot.ly/products/cloud 
To make a file public in the API, set the optional argument 'world_readable' to True.`

2. Pandas: Dexbot data prechart should be managed in pandas. There are 7 different ways in which time series data can be charted. I would advise using the pandas as much as possible to be consistent instead of js. It is also more powerful and less code to maintain. The pandas library is geared for financial applications and easier to manage large amounts of financial data dynamically. would also advise against numpy arrays or javascript arrays for handling and parsing data. Use javascript framework only if absolutely necessary. 

3. Real Time Updates. Plot.ly enables real time updates to charts. need to modify sample code to use plotly.offline for local display.  see https://plot.ly/python/sending-data-to-charts/

4. Interactivity: Plot.ly enables end users to modify and filter data views. see modified sample code to use plotly.offline for privacy. see privacy-slider.py example

5. Local data display:  Use plotly offline from command line to enable html to be displayed inside of a website page.
plot.ly runs a webserver locally when plot() is used. iplot is for notebooks such as jupyter. 


<h4>Todo: </h4>
Investigate integration with existing PyQT5 desktop app/pywebview


<h4> Links to additional resources: </h4>
<ul>
<li> https://plot.ly/pandas/time-series/                                                                                      
<li> https://plot.ly/python/candlestick-charts/                                                                               
<li> https://towardsdatascience.com/python-for-finance-dash-by-plotly-ccf84045b8be
<li> https://plot.ly/python/user-guide/   
<li>  https://plot.ly/python/offline/#plotly-offline-from-command-line
</ul>
