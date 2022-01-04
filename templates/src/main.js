var url = "http://127.0.0.1:5000";
var app = new Vue({
  el: "#app",
  data: {
    check_movies: [
      // 用于布局测试
      {
        id: 1,
        name: "M1",
        tag: "T1"
      },
      {
        id: 2,
        name: "M2",
        tag: "T2"
      },
      {
        id: 3,
        name: "M3",
        tag: "T3"
      },
      {
        id: 4,
        name: "M4",
        tag: "T4"
      },
      {
        id: 5,
        name: "M5",
        tag: "T5"
      },
      {
        id: 6,
        name: "M6",
        tag: "T6"
      },
      {
        id: 7,
        name: "M7",
        tag: "T7"
      },
      {
        id: 8,
        name: "M8",
        tag: "T8"
      },
    ],
    pre_movies: [],
    button: [false, false, false, false, false, false, false, false],
  },
  methods: {
    refreshMovies() {
      axios
        .get(url + "/init")
        .then((response) => (this.check_movies = response.data))
        .catch(function (error) {
          // 请求失败处理
          console.log(error);
        });
      this.button = [false, false, false, false, false, false, false, false];
    },
    addPreMovie(index) {
      var id = this.check_movies[index].id;
      var name = this.check_movies[index].name;
      for (var i in this.pre_movies) {
        if (this.pre_movies[i].id == id) {
          alert("已经添加过该电影了");
          return;
        }
      }
      this.pre_movies.push({
        id: id,
        name: name
      });
      this.button[index] = true;
      console.log(JSON.stringify(this.pre_movies));
    },
    removePreMovie(index) {
      var id = this.pre_movies[index].id;
      for (var i in this.pre_movies) {
        if (this.pre_movies[i].id == id) {
          this.pre_movies.splice(i, 1);
          break;
        }
      }
      for (var j in this.check_movies) {
        if (this.check_movies[j].id == id) {
          this.button[j] = false;
        }
      }
    },
    removeAll() {
      this.button = [false, false, false, false, false, false, false, false];
      this.pre_movies = [];
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