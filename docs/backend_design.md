#### 数据库信息预处理

见MongoDB_SQL

movie_score_avg.js 

计算各电影平均评分

| 字段名 | 解释         | 类型   |
| ------ | ------------ | ------ |
| _id    | 电影id       | INT32  |
| value  | 电影平均评分 | Double |

tag_hot_movie_array.js  

对已处理相关度>0.9的电影，筛选均分>4.0者



| 字段名       | 解释                 | 类型        |
| ------------ | -------------------- | ----------- |
| _id          | 标签id               | INT32       |
| movieIdArray | 满足条件的电影id集合 | Double 数组 |

movie_tag_relevance.js  

负责筛选相关度>0.9的电影集合，以tagId分组



| 字段名   | 解释                 | 类型        |
| -------- | -------------------- | ----------- |
| _id      | 标签id               | INT32       |
| tagArray | 满足条件的电影id集合 | Double 数组 |

hot_movie_on_unique_tag

生成热门电影，关联多个表组合信息
| 字段名   | 解释     | 类型        |
| -------- | -------- | ----------- |
| _id      | 电影id   | INT32       |
| title    | 电影标题 | Double 数组 |
| tag_id   | 标签id   | INT32       |
| tag_name | 标签名   | string      |
| url      | 图片链接 | string      |

