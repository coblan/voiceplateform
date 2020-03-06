<template>
    <div>
        <div v-for="link in ctx.links" style="padding: 20px">
            <a :href="link.src"  v-text="link.label"></a>
            <span style="display: inline-block;margin-left: 20px" v-text="link.detail"></span>
        </div>

    </div>
</template>
<script>
    export default {
        props:['ctx']
    }
</script>