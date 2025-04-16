<template>

<a>hello world</a>
<button @click="fetchThreads">aaa</button>
</template>

<script setup lang="ts">

type Threads = {
    id: number,
    user_name: string
    content: number
};


async function fetchThreads(): Promise<Threads> {
    const url = "http://localhost:8000/threads";

    const response = await fetch(
        url,
        {
            method: "GET",
            headers: {"content-type": "application/json"},
        }
    );
    
    const threads = await response.json();
    return threads;

}



</script>


<style scoped>

</style>
