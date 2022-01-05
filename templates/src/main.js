var backend = "http://127.0.0.1:5000";
var test_url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F246907e641edd915ba79bc54abaa84b9b116013b2063c-eutAok_fw658&refer=http%3A%2F%2Fhbimg.b0.upaiyun.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1643866502&t=0387f1b089f1231eda907d0ee13ad212";
var app = new Vue({
  el: "#app",
  data: {
    check_movies: [
      // 用于布局测试
      {
        id: 1,
        name: "M1",
        tag: "T1",
        url: test_url,
      },
      {
        id: 2,
        name: "M2",
        tag: "T2",
        url: test_url,
      },
      {
        id: 3,
        name: "M3",
        tag: "T3",
        url: test_url,

      },
      {
        id: 4,
        name: "M4",
        tag: "T4",
        url: test_url,
      },
      {
        id: 5,
        name: "M5",
        tag: "T5",
        url: test_url,
      },
      {
        id: 6,
        name: "M6",
        tag: "T6",
        url: test_url,
      },
      {
        id: 7,
        name: "M7",
        tag: "T7",
        url: test_url,
      },
      {
        id: 8,
        name: "M8",
        tag: "T8",
        url: test_url,
      },
    ],
    pre_movies: [],
    rec_movies: [],
    button: [false, false, false, false, false, false, false, false],
    loading: true,
    start_rec: false,
  },
  methods: {
    refreshMovies() {
      axios
        .get(backend + "/init")
        .then((response) => {
          this.check_movies = response.data;
          this.button = [false, false, false, false, false, false, false, false];
        })
        .catch(function (error) {
          // 请求失败处理
          console.log(error);
        });
    },
    addPreMovie(index) {
      var id = this.check_movies[index].id;
      var name = this.check_movies[index].name;
      var url = this.check_movies[index].url;
      var tag = this.check_movies[index].tag;
      for (var i in this.pre_movies) {
        if (this.pre_movies[i].id == id) {
          alert("已经添加过该电影了");
          return;
        }
      }
      this.pre_movies.push({
        id: id,
        name: name,
        url: url,
        tag: tag,
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
      console.log(this.rec_movies.length);
    },
    getRecommend() {
      this.start_rec = true;
      this.loading = true;
      console.log(this.start_rec);
      console.log(this.loading);
      axios
        .post(backend + "/recommend")
        .then((response) => {
          this.rec_movies = response.data;
          this.loading = false;
        })
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