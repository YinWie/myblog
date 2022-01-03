import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        //相当于自定义组件中的data
    },
    getters: {
        //相当于自定义组件中的computed
    },
    mutations: {
        //相当于自定义组件中的methods，只能做同步的操作
        //对state中的数据进行修改
    },
    actions: {
        //异步操作，例如ajax请求
        //使用commit 触发 mutations
    }
})
