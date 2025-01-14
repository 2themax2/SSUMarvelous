<script setup>
import {defineProps, onMounted, ref, watchEffect} from "vue";
import axios from "axios";
import Card from 'primevue/card';

const descriptions = {}
const props = defineProps(['top'])
const descriptionsTop = ref([])

onMounted(()=> {
  axios.get('https://marvelous-ssu.azurewebsites.net/role')
      .then((response) => {
        console.log(response.data)
        let data = response.data
        data.forEach( item => {
          descriptions[item.role.toLowerCase()] = [item.role, item.description]
        })
        console.log(descriptions)
      })
      .catch(err => {
        console.log(err)
      })
});

watchEffect(() => {
  if (props.top && descriptions) {
    props.top.forEach(item => {
      descriptionsTop.value.push(descriptions[item[0]])
    })
  }
})


</script>

<template>
  <div class="flex  flex-column w-10 p-3">
      <div class="flex align-items-center justify-content-center mt-5">
          <h3 class="font-bold" style="color: var(--p-sky-950)">Role descriptions</h3>
      </div>
    <div v-for="item in descriptionsTop">
      <Card class="mt-3" >
          <template #title> {{item[0]}}</template>
          <template #content>
              <p>
                  {{item[1]}}
              </p>
          </template>

      </Card>
    </div>
  </div>

</template>
<style scoped>

</style>