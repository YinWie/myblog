import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import archives from '../views/archives.vue'
import finds from '../views/finds.vue'
import labo from '../views/labo.vue'
import tools from '../views/tools.vue'


Vue.use(VueRouter)

const routes = [
      {
        path: '/',
        redirect: '/home',
        name: '首页',
        component: Home
    },
      {
        path: '/home',
        name: '首页',
        component: Home
    },
    {
        path: '/archives',
        name: '档案馆',
        component: archives
    }, {
        path: '/finds',
        name: '友链',
        component: finds
    }, {
        path: '/labo',
        name: '实验室',
        component: labo
    }, {
        path: '/tools',
        name: '工具箱',
        component: tools
    }

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
