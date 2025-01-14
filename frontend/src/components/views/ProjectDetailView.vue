<script setup>
import {onMounted, ref} from 'vue';
import axios from "axios";
import Column from "primevue/column";
import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Card from "primevue/card";
const props = defineProps(['id'])
const projectData = ref()
const studentsGroups =  ref()
const studentsNoGroup = ref()

onMounted(() => {
    axios.get(`https://marvelous-ssu.azurewebsites.net/project/${props.id}/get_project`)
        .then((response) => {
            console.log(response.data)
            projectData.value = response.data
            studentsNoGroup.value = response.data.students.no_group
            studentsGroups.value = response.data.students.groups
            console.log(studentsNoGroup)
        })
        .catch(err => { console.log(err.data)})
})

</script>

<template>

    <div class="flex flex-wrap pt-3">
        <div class="flex flex-col align-items-left justify-content-center p-2 mt-5">
            <h1 class="font-bold" style="color: var(--p-sky-950)">Project: {{ projectData.name }}</h1>
            <div class="flex flex-row">
                <Card >
                    <template #title> Teacher:</template>
                    <template #content>
                        <p>
                            {{projectData.teacher}}
                        </p>
                    </template>
                </Card>
                <Card>
                    <template #title>
                        Description:
                    </template>
                    <template #content>
                        {{projectData.description}}
                    </template>
                </Card>
            </div>

        </div>
        <div v-if="studentsGroups">

        </div>
        <div v-else>
            <h3 style="color: var(--p-sky-900)">Students </h3>
            <DataTable :value="studentsNoGroup" tableStyle="min-width: 50rem">
                <Column field="name" header="Name"></Column>
                <Column field="mayor" header="Mayor"></Column>
                <Column field="role" header="Role"></Column>
            </DataTable>
        </div>

    </div>
</template>

