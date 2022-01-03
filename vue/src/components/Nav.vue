<template>
  <div>
    <!--适配电脑-->
    <div class=" hidden-md-and-down pc">
      <div class=" pc-box" v-for="data in links " :key="data">
        <router-link tag='div' class='link' :to="{ path: data.link }">{{ data.name }}</router-link>
      </div>
    </div>
    <!--适配手机-->
    <div class="pone hidden-lg-and-up  ">
      <el-menu :default-active="activeIndex"
               class="el-menu-demo"
               mode="horizontal"
               @select="handleSelect"
               background-color='rgba(0,0,0,0.3)'
               text-color='#F5F5F7'>
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-s-operation "></i></template>
          <el-menu-item v-for="data in links " :key="data.link">
            <router-link tag='div' class='link'  :to="{ path: data.link }">{{ data.name }}</router-link>
          </el-menu-item>
        </el-submenu>
      </el-menu>
    </div>
  </div>
</template>
<script>
import 'element-ui/lib/theme-chalk/display.css';
import 'element-ui/lib/theme-chalk/base.css';
export default {
  name: "Nav",
  props:['links'],

}
</script>

<style scoped>
.link.router-link-active,.articles.router-link-active {
  color:#B4BBDA;
  text-decoration:underline;

}
.link{
  color:white;
  -webkit-user-select:none;
  -moz-user-select:none;
  -ms-user-select:none;
  user-select:none;
  cursor:pointer;
}
.pc {
  width: 100%;
  position: absolute;
  min-height: 26px;
  align-items: center;
  background: rgba(0, 0, 0, 0.2);
  display: flex;
  justify-content: center;
  z-index: 100;

}

.pc-box {
  width: 10%;
  align-items: center;
}

a {
  text-decoration: none;
  color: #F5F5F7;
  font-size: 20px;
}

div {
  display: block;
}


</style>
