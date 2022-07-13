<template>
  <div v-if="room" class="game-view">
    <h1>{{ room.room_name }} (round {{ room.games + 1 }})</h1>
    <score-board :me="me" :opponent="opponent" :games="room.games" :turn="room.turn"/>
    <h2>{{ turnDisplay }}</h2>
    <tic-tac-toe-game :board="room.board" :is-my-turn="isMyTurn" @choose-square="chooseSquare"/>
    <transition name="bounce">
      <h3 v-if="showWinnerMessage">{{ winnerMessage }}</h3>
    </transition>
  </div>
</template>

<script>
import TicTacToeGame from "@/components/TicTacToeGame.vue";
import ScoreBoard from '@/components/ScoreBoard.vue';

export default {
  name: "GameView",
  components: {
    TicTacToeGame,
    ScoreBoard
  },
  data() {
    return {
      showWinnerMessage: false
    }
  },
  watch: {
    winnerMessage() {
      this.showWinnerMessage = true;
      setTimeout(() => {
        this.showWinnerMessage = false;
      }, 2000)
    }
  },
  created() {
    if (Object.keys(this.$store.state.room).length === 0) {
      this.$router.push('/');
    }
  },
  computed: {
    room () {
      return this.$store.state.room;
    },
    me () {
      return this.$store.getters.me;
    },
    isMyTurn () {
      return this.opponent && this.me.name === this.room.turn;
    },
    opponent () {
      return this.$store.getters.opponent;
    },
    turnDisplay () {
      if (this.opponent) {
        return `It's ` + this.room.turn + `'s turn`
      }
      return 'Waiting for an opponent...'
    },
    winnerMessage () {
      return this.$store.state.winnerMessage;
    }
  },
  methods: {
    chooseSquare (index) {
      if (this.room.board[index] === '' && this.opponent && this.room.turn === this.me.name) {
        const data = {
          index,
          roomName: this.room.room_name,
          user: this.me,
        }
        this.$socket.emit('chooseSquare', data);
      }
    }
  }
}
</script>

<style scoped>
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
</style>
