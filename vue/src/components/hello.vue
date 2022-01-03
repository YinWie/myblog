<template>
  <div class="wb">
    <div class="vd">
      <div class="hidden-md-and-down mb1">
        <video loop muted autoplay class="video1 hidden-md-and-down ">
          <source src="../../public/static/index.mp4" type="video/mp4">
        </video>
      </div>
      <div class="hidden-lg-and-up mb2">
        <video loop muted autoplay class="video2 hidden-lg-and-up ">
          <source src="../../public/static/index.mp4" type="video/mp4">
        </video>
      </div>
    </div>
    <div class="hellos">
      <div class="hlpc hidden-md-and-down">
        <p>音尾の小窝</p>
        <p>Hello</p>
        <div class="link">
          <div>
            <a href="https://space.bilibili.com/36134023" target="_blank">前往哔哩哔哩</a>
          </div>
          <div>
            <a href="https://github.com/jc1327540662" target="_blank">前往GitHub</a>
          </div>
        </div>
      </div>
      <div class="hlpo hidden-lg-and-up">
        <p>音尾の小窝</p>
        <p>Hello</p>
        <div class="link">
          <div>
            <a href="https://space.bilibili.com/36134023" target="_blank">前往哔哩哔哩</a>
          </div>
          <div>
            <a href="https://github.com/jc1327540662" target="_blank">前往GitHub</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import 'element-ui/lib/theme-chalk/display.css';

export default {
  name: "hello"
}
</script>

<style scoped>

.vd {
  width: 100%;
  z-index: -11;

}

.mb1:before {
  content: "";
  background: rgba(7, 10, 12, 0.3);
  position: absolute;
  min-height: 560px;
  left: 0;
  right: 0;
  z-index: 1;
}

.mb2:before {
  content: "";
  background: rgba(7, 10, 12, 0.3);
  position: absolute;
  min-height: 340px;
  left: 0;
  right: 0;
  z-index: 1;
}

.video1 {
  width: 100%;
  height: 560px;
  object-fit: cover;
  z-index: -11;
}

.video2 {
  width: 100%;
  height: 340px;
  object-fit: cover;
}

source {
  width: auto;
  height: auto;
  min-height: 100%;
  min-width: 100%;
}

.hlpo {
  position: absolute;
  top: 120px;
  left: 10%;
  right: 10%;
  width: 80%;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  z-index: 10;
}

.hlpo p {
  font-size: 64px;
  color: #F5F5F7;
  height: auto;
  display: block
}

.hlpo a {
  color: #F5F5F7;
  font-size: 15px;
  white-space: nowrap;

}

.hlpc {
  position: absolute;
  top: 180px;
  left: 35%;
  right: 35%;
  width: 30%;
  height: 200px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  z-index: 10;
}

.hlpc p {
  font-size: 64px;
  color: #F5F5F7;
  height: auto;
  display: block
}

.link {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.link div {
  width: auto;
  padding: 5px;
}

.hlpc a {
  color: #F5F5F7;
  font-size: 15px;
  white-space: nowrap;
}

a:hover {
  color: #b5bad9;
  text-decoration: none;
}

a:active {
  color: #c8a8b7;
}

a:link {
  color: #F5F5F7;
}
</style>
