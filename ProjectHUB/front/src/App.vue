<template>
  <img alt="Vue logo" src="assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import axios from 'axios'
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data: ()=> ({
    projects: []
  }),
  components: {
    HelloWorld
  },
  mounted () {
  axios.get('http://localhost:8000/api/projects/').then((response) => {
    this.projects = response.data
  })
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
}
</style>
