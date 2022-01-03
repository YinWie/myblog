<template>
  <div>
    <hd :imgSrc="imgSrc"></hd>
    <div class="home hidden-md-and-down" v-for="data in pc " :key="data">
      <div class="fid">
        <find v-for="dt in data " :key="dt" :imgSrc=dt.imgSrc :name=dt.name :lk=dt.lk></find>
      </div>
    </div>
    <div class="home hidden-lg-and-up">
      <div class="phone">
        <find v-for="data in datas " :key="data" :imgSrc=data.imgSrc :name=data.name :lk=data.lk></find>

      </div>
    </div>

  </div>
</template>

<script>
import hd from "@/components/hd";
import find from "@/components/find";
import 'element-ui/lib/theme-chalk/display.css';
import axios from "axios";

export default {
  name: "project",
  components: {
    hd, find
  },
  data() {
    return {
      datas: [],
      pc: []
    }
  },
  methods: {
    getMessage() {
      const path = '/links/finds_links/data';
      axios.get(path)
          .then((res) => {
            this.datas = res.data[0];
            this.pc = res.data[1];
            this.imgSrc = res.data[2];
          })
          .catch((error) => {
            console.error(error);
          });
    },
  },
  created() {
    this.getMessage();
  },

}
</script>

<style scoped>
.phone {
  width: 300px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.home {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-top: 20px;
}

.fid {
  height: 100px;
  width: 600px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 20px;

}


</style>
