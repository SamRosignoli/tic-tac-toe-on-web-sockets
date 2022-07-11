import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSocketIO from 'vue-socket.io'
import SocketIO from 'socket.io-client'

Vue.config.productionTip = false

const options = { auth: process.env.VUE_APP_SOCKET_KEY }

Vue.use(new VueSocketIO({
  debug: true,
  connection: SocketIO('http://localhost:5000', options), //options object is Optional
  vuex: {
    store,
    actionPrefix: "onSocketEvent_",
  }
}));

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
