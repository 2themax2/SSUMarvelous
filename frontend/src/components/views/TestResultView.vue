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
        // barData.value = setBarData();
        // barOptions.value = setBarOptions();
        // radarData.value = setRadarData();
        // radarOptions.value = setRadarOptions();
      })
      .catch(err => {
          console.log(err)
          toast.add({severity: 'error', summary: err.response.data.error})
      })
});
provide('topThree', topThree.values)
        provide('scores', scores)



// bar data
const barData = ref();
const barOptions = ref();

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1)
}

const getLabels = (results) => {
  let resultLabels = []
  for (let i=0; i<results.value.length; i++){
    resultLabels.push(capitalizeFirstLetter(results.value[i][0]))
  }
  return resultLabels
}

const getData = (results) => {
  let data = []
  for (let i=0; i<results.value.length; i++){
    data.push(results.value[i][1])
  }
  return data
}

const setBarData = () => {
    const documentStyle = getComputedStyle(document.documentElement);

    return {
        labels: getLabels(topThree),
        datasets: [
            {
                label: 'Top three results',
                backgroundColor: 'rgba(14, 165, 233, 0.2)',
                borderColor: documentStyle.getPropertyValue('--p-sky-500'),
                data: getData(topThree),
                borderWidth: 2
            }
        ]
    };
};
const setBarOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--p-text-color');
    const textColorSecondary = documentStyle.getPropertyValue('--p-text-muted-color');
    const surfaceBorder = documentStyle.getPropertyValue('--p-content-border-color');

    return {
        maintainAspectRatio: false,
        aspectRatio: 0.8,
        plugins: {
            legend: {
                labels: {
                    color: textColor
                }
            },

        },
        scales: {
            x: {
                ticks: {
                    color: textColorSecondary,
                    font: {
                        weight: 500
                    }
                },
                grid: {
                    display: false,
                    drawBorder: false
                }
            },
            y: {
                max: 12,
                min: 1,
                ticks: {
                  stepSize: 1,
                  color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder,
                    drawBorder: false
                }
            }
        }
    };
}

//radar

const radarData = ref();
const radarOptions = ref();

const setRadarData = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--p-text-color');
    let data = []
    let labels = []
    for (let key in scores.value) {
      labels.push(capitalizeFirstLetter(key))
      data.push(scores.value[key])
    }

    return {
        labels: labels,
        datasets: [
            {
                label: 'My First dataset',
                fill: true,
                borderColor: documentStyle.getPropertyValue('--p-sky-400'),
                backgroundColor: 'rgba(14, 165, 233, 0.2)',
                pointBackgroundColor: documentStyle.getPropertyValue('--p-sky-400'),
                pointBorderColor: documentStyle.getPropertyValue('--p-sky-400'),
                pointHoverBackgroundColor: textColor,
                pointHoverBorderColor: documentStyle.getPropertyValue('--p-sky-400'),
                data: data,
                borderWidth: 2
            }
        ]
    };
};
const setRadarOptions = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--p-text-color');
    const textColorSecondary = documentStyle.getPropertyValue('--p-text-muted-color');

    return {
        plugins: {
            legend: {
                labels: {
                    color: textColor
                }
            }
        },
        scales: {
            r: {
                grid: {
                    color: textColorSecondary
                },
                max: 12,
                min: 1,
                ticks: {
                  stepSize: 1
                }
            }
        }
    };
}



</script>

<template>
  <div class="flex flex-column justify-content-center align-items-center w-full">
    <header class="header-section flex align-center">
      <h1>You are a: {{header}}</h1>
    </header>
    <Toast />
<!--    <BarChart />-->
    <RadarChart />
<!--    <div class="flex justify-content-center align-items-center w-10 h-24rem p-3">-->
<!--      <Chart type="bar" :data="barData" :options="barOptions" class="flex h-full w-full"  />-->
<!--    </div>-->
<!--    <div class="bg-primary flex justify-content-center align-items-center w-8 p-3">-->
<!--      <Chart type="radar" :data="radarData" :options="radarOptions" class=" w-full p-3 flex justify-content-center align-items-center" />-->
<!--    </div>-->
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