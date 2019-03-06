Vue.component('card-blog',{
    props: ['blog'],
    template:`
    <div class="card my-3">
      <img :src="blog.image" class="card-img-top img-fluid" alt="..." />
      <div class="card-body" :class="{test: blog.col}" v-on:click.self="changeBGColor(blog)">
        <h5 class="card-title">
          {{ blog.title }}
          <span class="badge badge-success ml-5">Likes: {{blog.likes}}</span>
        </h5>
        <p class="card-text">
          {{blog.content}}<br />
          <small class="text-muted">Create By: {{blog.createBy}}</small>
          <small class="text-muted ml-5">Create Date: {{blog.createDate}}</small>
        </p>
        <!--<button class="btn btn-primary">Go to my page</button>-->
        <button class="btn btn-success" v-on:click="blog.likes += 1">I like this!</button>
        <button class="btn btn-info" @click="showComment(blog)">{{blog.caser ? "Hide Comments":"Show comments"}}</button>
        <input type="text" class="form-control" placeholder="Add comment" style="padding-top:10px" id="add">
        <button id="basic-addon1" v-on:click="addComment(blog)">Search</button>
        <div class="card mt-2 text-dark" v-for="(comment, index) in blog.comments" :key="index" v-show="blog.caser">
        <div class="card-body">
        </div>
          <div class="card-body">
          <h6 class="card-title">Comment {{index +1 }}</h6>
            <h6 class="card-title">Comment {{index +1 }}</h6>
            <p class="card-text">
              {{comment.text}}<br />
              <small class="text-muted">Create By: {{comment.createBy}}</small>
              <small class="text-muted ml-5">Create Date: {{blog.createDate}}</small>
            </p>
          </div>
        </div>
      </div>
    </div>`,
  methods: {
    changeBGColor(blog) {
      blog.col = !blog.col;
    },
    showComment(bl) {
      bl.caser = !bl.caser
    },
    search: function () {
      var text = document.querySelector("#search").value
      if (text == "") {
        for (var index = 0; index < this.blogs.length; index++) {
          this.blogs[index].showing = true
        }
      } else {
        for (var index = 0; index < this.blogs.length; index++) {
          if (this.blogs[index].title.toUpperCase().indexOf(text.toUpperCase()) > -1) {
            this.blogs[index].showing = true
          } else {
            this.blogs[index].showing = false
          }
        }
      }
    },
    addComment(blog){
        var text = document.querySelector("#add").value
        blog.comments.push(text)
    }
  },
  computed: {
    countLike: function () {
      var like = 0;
      for (var index = 0; index < this.blogs.length; index++) {
        like += this.blogs[index].likes
      }
      return like;
    },
  },
  watch: {
    blogs: function (oldValue, newValue) {
      if (oldValue.length > this.maxPost) {
        this.tooManyPost = true
      } else {
        this.tooManyPost = false
      }
    }

  },

})