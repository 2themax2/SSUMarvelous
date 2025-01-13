<script setup>

import {inject, onMounted, ref, provide} from "vue";
import axios from "axios";
import { useRoute, useRouter } from 'vue-router'
import { useToast } from "primevue/usetoast";
import {Toast} from "primevue";
import Chart from 'primevue/chart';
import BarChart from '../BarChart.vue';
import RadarChart from '../RadarChart.vue'

const router = useRouter()
const route = useRoute()
const toast = useToast();

const topThree = ref()
const scores = ref()
const header = ref()

onMounted(()=> {
  axios.get('http://127.0.0.1:8000/student/440536/get_test_result')
      .then((response) => {
        console.log(response.data)
        topThree.value = response.data.topThree
        scores.value = response.data.allScores
        header.value = capitalizeFirstLetter(topThree.value[0][0])
      })
      .catch(err => {
          console.log(err)
          toast.add({severity: 'error', summary: err.response.data.error})
      })
});

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1)
}

</script>

<template>
  <div class="flex flex-column justify-content-center align-items-center w-full">
    <header class="header-section flex align-center">
      <h1>You are a: {{header}}</h1>
    </header>
    <Toast />
    <BarChart :top="topThree"/>
    <RadarChart :scores="scores" />
  </div>
</template>

<style scoped>
.header-section {
  margin-bottom: 20px;
}

.text-center {
  text-align: center;
}


</style>