# pyecharts_worldmap

country_cn.txt和country_eng是世界地图中国家的中文和英文，因为pyecharts中需要使用国家英文来构造地图数据，可以根据情况自行修改。

geo-example.txt中是地理位置信息的示例，每行显示一条位置信息。

    bash world-geo.sh geo-example.txt > example.txt
  
使用shell脚本统计国家位置数据并保存到文件，python脚本读取该文件绘制世界地图。
