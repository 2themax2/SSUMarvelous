<script setup>
import {inject, onMounted, ref, provide} from "vue";
import axios from "axios";
import { useRoute, useRouter } from 'vue-router'
import { useToast } from "primevue/usetoast";
import {Toast} from "primevue";
import Chart from 'primevue/chart';

const topThree = inject('topThree')

onMounted(() => {
  barData.value = setBarData();
  barOptions.value = setBarOptions();
  console.log(topThree)
})

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
  console.log(results)
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


</script>

<template>
<!--  <div class="flex justify-content-center align-items-center w-10 h-24rem p-3">-->
<!--      <Chart type="bar" :data="barData" :options="barOptions" class="flex h-full w-full"  />-->
<!--  </div>-->

</template>

<style scoped>

</style>