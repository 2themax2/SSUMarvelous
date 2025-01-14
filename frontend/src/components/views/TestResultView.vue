<script setup>

import {onMounted, ref} from "vue";
import axios from "axios";
import { useRoute, useRouter } from 'vue-router'
import { useToast } from "primevue/usetoast";
import {Toast} from "primevue";
import BarChart from '../BarChart.vue';
import RadarChart from '../RadarChart.vue'
import RoleDescription from "@/components/RoleDescription.vue";

const router = useRouter()
const route = useRoute()
const toast = useToast();

const topThree = ref()
const scores = ref()
const header = ref()

onMounted(()=> {
  axios.get('https://marvelous-ssu.azurewebsites.net/student/440536/get_test_result')
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
    <div class="flex align-items-center justify-content-center mt-5">
      <h1 class="font-bold" style="color: var(--p-sky-950)">You are a: {{header}}</h1>
    </div>
    <Toast />
    <BarChart :top="topThree"/>
    <RoleDescription :top="topThree"/>
    <RadarChart :scores="scores" />
  </div>
</template>