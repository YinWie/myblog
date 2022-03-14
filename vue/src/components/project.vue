<template>
  <div class="">
    <div class="pc hidden-md-and-down">
      <a :href='link' class="im">
        <img :src="imgSrc" width="100%" height="100%" alt=""/>
      </a>
      <a :href='link' class="introduce">
        <h2>{{ names }}</h2>

        <p>{{ datas }}</p>
      </a>

    </div>
    <div class="phone hidden-lg-and-up">
      <a class="im" :href='link'>
        <img :src="imgSrc" width="100%" height="100%" alt=""/>
      </a>
      <a :href='link' class="introduce-phone">
        <h3>{{ names }}</h3>

        <p>{{ datas }}</p>

      </a>

    </div>
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css';

export default {
  name: "project",
  props: ['names', 'imgSrc', "datas", 'link'],
}
</script>

<style scoped>
p {

  word-wrap: break-word;


}


a {
  color: #1D1D1F;
  text-decoration: none;
}

.pc {
  height: 250px;
  width: 700px;
  margin-top: 20px;
  margin-right: 20px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.phone {
  height: 150px;
  width: 360px;
  margin-top: 20px;
  margin-right: 20px;
  display: flex;
  flex-direction: row;
  justify-content: center;


}

.im {
  width: 30%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

}

.introduce {
  width: 70%;
  display: flex;
  align-items: center;
  flex-direction: column;
  word-wrap: break-word;
  padding: 20px;
  padding-top: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}

.introduce-phone {
  width: 70%;
  display: flex;
  align-items: center;
  flex-direction: column;
  word-wrap: break-word;
  padding: 5px;
  padding-top: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
}
</style>