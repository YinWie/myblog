<template>
  <div class="">
    <hd :imgSrc="imgSrc"></hd>
    <div id="bods">
      <div>
        <project v-for="data in nm " :key="data" :names=data.name :imgSrc=data.img :datas=data.datas :link=data.link></project>
      </div>
      <lb class="hidden-md-and-down" :texts="texts"></lb>
    </div>
  </div>
</template>

<script>
import hd from "@/components/hd";
import lb from "@/components/Lsidebar";
import project from "@/components/project";
import 'element-ui/lib/theme-chalk/display.css';
import axios from "axios";

export default {
  name: "labo",
  components: {
    hd, lb, project

  },
  data() {
    return {
      nm: [],
      texts: []
    }
  },
  methods: {
    getMessage() {
      // /home/introduce
      const path = '/labo/labo_content/data';
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
#bods {
  display: flex;
  flex-direction: row;
  justify-content: center;
  /*align-items: center;*/
}

</style>
