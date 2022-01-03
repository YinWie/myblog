<template>
  <div class="boxs">
    <hd :imgSrc="imgSrc"></hd>

    <div id="bodys">
      <div>
        <project v-for="data in nm " :key="data" :names=data.name :imgSrc=data.img :datas=data.datas :link=data.link></project>
      </div>
      <lb class="hidden-md-and-down" :texts="texts"></lb>
    </div>
  </div>

</template>

<script>

import lb from "@/components/Lsidebar"
import hd from "@/components/hd"
import project from "@/components/project";
import 'element-ui/lib/theme-chalk/display.css';
import axios from "axios";
export default {
  name: "archives",

  components: {
    lb, hd, project
  },
  data() {
    return {
      texts:[],
      nm:[],
      imgSrc:''
    }
  },
  methods: {
    getMessage() {
      const path = '/archives/project_data';
      axios.get(path)
          .then((res) => {
            this.nm = res.data[0];
            this.texts = res.data[1];
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
#bodys {
  display: flex;
  flex-direction: row;
  justify-content: center;

}

</style>
