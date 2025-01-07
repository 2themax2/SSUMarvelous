<script setup>
// import TestQuestions from './components/TestQuestions.vue'
import {onMounted, ref, provide} from "vue";
import axios from "axios";
// import NavBar from "./components/NavBar.vue";

const questions = ref([])
onMounted(()=> {
  axios.get('http://127.0.0.1:8000/RoleTest/').then((response) => {
    console.log(response.data)
    questions.value = response.data
  })
});

provide('questions',questions)


</script>

<template>
  <header>
<!--    <NavBar />-->
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/test">Test</RouterLink>
    </nav>
  </header>
  <main>
    <RouterView />
<!--    <TestQuestions/>-->
  </main>
</template>

