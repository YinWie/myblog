<template>
  <div class="mys">
    <div class=" hidden-md-and-down pc">
      <div class="im demo">
        <img :src="imgSrc" width="100%" height="100%" alt="" class="an"/>
      </div>
      <div class="word">
        <h1>简介</h1>
        <p v-for="data in texts" :key="data">{{ data.word }}</p>
      </div>
    </div>
    <div class="hidden-lg-and-up phone">
      <div class="im demo">
        <img :src="imgSrc" width="100%" height="100%" alt="" class="an"/>
      </div>
      <div class="word">
        <h1>简介</h1>
        <p v-for="data in texts" :key="data">{{ data.word }}</p>
      </div>
    </div>


  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css';
import 'element-ui/lib/theme-chalk/base.css';
import axios from 'axios';

export default {
  name: "my",
  data() {
    return {
      imgSrc: require("../../public/static/logo.jpg"),
      texts: []
    }
  },
    methods: {
    getMessage() {
      // /home/introduce
      const path = '/home/introduce/data';
      axios.get(path)
        .then((res) => {
          this.texts = res.data;
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
.mys {
  display: flex;
  justify-content: center;
  align-items: center;


}

.phone {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

p {
  display: block;
  font-size: 25px;
  word-wrap: break-word;
  padding: 5px;
  text-align: left;
  text-indent: 2em;
  color: #707579;

}

.pc {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

}

.word {
  display: flex;
  flex-direction: column;
  width: 600px;
  padding: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}

.phone .word {
  display: flex;
  flex-direction: column;
  width: 300px;
  padding: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);

}

.im {
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  height: 200px;
  width: 600px;
  user-select: none;
}

img {
  height: 200px;
  width: 200px;
  border-radius: 100px;
  user-select: none;

}

.demo {
  text-align: center;
  margin-top: 100px;
  cursor: pointer;
}

@-webkit-keyframes rotation {
  from {
    -webkit-transform: rotate(0deg);
  }
  to {
    -webkit-transform: rotate(360deg);
  }
}

.an {
  -webkit-transform: rotate(360deg);
  animation: rotation 5s linear infinite;
  -moz-animation: rotation 5s linear infinite;
  -webkit-animation: rotation 5s linear infinite;
  -o-animation: rotation 5s linear infinite;

}

.phone .im {
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  height: 200px;
  width: 310px;
}

.pc div {
  padding: 10px;
}

.phone div {
  padding: 10px;

}
</style>
