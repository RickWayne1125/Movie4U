// 对已处理相关度>0.9的电影，筛选均分>4.0者
db.getCollection("genome-scores").aggregate([
    {
        $match: {
            "relevance": {
                $gt: 0.9
            },
            
        }
    },
    {
        $lookup: {
            from: "movies_socre",
            localField: "movieId",
            foreignField: "_id",
            as: "movieInfo",
            
        }
    },
    {
        $match: {
            "movieInfo.value": {
                $gt: 4.0
            }
        },
        
    },
    {
        $group: {
            _id: "$tagId",
            movieIdArray: {
                $push: "$movieId"
            },
            
        }
    },
    {
        $sort: {
            _id: 1
        }
    },
    {
        $out: "tagId-movieIdArray"
    }
]) 