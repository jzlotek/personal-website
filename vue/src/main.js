import Vue from 'vue'
import App from './App'
import router from './router'
import NavBar from './components/NavBar'
import Particles from './components/Particles'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    NavBar,
    Particles
  },
  render: h => h(App)
})
