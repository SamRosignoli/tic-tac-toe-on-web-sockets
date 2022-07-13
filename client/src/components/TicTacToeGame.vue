<template>
  <div class="tic-tac-toe-game">
    <div
      v-for="(item, index) in board"
      :key="index"
      class="game-grid-item"
      :class="{ hoverable: !item.length && isMyTurn }"
      @click="chooseSquare(index)"
    >
      <span :class="item === 'X' ? 'x-square' : 'o-square'">{{ item }}</span>
    </div>
  </div>
</template>
<script>
export default {
  name: 'TicTacToeGame',
  props: ['board', 'isMyTurn'],
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
    background-color: #fff;
    border: 1px solid #2c3e50;
    height: 150px;
    width: 150px;
    font-size: 50px;
    display: grid;
    place-items: center;
    font-weight: 600;
    cursor: default;
  }

  .hoverable {
    background-color: #fff;
    transition: 0.5s ease;
    cursor: pointer;
  }

  .hoverable:hover {
    background-color: #eee;
  }

  .x-square {
    color: #41b783;
  }

  .o-square {
    color: #2c3e50;
  }
</style>