<template>
  <!--  <div class="">-->
  <div class="pc">
    <div class="im">
      <a :href="lk" target="_blank">
        <img :src="imgSrc" width="100%" height="100%" alt="" class="im"/>
      </a>

    </div>

    <div class="name">
      <a :href="lk" target="_blank">
        <h2>{{ name }}</h2>
      </a>
    </div>
  </div>

  <!--  </div>-->
</template>

<script>
export default {
  name: "find",
  props: ['imgSrc', 'name', 'lk'],

}
</script>

<style scoped>

.pc {
  height: 100%;
  width: 100%;
  margin: 10px;
  padding: 10px;
  display: flex;
  flex-direction: row;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}

h2 {
  color: #1D1D1F;
}

a:hover {
  text-decoration: none;
}

.im {
  width: 100px;
  height: 100px;
  border-radius: 100px;
  transition: all 1s;
}

img:hover {
  transform: rotate(360deg);
}

.name {
  width: 60%;
  display: flex;
  justify-content: center;
  align-items: center;
  word-wrap: break-word;

}

</style>