var url = "https://185.196.220.38";
var app = new Vue({
  el: "#checkList",
  data: {
    check_movies: [
      {
        id: 1,
        name: "M1",
        tag: "T1",
      },
      {
        id: 2,
        name: "M2",
        tag: "T2",
      },
      {
        id: 3,
        name: "M3",
        tag: "T3",
      },
    ],
    pre_movies: [],
  },
  methods: {
    refreshMovies() {
      axios
        .get(url + "/")
        .then((response) => (this.check_movies = response.data.init_list))
        .catch(function (error) {
          // 请求失败处理
          console.log(error);
        });
    },
    addPreMovie(index) {
      var id = check_movies[index].id;
      this.pre_movies.push({ id: id });
    },
    getRecommend() {
      axios
        .post(url + "/recommend")
        .then((response) => (this.rec_list = response.data.rec_list))
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  mounted() {
    // 获取冷启动电影
    this.refreshMovies();
  },
});
