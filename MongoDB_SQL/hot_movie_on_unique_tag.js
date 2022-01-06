// 生成热门电影，关联多个表组合信息
db.getCollection("tagId-movieIdArray").aggregate([
    {
        $unwind: "$movieIdArray"
    },
    {
        $group: {
            _id: "$movieIdArray",
            movie_tags: {
                $push: "$_id"
            },
            
        }
    },
    {
        $lookup: {
            from: "movies",
            localField: "_id",
            foreignField: "movieId",
            as: "movieInfo"
        }
    },
    {
        $project: {
            tag_id: {
									$first:"$movie_tags"
            },
            title: "$movieInfo.title",
						url:"$movieInfo.url"
        }
    },
		{$unwind:"$title"},
		{$unwind:"$url"},
    {
        $lookup: {
            from: "genome-tags",
            localField: "tag_id",
            foreignField: "tagId",
            as: "tagInfo"
        }
    },
    {
        $project: {
            title: "$title",
            tag_id: "$tag_id",
            tag_name: "$tagInfo.tag",
						url:"$url"
        }
    },
		{$unwind:"$tag_name"},
    {
        $sort: {
            _id: 1
        }
    },
		{$out:"hot_movie_on_single_tag"}
])