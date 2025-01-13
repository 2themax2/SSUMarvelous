<script setup>
import {ref, watchEffect} from "vue";
import Chart from 'primevue/chart';

const props = defineProps(['top'])

// bar data
const barData = ref();
const barOptions = ref();

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1)
}

const setBarData = () => {
  const documentStyle = getComputedStyle(document.documentElement);
  let data = []
  let labels = []

  for (let i=0; i<props.top.length; i++){
      data.push(props.top[i][1])
      labels.push(capitalizeFirstLetter(props.top[i][0]))
  }

  return {
    labels: labels,
    datasets: [
      {
        label: 'Top three results',
        backgroundColor: 'rgba(14, 165, 233, 0.2)',
        borderColor: documentStyle.getPropertyValue('--p-sky-500'),
        data: data,
        borderWidth: 2
      }
    ]
  }
}
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

watchEffect(() => {
  if (props.top){
    barData.value = setBarData();
    barOptions.value = setBarOptions();
  }
})

</script>

<template>
  <div class="flex justify-content-center align-items-center w-10 h-24rem p-3">
      <Chart type="bar" :data="barData" :options="barOptions" class="flex h-full w-full"  />
  </div>

</template>

<style scoped>

</style>