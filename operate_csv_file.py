import csv

# =========================================================================== #
# 读取 csv 数据到 dict 中
with open('temp.csv', 'r', encoding='utf-8') as f_r:
    r_rows = csv.DictReader(f_r)
    for r_row in r_rows:
        dict_tmp = dict(r_row)
        print(dict_tmp)

# 读取 csv 数据到 list 中
with open('temp.csv', 'r', encoding='utf-8') as f_r:
    r_rows = csv.reader(f_r)
    headers = next(r_rows)
    print(headers)
    for r_row in r_rows:
        print(r_row)

# =========================================================================== #
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [
    {'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007','Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
    {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007','Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
    {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007','Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
]
# 将 dict 数据写入到 csv 文件
with open("temp.csv", 'w', encoding='utf-8', newline="") as f_w:
    f_csv = csv.DictWriter(f_w, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

list_temp = [
    ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume'],
    ['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '181800'],
    ['AIG', '71.38', '6/11/2007', '9:36am', '-0.15', '195500'],
    ['AXP', '62.58', '6/11/2007', '9:36am', '-0.46', '935000']
]
# 将 list 数据写入到 csv 文件
with open("temp.csv", 'w', encoding='utf-8', newline="") as f_w:
    f_csv = csv.writer(f_w)
    f_csv.writerows(list_temp)
