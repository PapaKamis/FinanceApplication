from django.shortcuts import render
from .models import Historical_data, Company
from django.contrib.auth.models import User
import pandas as pd
import plotly.graph_objects as go
import plotly.offline
import plotly.express as px
import yfinance as yf

def hist_data(company, period):
    get_data = yf.Ticker(company)
    return get_data.history(period=period)

# data = pd.DataFrame(hist_data('^GSPC', '3mo'))
# data.drop(columns=['Dividends', 'Stock Splits'], inplace=True)
# data.index.name = 'Date'
# data.reset_index(inplace=True)
#
# comp = Company(Name='^GSPC')
# comp.save()

# comp = Company.objects.filter(Name='^GSPC').first()
#
# for row in range(data['Date'].count()):
#     hdata = Historical_data(
#       Company = comp,
#     Date = data.iloc[row][0],
#     Open = data.iloc[row][1],
#     High = data.iloc[row][2],
#     Low = data.iloc[row][3],
#     Close = data.iloc[row][4],
#     Volume = data.iloc[row][5]
#     )
#     hdata.save()



#
h_orm = Historical_data.objects.values()
data = pd.DataFrame(h_orm)


print('------------')
print(data)
print('-------------')
print(h_orm)


def home(request):
    fig = px.line(data, x=data['Date'], y=data.drop(columns=['Volume', 'Company_id']).columns,
                  hover_data={"Date": "|%B %d, %Y"},
                  title='^GSPC')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%d\n%b\n%Y")
    graph_div = plotly.offline.plot(fig, auto_open=False, output_type="div")

    context = {
        # 'posts': Post.objects.all(),
        'title': 'Home',
        'graph_div': graph_div
    }
    return render(request, 'finance/home.html', context)

def about(request):
    context = {
        'script': 'k',
    }
    return render(request, 'finance/about.html', context)


# Twforsure1