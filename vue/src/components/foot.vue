<template>
  <div class="foots">
    <div class="pc">
      <!--     注释是未完善功能的接口 -->
      <p>感谢您的访问</p>
      <!--          <div class=""><p>开放api</p></div>-->
      <span id="site_runtime">{{ dateFormat(newDate) }}</span>
      <!--          <div class="index">-->
      <!--            <p>访问人数</p>-->
      <!--            <p>浏览总量</p>-->
      <!--          </div>-->
      <div class="">
        <a href="https://beian.miit.gov.cn/" target="_blank">{{ record }}</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "foot",
  data() {
    return {
      record: "冀ICP备2021025902号",
      newDate: new Date()
    }
  },
  mounted() {
    let that = this
    this.timer = setInterval(function () {
      that.newDate = new Date().toLocaleString()
    })
  }, beforeDestroy: function () {
    if (this.timer) {
      clearInterval(this.timer)
    }
  }
  , methods: {
    dateFormat() {
      // window.setTimeout("show_site_runtime()", 1000);
      let X = new Date("12/31/2021 00:00:00");
      let Y = new Date();
      let T = (Y.getTime() - X.getTime());
      let i = 24 * 60 * 60 * 1000;
      let d = T / i;
      let D = Math.floor(d);
      let h = (d - D) * 24;
      let H = Math.floor(h);
      let m = (h - H) * 60;
      let M = Math.floor(m);
      let s = (m - M) * 60
      let S = Math.floor(s);
      return  D + "天 " + H + " 小时 " + M + " 分 " + S + " 秒 "
    }
  }
}
</script>

<style scoped>
.foots {
  margin-top: 30px;
  flex: 0 0 auto;
  bottom: 0px;
  height: 120px;

}

.pc {
  background-color: #c8a8b7;
  width: 100%;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

}

a {
  color: #F5F5F7;
  text-decoration: none;
}

p {
  font-size: 20px;

}

.pc .index {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.pc .index p {
  padding: 5px;
}
</style>
