import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router/index'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    connected: false,
    nickname: null,
    room: {},
    joinErrorMessage: '',
    winnerMessage: ''
  },
  getters: {
    isLoading (state) {
      return !state.connected;
    },
    isMyTurn (state) {
      return state.room.turn === state.nickname;
    },
    mySymbol (state) {
      if (!state.nickname) {
        return null;
      }
      return state.room.users[state.nickname].symbol;
    },
    me (state) {
      if (Object.keys(state.room).length === 0) {
        return null;
      }
      const userNames = Object.keys(state.room.users);
      const nickname = userNames.find(name => name === state.nickname);
      return nickname ? {
        name: nickname,
        ...state.room.users[nickname]
      } : null
    },
    opponent (state) {
      if (Object.keys(state.room).length === 0) {
        return null;
      }
      const userNames = Object.keys(state.room.users);
      const opponentName = userNames.find(name => name !== state.nickname);
      return opponentName ? {
        name: opponentName,
        ...state.room.users[opponentName]
      } : null
    }
  },
  mutations: {
    setConnected(state, val) {
      state.connected = val;
    },
    setNickname(state, val) {
      state.nickname = val;
    },
    setRoom(state, val) {
      state.room = val;
    },
    setJoinErrorMessage(state, val) {
      state.joinErrorMessage = val;
    },
    setWinnerMessage(state, val) {
      state.winnerMessage = val;
    },
  },
  actions: {
    onSocketEvent_connect({ commit }, result) {
      if (result) {
        commit('setConnected', result !== "Unauthorized");
      }
    },
    onSocketEvent_joinRoomSelf({ commit }, data) {
      if (data.status === 'success') {
        commit('setNickname', data.nickname);
        router.push('game');
      } else {
        commit('setJoinErrorMessage', data.message);
      }
    },
    onSocketEvent_userJoined({ commit }, data) {
      if (data.status === 'success') {
        commit('setRoom', data.room);
      }
    },
    onSocketEvent_updateRoom({ commit }, data) {
      if (data.status === 'success') {
        commit('setRoom', data.room);
        if (data.end) {
          commit('setWinnerMessage', data.end);
        }
      }
    },
    onSocketEvent_message({ commit }, data) {
      if (data.status === 'success') {
        commit('setRoom', data.room);
      }
    }
  },
  modules: {
  }
})