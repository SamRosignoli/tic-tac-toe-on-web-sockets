<template>
  <div class="tic-tac-toe-game">
    <div
      v-for="(item, index) in board"
      :key="index"
      class="game-grid-item"
      @click="chooseSquare(index)"
    >
      <span>{{ item }}</span>
    </div>
  </div>
</template>
<script>
export default {
  name: 'TicTacToeGame',
  props: ['board'],
  methods: {
    chooseSquare(index) {
      this.$emit('choose-square', index)
    }
  }
}
</script>

<style scoped>
  .tic-tac-toe-game {
    width: 450px;
    display: grid;
    grid-template-columns: auto auto auto;
  }

  .game-grid-item {
    background-color: rgba(255, 255, 255, 0.8);
    border: 1px solid rgba(0, 0, 0, 0.8);
    height: 150px;
    width: 150px;
    font-size: 50px;
    display: grid;
    place-items: center;
    font-weight: 600;
  }
</style>