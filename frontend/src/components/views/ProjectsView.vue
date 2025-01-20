<script setup>
import {onMounted,  ref} from "vue";
import axios from "axios";
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Button from 'primevue/button'
import router from "@/router.js";

const projects = ref()

onMounted(()=> {
    axios.get('https://marvelous-ssu.azurewebsites.net/project')
        .then((response) => {
            console.log(response.data)
            projects.value = response.data
        })
        .catch(err => {
            console.log(err.data)
        })
})

const handleClick = (data) => {
    router.push({path: `/projects/${data.project_nr}`})
}
</script>

<template>
    <div class="flex flex-wrap pt-3">
        <DataTable :value="projects" tableStyle="min-width: 50rem">
            <Column field="name" header="Name"></Column>
            <Column field="description" header="Description"></Column>
            <Column field="" header="Teacher"></Column>
            <Column class="w-24 !text-end">
                <template #body="{ data }">
                    <Button icon="pi pi-info" @click="handleClick(data)" severity="secondary" rounded></Button>
                </template>
            </Column>
        </DataTable>
    </div>


</template>