from pyecharts import options as opts
from pyecharts.charts import Map

cn_to_eng = {}
data = []

with open('data/worldmap/country-cn.txt', 'r', encoding='utf-8') as cn:
    with open('data/worldmap/country-eng.txt', 'r', encoding='utf-8') as eng:
        while True:
            line_cn = cn.readline()
            line_eng = eng.readline()
            if not line_cn or not line_eng:
                break
            country_cn = line_cn[:-1]
            country_eng = line_eng[:-1]
            if country_cn not in cn_to_eng:
                cn_to_eng[country_cn] = country_eng


#for key, value in cn_to_eng.items():
#    print("\'{}\' ".format(key), end='')


with open('data/worldmap/fdns-global-geo-stat.txt', 'r', encoding='utf-8') as f:
    max_cnt = 0
    while True:
        line = f.readline()
        if not line:
            break
        country = line.split(' ')[0]
        cnt = int(line.split(' ')[1][:-1])
        if country == "中国":
            cnt = 0
        if cnt > max_cnt:
            max_cnt = cnt
        data.append([cn_to_eng[country], cnt])


#print(data)

worldMap = Map()
worldMap.add("转发DNS分布", data, "world", is_map_symbol_show=False)
worldMap.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
worldMap.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=max_cnt))
worldMap.render(path="data/output/转发DNS分布-全球.html")
