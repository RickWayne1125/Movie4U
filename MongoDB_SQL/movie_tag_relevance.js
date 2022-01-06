// 筛选相关度>0.9的电影集合，以tagId分组
db.getCollection("genome-scores").aggregate([
    {
        $match: {
            relevance:{$gt: 0.9}
        }
    },
    {
        $group: {
            _id: "$movieId",
            tagArray: {
                $push:"$movieId"
            }
        }
    },
    {
        $sort: {
            _id: 1
        }
    },
    {
        $out: "movies_tag"
    }
]) 