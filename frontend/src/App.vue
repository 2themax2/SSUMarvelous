<script setup>
import TestQuestions from './components/TestQuestions.vue'
import {onMounted, ref, provide} from "vue";
import axios from "axios";

const questions = ref( [
      "I enjoy coming up with unconventional solutions that often surprise others.",
        "I get inspired by brainstorming sessions and prefer creating something new over repeating existing ideas.",
         "I easily make connections and see potential collaboration partners everywhere.",
         "I enjoy connecting people and love exploring new opportunities.",
         "I have a good overview and ensure everyone knows what needs to be done.",
        "I logically divide tasks and monitor the team's progress.",
         "I like motivating others to take action and make quick decisions.",
        "I perform well under time pressure and enjoy a fast work pace.",
         "I love delving into problems and asking critical questions when needed.",
         "Before making a decision, I like to consider all sides of the matter.",
         "I find it important that everyone feels comfortable and can truly collaborate.",
         "I quickly notice tensions or irritations in the group and try to resolve them.",
         "I enjoy translating great plans into a concrete action plan.",
         "I work in a structured manner and like to complete tasks efficiently.",
        "I am a perfectionist and check that everything is correct down to the last detail.",
         "I derive satisfaction from completing a project meticulously.",
         "I enjoy diving deep into a subject and mastering the finer details of the craft.",
         "I like sharing my expertise with others and continuously learning.",
        ]);
// onMounted(()=> {
//   axios.get('http://127.0.0.1:8000/RoleTest/').then((response) => {
//     console.log(response.data)
//     questions.value = response.data
//   })
// });

provide('questions',questions)
</script>

<template>
  <header>
  </header>

  <main>
    <TestQuestions/>
  </main>
</template>

