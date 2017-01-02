
# coding: utf-8

# In[2]:

from highcharts import Highchart
import numpy as np
import functools


# In[4]:

def make_chart_daily_pnl(stats):
    chart = Highchart()
    options = {
        'chart': {
            'zoomType': 'x'
        },
        'title': {
            'text': 'Daily Profit and Loss'
            },
        'xAxis': {
            'type': 'datetime'
        },
        'yAxis': {
            'title': {
                'text': 'Daily P/L'
            }
        },
        'legend': {
            'enabled': False
        }
    }
    chart.set_dict_options(options)
    timestamps = stats.index.astype(np.int64) // 1000000
    plot_data = np.dstack((timestamps, stats["day_pnl"].values))[0].tolist()
    chart.add_data_set(plot_data, 'line', 'PnL')
    return chart

def make_chart_daily_exposure(stats):
    chart = Highchart()
    options = {
        'chart': {
            'zoomType': 'x'
        },
        'title': {
            'text': 'End of day exposure'
            },
        'xAxis': {
            'type': 'datetime'
        },
        'yAxis': {
            'title': {
                'text': 'Exposure'
            }
        },
        'legend': {
            'enabled': False
        }
    }
    chart.set_dict_options(options)
    timestamps = stats.index.astype(np.int64) // 1000000
    plot_data = np.dstack((timestamps, stats["day_end_exposure"].values))[0].tolist()
    chart.add_data_set(plot_data, 'area', 'Exposure')
    return chart

def make_chart_daily_max_long_short(stats):
    chart = Highchart()
    options = {
        'chart': {
            'zoomType': 'x'
        },
        'title': {
            'text': 'Max Long/Short intra day'
            },
        'xAxis': {
            'type': 'datetime'
        },
        'yAxis': {
            'title': {
                'text': '$'
            }
        },
        'legend': {
            'enabled': False
        }
    }
    chart.set_dict_options(options)
    timestamps = stats.index.astype(np.int64) // 1000000
    long_data = np.dstack((timestamps, stats["max_long"].values))[0].tolist()
    chart.add_data_set(long_data, 'column', 'Max Long')
    short_data = np.dstack((timestamps, -stats["max_short"].values))[0].tolist()
    chart.add_data_set(short_data, 'column', 'Max Short')
    return chart

def get_position_value(product_map, account, pid):
    p = account.get_position(pid["exchange"], pid["orderbook_id"])
    if p.asset_value > 0:
        return {'name': str(product_map[pid["orderbook_id"]]), 'value': p.asset_value * p.price_factor}
    else:
        return {'name': "("+str(product_map[pid["orderbook_id"]])+")", 'value': -p.asset_value * p.price_factor}
        
def make_chart_asset_allocation(product_map, account):
    allocations = list(map(functools.partial(get_position_value, product_map, account), account.get_ids()))
    capital = account.get_stats().tail(1)['day_end_capital'][0]
    allocations.append({'name': 'Cash', 'value': capital})
    total_allocations = sum(map(lambda x: x['value'], allocations))
    allocations_percent = list(map(lambda x: {'name': x['name'], 'y': x['value'] / total_allocations * 100}, allocations))

    chart = Highchart()
    options = {
        'chart': {
            'zoomType': 'x'
        },
        'title': {
            'text': 'Asset allocation'
            },
        'xAxis': {
            'type': 'datetime'
        },
        'yAxis': {
            'title': {
                'text': 'Daily P/L'
            }
        },
        'legend': {
            'enabled': False
        }
    }
    chart.set_dict_options(options)
    chart.add_data_set(allocations_percent, 'pie', 'Asset allocation')
    return chart

def make_chart_max_drawdown(stats):
    chart = Highchart()
    options = {
        'chart': {
            'zoomType': 'x'
        },
        'title': {
            'text': 'Max Drawdown'
            },
        'xAxis': {
            'type': 'datetime'
        },
        'yAxis': {
            'title': {
                'text': 'Daily P/L'
            }
        },
        'legend': {
            'enabled': False
        }
    }
    chart.set_dict_options(options)
    timestamps = stats.index.astype(np.int64) // 1000000
    plot_data = np.dstack((timestamps, stats["max_drawdown"].values))[0].tolist()
    chart.add_data_set(plot_data, 'column', 'Max Drawdown')
    return chart

def make_chart_realized_pnl(stats):
    chart = Highchart()
    options = {
        'chart': {
            'zoomType': 'x'
        },
        'title': {
            'text': 'Realized Cumulative Profit and Loss'
            },
        'xAxis': {
            'type': 'datetime'
        },
        'yAxis': {
            'title': {
                'text': 'Realized P/L'
            }
        },
        'legend': {
            'enabled': False
        }
    }
    chart.set_dict_options(options)
    timestamps = stats.index.astype(np.int64) // 1000000
    plot_data = np.dstack((timestamps, stats["realized_pnl"].values))[0].tolist()
    chart.add_data_set(plot_data, 'line', 'PnL')
    return chart


# In[ ]:



