var url = "https://185.196.220.38";
var app = new Vue({
  el: "#checkList",
  data: {
    check_movies: [
      // 用于布局测试
      { id: 1, name: "M1", tag: "T1" },
      { id: 2, name: "M2", tag: "T2" },
      { id: 3, name: "M3", tag: "T3" },
      { id: 4, name: "M4", tag: "T4" },
      { id: 5, name: "M5", tag: "T5" },
      { id: 6, name: "M6", tag: "T6" },
      { id: 7, name: "M7", tag: "T7" },
      { id: 8, name: "M8", tag: "T8" },
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
