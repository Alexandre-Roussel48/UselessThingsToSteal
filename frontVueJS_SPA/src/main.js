import "../../static/sass/uselessthingstosteal.scss"

import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'
import router from './router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUser, faLock } from '@fortawesome/free-solid-svg-icons'

library.add(faUser, faLock)

const store = createStore({
  state () {
    return {
      username: "",
      token: ""
    }
  },
  mutations: {
    set_user_data (state, payload) {
  		state.username = payload.username;
  		state.token = payload.token;
    }
  },
  getters: {
    is_connected (state) {
      return state.username != "" && state.token != "";
    }
  }
})

const app = createApp(App)

app.component('font-awesome-icon', FontAwesomeIcon)

app.use(router)

app.use(store)

app.config.globalProperties.$url_prefix = "http://127.0.0.1:5000"

app.mount('#app')