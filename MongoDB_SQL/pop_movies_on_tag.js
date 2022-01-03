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