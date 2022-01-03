<template>
  <div class="pc">
    <div class="word">
      <h2>这是什么？？</h2>
      <p v-for="data in texts" :key="data">{{ data.word }}</p>
    </div>
  </div>

</template>

<script>
export default {
  name: "Lsidebar",
  props: ["texts"],
}
</script>

<style scoped>


.pc {
  margin-top: 20px;

  width: 260px;


}
p{
  color: #707579;
}
.word {
  display: flex;
  flex-direction: column;
  word-wrap: break-word;
  padding: 15px;

  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}
</style>