<script setup>
import {defineProps, onMounted, ref, watchEffect} from "vue";
import axios from "axios";
import Panel from 'primevue/panel';


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
  <div class="flex w-10 p-3">

    <div v-for="item in descriptionsTop">
      <Panel class="flex m-2" >
        <template #header>
          <div class="flex items-center gap-2">
            <span class="font-bold p-panel-header p-panel-header-color">{{item[0]}}</span>
          </div>
        </template>
        <p class="m-0">
          {{item[1]}}
        </p>
      </Panel>
    </div>
  </div>

</template>
<style scoped>

</style>