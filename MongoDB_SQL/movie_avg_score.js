
db.ratings.aggregate([
    {
        $group: {
            _id: "$movieId",
            value: {
                $avg: "$rating"
            }
        }
    },
    {
        $sort: {
            _id:  - 1
        }
    },
    {
        $out: "movies_socre"
    }
]) 