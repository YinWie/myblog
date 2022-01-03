<template>
  <div class="hh">
     <img :src='imgSrc' width="100%" height="100%" alt="" />
  </div>
</template>

<script>


export default {
  name: "head",

  props:['imgSrc'],
   data() {
    return {
       // imgSrc:"./static/1.jpg",
    }
  }
}
</script>

<style scoped>
.hh {
  height:560px;
}
</style>