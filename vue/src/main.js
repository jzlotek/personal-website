import Vue from 'vue'
import App from './App'
import router from './router'
import NavBar from './components/NavBar.vue'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    NavBar
  },
  render: h => h(App)
})
