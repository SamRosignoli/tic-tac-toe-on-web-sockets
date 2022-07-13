import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSocketIO from 'vue-socket.io'
import SocketIO from 'socket.io-client'

Vue.config.productionTip = false

const options = { auth: process.env.VUE_APP_SOCKET_KEY }

const serverAddress = 'http://localhost:5000';

const actionPrefix = 'onSocketEvent_';

Vue.use(new VueSocketIO({
  debug: true,
  connection: SocketIO(serverAddress, options),
  vuex: { store, actionPrefix }
}));

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
