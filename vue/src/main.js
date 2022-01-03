import Vue from 'vue'
import App from './App.vue'
import elementUI from '../node_modules/element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import router from './router'
import store from './store'
import axios from './axios';

Vue.prototype.$axios=axios

Vue.use(elementUI)
Vue.config.productionTip = false
Vue.config.silent = true
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')



