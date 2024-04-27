import "../sass/uselessthingstosteal.scss"

import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import router from './router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUser, faLock, faCaretLeft, faCaretRight } from '@fortawesome/free-solid-svg-icons'

library.add(faUser, faLock, faCaretLeft, faCaretRight)

const store = createStore({
  state () {
    return {
      username: "",
      token: "",
      connection_count: -1,
      next_card: "",
      next_theft: ""
    }
  },
  mutations: {
    set_user_data (state, payload) {
  		state.username = payload.username;
  		state.token = payload.token;
      state.connection_count = payload.connection_count;
    },
    set_next_card (state, payload) {
      state.next_card = payload.next_card;
    },
    set_next_theft (state, payload) {
      state.next_theft = payload.next_theft;
    },
    disable_tutorial (state) {
      state.connection_count = -1;
    }
  },
  getters: {
    is_connected (state) {
      return state.username != "" && state.token != "";
    },
    is_first_time (state) {
      return state.connection_count == 0;
    },
    next_card (state) {
      const now = Date.now();
      const next_card = new Date(state.next_card);
      return (next_card - now) > 0 ? (next_card - now) : 0;
    },
    next_theft (state) {
      const now = Date.now();
      const next_theft = new Date(state.next_theft);
      return (next_theft - now) > 0 ? (next_theft - now) : 0;
    }
  }
})

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon)

app.use(router)

app.use(store)

app.config.globalProperties.$url_prefix = "http://127.0.0.1:5000"

app.mount('#app')