<template>
  <div id="app">
    <h1>Game Of Life</h1>
    <life-component></life-component>
  </div>
</template>

<script>
import lifeComponent from './components/lifeComponent.vue'

export default {
  name: 'App',
  components: {
    lifeComponent,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  margin-left: 36%;
  margin-right: 36%;
}

body {
  background-color: antiquewhite;
}
</style>
