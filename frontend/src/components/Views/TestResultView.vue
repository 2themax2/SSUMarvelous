<script setup>

import {onMounted, ref} from "vue";
import axios from "axios";
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()
const route = useRoute()

const questions = ref([])
// onMounted(()=> {
//   axios.get('http://127.0.0.1:8000/Student/').then((response) => {
//     console.log(response.data)
//     questions.value = response.data
//   })
// });
const result = "You are a Plant!"
</script>

<template>
  <header class="header-section">
      <h1 class="text-center">Test Result</h1>
  </header>
  <p class="flex align-items-center">{{result}}</p>

</template>