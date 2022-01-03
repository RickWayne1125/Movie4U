#### 各标签热门电影推荐

数据预处理：MongoDB_SQL中

movie_avg_score.js 负责计算各电影平均评分，生成**movies_socre**集合

| 字段名 | 解释         | 类型         |
| ------ | ------------ | ------------ |
| _id    | 电影id       | INT32/Double |
| value  | 电影平均评分 | Double       |

pop_movies_on_tag.js 负责统计与标签相关度>`0.9` ，且满足评分>`4.0`的电影id数组，生成**tagId-movieIdArray**集合

| 字段名       | 解释                 | 类型         |
| ------------ | -------------------- | ------------ |
| _id          | 标签id               | INT32/Double |
| movieIdArray | 满足条件的电影id集合 | Double 数组  |

样例：

{_id:19 movieIdArray:[110,260,293,1196,1198,1218,2571,4993,5782,5952,58559,79132]}

标签：动作片

电影：

Braveheart (1995)

Star Wars: Episode IV - A New Hope (1977)

Léon: The Professional (a.k.a. The Professional) (Léon) (1994)

----

一页展示8个热门电影，每个tag取两个，由于tagId-movieIdArray内tag对应movieId集合是不等长的，
- 多于两个者，只取两个
- 一个者，直接取
- 无对应者，跳过
总计取8个movieId

tag取法：暂定静态，从1取到1126【总tag数1128，后两似乎没热片？】
init_pop_movies 返回无重复的电影id集合
样例：
迭代结束的随机数：871
8部热门影片id：{26150, 905, 2731, 3089, 26578, 916, 213, 3415}

----

推荐通过累计用户选择，跟数据库similarity库比较?
