#!/usr/local/bin python3


def calculate(stock_list):
    profit = 0
    for i, c in enumerate(stock_list):
        sale_list = stock_list[i:]
        for v in sale_list:
            profit = int(v) - int(c) if int(v) - int(c) > profit else profit

    return profit


if __name__ == '__main__':

    list_str = raw_input("Insera a lista no formato '1,20,3,14...': ")
    stk_list = list_str.split(',')
    print(calculate(stk_list))
