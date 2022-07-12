<template>
  <div v-if="room" class="game-view">
    <h1>{{ room.room_name }} (round {{ room.games + 1 }})</h1>
    <score-board :me="me" :opponent="opponent" :games="room.games"/>
    <h2>{{ turnDisplay }}</h2>
    <div class="view-split">
      <div class="view-part">
        <tic-tac-toe-game :board="room.board" @choose-square="chooseSquare"/>
      </div>
      <div class="view-part">
        <chat :messages="messages" @send-message="sendMessage"/>
      </div>
    </div>
  </div>
</template>

<script>
import TicTacToeGame from "@/components/TicTacToeGame.vue";
import ScoreBoard from '@/components/ScoreBoard.vue';
import Chat from '@/components/Chat.vue';

export default {
  name: "GameView",
  components: {
    TicTacToeGame,
    ScoreBoard,
    Chat
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
    messages () {
      return this.room.messages;
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
    },
    sendMessage(message) {
      const data = {
        message,
        room: this.room.room_name,
        nickname: this.me.name,
      }
      this.$socket.emit('message', data); 
    }
  }
}
</script>

<style scoped>
  .view-split {
    display: flex;
    flex-direction: row;
  }

  .view-part {
    width: 50%;
  }

</style>