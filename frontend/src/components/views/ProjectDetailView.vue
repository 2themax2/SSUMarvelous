<script setup>
import {onBeforeMount, onMounted, onUpdated, ref, watchEffect} from 'vue';
import axios from "axios";
import Column from "primevue/column";
import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Card from "primevue/card";
const props = defineProps(['id'])
const projectData = ref()
const studentsGroups =  ref()
const studentsNoGroup = ref()
const token = ref()
const data = ref([])

onBeforeMount(() => {
    if(props.id){
        axios.get(`https://marvelous-ssu.azurewebsites.net/project/${props.id}/get_project`)
            .then((response) => {
                console.log(response.data)
                projectData.value = response.data
                studentsNoGroup.value = projectData.value.students.no_group
                studentsGroups.value = projectData.value.students.groups
            })
            .catch(err => { console.log(err)})
    }
})

// onUpdated(() => {
//     makeData()
// })

const makeData = () => {
    for (let i=1; i<=Object.keys(studentsGroups.value).length; i++){
        let record = {}
        record['group_id'] = i
        record['students'] = studentsGroups.value[i]
        data.value.push(record)
    }
}

const makeGroups = () => {
    axios.get('https://marvelous-ssu.azurewebsites.net/csrf-token/')
        .then((response) => {
            console.log(response.data)
            token.value = response.data.csrfToken
            axios.post(`https://marvelous-ssu.azurewebsites.net/project/make_groups/`,
                {project_nr: props.id}, {
                    headers: {'Content-Type': 'application/json',
                    'X-CSRFToken': token.value },
                credentials: 'include',
                })
                .then((res) => {
                console.log(res.data)
                })
                .catch(err => { console.log(err)})
        })
        .catch(error => {console.log(error)})
}

</script>

<template>
    <div class="flex flex-column justify-content-center ">
        <h1 class="font-bold" style="color: var(--p-sky-950)">Project: {{ projectData.name }}</h1>
        <div class="flex flex-row">
            <Card class="flex m-2">
                <template #title> Teacher:</template>
                <template #content>
                    <p>
                        {{projectData.teacher}}
                    </p>
                </template>
            </Card>
            <Card class="flex m-2">
                <template #title>Description:</template>
                <template #content>
                    {{projectData.description}}
                </template>
            </Card>
        </div>

        <div v-if="Object.keys(studentsGroups).length !== 0">
            <div class="flex justify-content-between m-2">
                <h3 style="color: var(--p-sky-900)">Groups </h3>
<!--                <Button class="p-2 m-1" label="Make groups" @click="makeGroups"/>-->
            </div>

<!--            <DataTable :value="data" v-model:expandedRows="expandedRows" dataKey="group_id"-->
<!--                       @rowExpand="onRowExpand" @rowCollapse="onRowCollapse" tableStyle="min-width: 50rem">-->
<!--                <Column expander style="width: 5rem" />-->
<!--&lt;!&ndash;                <Column field="group_id" header="Group"></Column>&ndash;&gt;-->
<!--                <template #expansion="slotProps">-->
<!--                    <div class="p-4">-->
<!--                        <h5>{{ slotProps.data.group_id }}</h5>-->
<!--                        <DataTable :value="slotProps.data.students">-->
<!--                            <Column field="name" header="Name"></Column>-->
<!--                            <Column field="mayor" header="Mayor"></Column>-->
<!--                            <Column field="role" header="Role"></Column>-->
<!--                        </DataTable>-->
<!--                    </div>-->
<!--                </template>-->
<!--            </DataTable>-->
        </div>


        <div v-else >
            <div class="flex justify-content-between m-2">
                <h3 style="color: var(--p-sky-900)">Students </h3>
                <Button class="p-2 m-1" label="Make groups" @click="makeGroups"/>
            </div>

            <DataTable :value="studentsNoGroup"  tableStyle="min-width: 50rem">
                <Column field="name" header="Name"></Column>
                <Column field="mayor" header="Mayor"></Column>
                <Column field="role" header="Role"></Column>

            </DataTable>
        </div>
    </div>
</template>

