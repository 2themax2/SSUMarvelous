<script setup>
import TestQuestions from './components/TestQuestions.vue'
import {onMounted, ref, provide} from "vue";
import axios from "axios";

const questions = ref([]);
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
  </header>

  <main>
    <TestQuestions/>
  </main>
</template>

