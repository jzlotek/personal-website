import Vuex from 'vuex';
import DefaultLayout from '~/layouts/Default.vue'
import { TOGGLE_NAV, NAV_VISIBLE, SET_NAV } from './store'


export default function (Vue, { router, head, isClient, appOptions }) {
  Vue.use(Vuex);
 
  appOptions.store = new Vuex.Store({
    state: {
        NAV_VISIBLE: false,
    },    
    mutations:{
        [TOGGLE_NAV](state) {
            state.NAV_VISIBLE = !state.NAV_VISIBLE;
        },
        [SET_NAV](state, opt) {
            state.NAV_VISIBLE = opt;
        },
    }
  });

  router.afterEach((to, from) => {
    appOptions.store.commit(SET_NAV, false);
  })

  // Set default layout as a global component
  Vue.component('Layout', DefaultLayout)

  head.link.push({
    rel: "stylesheet",
    type: "text/css",
    href: "https://use.fontawesome.com/releases/v5.8.1/css/all.css"
  })

}
