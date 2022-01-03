<template>
  <div class="page">
    <hello></hello><!--背景-->
    <my></my>
  </div>
</template>

<script>
import hello from '../components/hello';
import my from "@/components/my";

export default {
  name: 'Home',
  components: {
    hello,my
  },
  data() {
    return {}
  },
}
</script>
<style>

</style>
