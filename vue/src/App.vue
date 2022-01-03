<template>
  <div class="bk">
    <div id="app">
      <Nav :links="links"></Nav>
      <router-view/>
      <foot></foot>
    </div>
  </div>
</template>

<script>
import Nav from './components/Nav'
import foot from './components/foot'
import axios from "axios";
export default {
  name: 'app',
  components: {
    Nav, foot
  },
  data() {
    return {
      links: [],
    }
  },
  methods: {
    getMessage() {
      const path = '/home/nav_links';
      axios.get(path)
          .then((res) => {
            this.links = res.data;
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

<style lang="stylus">
html:root {
  background: url("../public/static/bg.webp");
  background-repeat: no-repeat;
  background-attachment: fixed;
}

#app

  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50

p{
  color: #707579;
}

</style>
