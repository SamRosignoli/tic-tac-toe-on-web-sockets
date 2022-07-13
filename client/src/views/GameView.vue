<template>
  <div v-if="room" class="game-view">
    <h1>{{ room.room_name }} (round {{ room.games + 1 }})</h1>
    <score-board :me="me" :opponent="opponent" :games="room.games"/>
    <h2>{{ turnDisplay }}</h2>
    <tic-tac-toe-game :board="room.board" @choose-square="chooseSquare"/>
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
    opponent () {
      return this.$store.getters.opponent;
    },
    turnDisplay () {
      if (this.opponent) {
        return `It's ` + this.room.turn + `'s turn`
      }
      return 'Waiting for an opponent...'
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
