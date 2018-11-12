import Vue from 'vue'
import App from './App'
import router from './router'
import NavBar from './components/NavBar'
import { Particle } from './components/particle.js'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    NavBar,
    Particle
  },
  render: h => h(App)
})
