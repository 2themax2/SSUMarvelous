<script setup>
import { ref, defineProps, watchEffect} from "vue";
import Chart from 'primevue/chart';

const radarData = ref();
const radarOptions = ref();

const props = defineProps(['scores'])

function capitalizeFirstLetter(string) {
  return string.charAt(0).toUpperCase() + string.slice(1)
}

const setRadarData = () => {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--p-text-color');
    let data = []
    let labels = []
    for (let key in props.scores) {
      labels.push(capitalizeFirstLetter(key))
      data.push(props.scores[key])
    }

    return {
        labels: labels,
        datasets: [
            {
                label: 'All scores',
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
          title:{
            display: true,
            text: 'These are your overall scores',
            fullSize: true,
            align: 'center',
            font: {
              size: 18
            },
            padding: {
                bottom: 1
            }
          },
          legend: {
            display: false
          }
        },
        scales: {
            r: {
                pointLabels: {
                 font: {
                   size: 14
                 }
                },
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

watchEffect(() => {
  if (props.scores){
    radarData.value = setRadarData();
    radarOptions.value = setRadarOptions();
  }

})
</script>
<template>
<!--  {{scores}}-->
  <div class="bg-primary flex justify-content-center align-items-center w-10 p-3">
    <Chart type="radar" :data="radarData" :options="radarOptions" class=" flex w-6 p-3 flex justify-content-center align-items-center" />
  </div>
</template>
<style scoped>

</style>